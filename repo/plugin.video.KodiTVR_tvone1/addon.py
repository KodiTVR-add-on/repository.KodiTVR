# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 RACC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import unicode_literals

import sys
from xbmcgui import ListItem
from kodi_six import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from routing import Plugin

import os
import json
import requests
from requests.exceptions import RequestException
from future.moves.urllib.parse import urljoin, urlencode
from resources.lib.relay import Relay

try:
    from xbmcvfs import translatePath
except ImportError:
    from kodi_six.xbmc import translatePath

addon = xbmcaddon.Addon()
plugin = Plugin()
plugin.name = addon.getAddonInfo("name")
USER_DATA_DIR = translatePath(addon.getAddonInfo("profile"))
cache_time = int(addon.getSetting("cache_time") or "0") * 60 * 60
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)


def log(msg, level=xbmc.LOGDEBUG):
    xbmc.log("[{0}] {1}".format(plugin.name, msg), level=level)


def xbmc_curl_encode(url):
    return "{0}|{1}".format(url[0], urlencode(url[1]))


TV = Relay(USER_DATA_DIR)


@plugin.route("/")
def root():
    categories = ["channels", "news", "shows", "movies", "sports", "music"]
    list_items = []
    for c in categories:
        li = ListItem(c)
        url = plugin.url_for(list_channels, cat=c)
        list_items.append((url, li, True))

    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("/list_channels/<cat>")
def list_channels(cat=None):
    playback_mode = addon.getSetting("playback_mode")
    names = []
    list_items = []
    for channel in TV.get_channels_by_category(cat, cache_time):
        title = channel.name
        if title in names:
            continue
        else:
            names.append(title)
        image = channel.img
        li = ListItem(title)
        li.setProperty("IsPlayable", "true")
        li.setArt({"thumb": image, "icon": image})
        li.setInfo(type="Video", infoLabels={"Title": title, "mediatype": "video"})
        li.setContentLookup(False)
        if playback_mode == "HLS":
            url = plugin.url_for(play, cat=cat, channel_id=channel._id)
        elif playback_mode == "RTMFP":
            url = plugin.url_for(play_rtmfp, cat=cat, channel_id=channel._id)
            fallback_url = plugin.url_for(play_netgroup, cat=cat, channel_id=channel._id)
            li.addContextMenuItems([("Play RTMFP Netgroup (P2P)", "PlayMedia({0})".format(fallback_url))])
        else:
            url = plugin.url_for(play_netgroup, cat=cat, channel_id=channel._id)
            fallback_url = plugin.url_for(play_rtmfp, cat=cat, channel_id=channel._id)
            li.addContextMenuItems([("Play RTMFP", "PlayMedia({0})".format(fallback_url))])
        list_items.append((url, li, False))
    xbmcplugin.addDirectoryItems(plugin.handle, list_items)
    xbmcplugin.setContent(plugin.handle, "videos")
    xbmcplugin.endOfDirectory(plugin.handle)


@plugin.route("/play/<cat>/<channel_id>/play.pvr")
def play(cat, channel_id):
    channels = TV.get_category_channel_by_id(cat, channel_id, cache_time)
    if channels.count() > 1:
        dialog = xbmcgui.Dialog()
        ret = dialog.select(
            "Choose Stream",
            [json.loads(c.relayer).get("fallbackUrl").split("?")[0] for c in channels],
        )
        if ret >= 0:
            channel = channels[ret]
        else:
            xbmcplugin.setResolvedUrl(plugin.handle, False, ListItem())
    else:
        channel = channels[0]

    if channel:
        title = channel.name
        image = channel.img
        stream = TV.get_stream_cast(channel.relayer)
        stream[1]["verifypeer"] = "false"
        li = ListItem(title, path=xbmc_curl_encode(stream))
        li.setArt({"thumb": image, "icon": image})
        li.setContentLookup(False)
        li.setMimeType("application/vnd.apple.mpegurl")
        xbmcplugin.setResolvedUrl(plugin.handle, True, li)


@plugin.route("/play_rtmfp/<cat>/<channel_id>/play.pvr")
def play_rtmfp(cat, channel_id):
    stream_server = addon.getSetting("stream_server")
    check = None
    channel = None
    try:
        check = requests.get(urljoin(stream_server, "/tvone1"), timeout=2).json().get("tvone1")
    except RequestException:
        dialog = xbmcgui.Dialog()
        dialog.notification(plugin.name, "Stream server unreachable", xbmcgui.NOTIFICATION_ERROR)
        xbmcplugin.setResolvedUrl(plugin.handle, False, ListItem())

    if check:
        channels = TV.get_category_channel_by_id(cat, channel_id, cache_time)
        if channels.count() > 1:
            dialog = xbmcgui.Dialog()
            ret = dialog.select(
                "Choose Stream",
                [json.loads(c.relayer).get("fallbackUrl").split("?")[0] for c in channels],
            )
            if ret >= 0:
                channel = channels[ret]
            else:
                xbmcplugin.setResolvedUrl(plugin.handle, False, ListItem())
        else:
            channel = channels[0]

    if channel:
        title = channel.name
        image = channel.img
        streams = TV.get_stream_server_rtmfp(stream_server, channel.relayer)
        li = ListItem(title, path=streams[1])
        li.setArt({"thumb": image, "icon": image})
        li.setContentLookup(False)
        li.setMimeType("video/x-flv")
        xbmcplugin.setResolvedUrl(plugin.handle, True, li)


@plugin.route("/play_netgroup/<cat>/<channel_id>/play.pvr")
def play_netgroup(cat, channel_id):
    stream_server = addon.getSetting("stream_server")
    check = None
    channel = None
    try:
        check = requests.get(urljoin(stream_server, "/tvone1"), timeout=2).json().get("tvone1")
    except RequestException:
        dialog = xbmcgui.Dialog()
        dialog.notification(plugin.name, "Stream server unreachable", xbmcgui.NOTIFICATION_ERROR)
        xbmcplugin.setResolvedUrl(plugin.handle, False, ListItem())

    if check:
        channels = TV.get_category_channel_by_id(cat, channel_id, cache_time)
        if channels.count() > 1:
            dialog = xbmcgui.Dialog()
            ret = dialog.select(
                "Choose Stream",
                [json.loads(c.relayer).get("fallbackUrl").split("?")[0] for c in channels],
            )
            if ret >= 0:
                channel = channels[ret]
            else:
                xbmcplugin.setResolvedUrl(plugin.handle, False, ListItem())
        else:
            channel = channels[0]

    if channel:
        title = channel.name
        image = channel.img
        streams = TV.get_stream_server_rtmfp(stream_server, channel.relayer)
        li = ListItem(title, path=streams[0])
        li.setArt({"thumb": image, "icon": image})
        li.setContentLookup(False)
        li.setMimeType("video/x-flv")
        xbmcplugin.setResolvedUrl(plugin.handle, True, li)


if __name__ == "__main__":
    plugin.run(sys.argv)
    del TV
