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

import os
import time
import json
import socket
import requests
from .peewee import SqliteDatabase, Model, TextField, FloatField, chunked
from binascii import a2b_hex
from base64 import b64encode, urlsafe_b64encode
from requests.exceptions import RequestException
from future.moves.urllib.parse import urljoin, urlencode
from future.moves.http.cookiejar import LWPCookieJar
from hashlib import md5
from warnings import simplefilter

simplefilter("ignore")
db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class Token(BaseModel):
    token = TextField()
    updated = FloatField(default=time.time)


class Channel(BaseModel):
    category = TextField()
    img = TextField()
    relayer = TextField()
    description = TextField()
    _id = TextField()
    name = TextField()
    language = TextField()
    updated = FloatField(default=time.time)


class Relay:
    def __init__(self, cache_dir):
        DB = os.path.join(cache_dir, "relay0.db")
        COOKIE_FILE = os.path.join(cache_dir, "lwp_cookies.dat")
        db.init(DB)
        db.connect()
        db.create_tables([Token, Channel], safe=True)
        self.base_url = a2b_hex("68747470733a2f2f6170692e6d6f6264726f2e746f").decode("utf-8")
        self.version = a2b_hex("322e322e3320467265656d69756d").decode("utf-8")
        self.user_agent = "Mozilla/5.0 (Linux; Android 7.1.2; AFTN Build/NS6212) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36"
        self.s = requests.Session()
        self.s.headers.update({"User-Agent": self.user_agent})
        self.s.cookies = LWPCookieJar(filename=COOKIE_FILE)
        if os.path.isfile(COOKIE_FILE):
            self.s.cookies.load(ignore_discard=True, ignore_expires=True)

    def __del__(self):
        db.close()
        self.s.cookies.save(ignore_discard=True, ignore_expires=True)
        self.s.close()

    @staticmethod
    def auth_encode(data):
        tab = bytearray.fromhex("d95dc33ea7d9b47ff18332c3b47fd96ee12234c34712b3b47f3222e5d3e8e8b47f13")
        m = 0xFF
        for c in data:
            m = (m + ord(c)) % 256
        res = []
        for i, c in enumerate(data):
            res.append(tab[i % len(tab)] ^ m ^ ord(c))
        return (m ^ 0x93, b64encode(bytearray(res)).decode("utf-8"))

    def image_url(self, img):
        return "{0}|{1}".format(img, urlencode({"User-Agent": self.user_agent}))

    def api_request(self, path, data, headers={}):
        url = urljoin(self.base_url, path)
        r = self.s.post(url, data=data, headers=headers, timeout=10, verify=False)
        r.raise_for_status()
        return r.json()

    def api_get_token(self):
        _data = "signature={0}&cert={1}&time={2:.0f}".format(0x1DA1009FD, 0xAB57C6E5, time.time())
        _crc, _payload = self.auth_encode(_data)
        post_encoded = urlencode({"payload": _payload})
        headers = {
            "X-Crc": _crc,
            "X-Version": b64encode(a2b_hex("fffaf1fee6e7faffe0bca1a2a7a2a1a4a3a6bcdefcf1f7e1fc")),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": len(post_encoded),
        }
        req = requests.Request("POST", urljoin(self.base_url, "/utils/auth"), data=post_encoded)
        prepped = req.prepare()
        prepped.headers = headers
        r = self.s.send(prepped, timeout=10, verify=False)
        r.raise_for_status()
        return r.json().get("token")

    def api_get_category(self, cat):
        data = {
            "data": cat,
            "parental": 0,
            "languages": json.dumps(
                []
            ),  # json.dumps(["hindi","russian","czech","spanish","turkish","french","english","arabic","portuguese","chinese","italian","german"])
            "alphabetical": 0,
            "token": self.get_token(),
            "version": self.version,
        }
        return self.api_request("/streambot/v4/show", data)

    def update_token(self):
        token = self.api_get_token()
        if token:
            with db.atomic():
                Token.delete().execute()
                Token.insert(token=token).execute()

    def update_category_channels(self, cat):
        category_data = self.api_get_category(cat)
        channels = []
        for c in category_data:
            if "relayer" in c:
                channels.append(
                    {
                        "category": c.get("category").lower(),
                        "img": self.image_url(c.get("img")),
                        "relayer": c.get("relayer"),
                        "description": c.get("description", ""),
                        "_id": c.get("_id"),
                        "name": c.get("name"),
                        "language": c.get("language"),
                    }
                )
        with db.atomic():
            if len(channels) > 2:
                Channel.delete().where(Channel.category == cat).execute()
            for batch in chunked(channels, 100):
                Channel.replace_many(batch).execute()

    def get_token(self):
        token = Token.select()
        if token.count() > 0:
            if time.time() - token[0].updated > 7200:
                self.update_token()
        else:
            self.update_token()
        return Token.select()[0].token

    def get_channels_by_category(self, cat, cache_time=0):
        channels = Channel.select().where(Channel.category == cat)
        if channels.count() == 0:
            self.update_category_channels(cat)
        else:
            current_time = int(time.time())
            if current_time - int(channels[0].updated) > cache_time:
                try:
                    self.update_category_channels(cat)
                except (ValueError, RequestException):
                    pass
        """ !! select cursor reset in sqlite after update commit """
        return Channel.select().where(Channel.category == cat)

    def get_category_channel_by_id(self, cat, _id, cache_time=0):
        channels = Channel.select().where(Channel._id == _id)
        if channels.count() == 0:
            self.update_category_channels(cat)
        else:
            current_time = int(time.time())
            if current_time - int(channels[0].updated) > cache_time:
                try:
                    self.update_category_channels(cat)
                except (ValueError, RequestException):
                    pass
        """ !! select cursor reset in sqlite after update commit """
        return Channel.select().where(Channel._id == _id)

    def get_stream_server_rtmfp(self, server, relayer):
        stream_info = json.loads(relayer)
        data = {
            "name": stream_info.get("name"),
            "peer": "false",
            "referer": a2b_hex("6d6f6264726f2e6d65").decode("utf-8"),
            "casting": "false",
            "wifi": "false",
            "token": self.get_token(),
            "playpath": stream_info.get("playpath"),
        }
        for tries in range(10):
            try:
                lb_info = self.api_request("/utils/loadbalancer", data)
            except ValueError:
                lb_info = {}
                break
            except RequestException:
                lb_info = {}
                continue
            try:
                test = socket.socket()
                test.settimeout(5)
                test.connect((lb_info.get("server"), stream_info.get("port", 80)))
                break
            except Exception:
                lb_info = {}
            finally:
                test.close()

        rtmfp_url = "rtmfp://{0}/{1}".format(
            lb_info.get("server", stream_info.get("server")), stream_info.get("playpath")
        )
        rtmfp_netgroup = stream_info.get("netgroup")
        fallbackurl = "rtmfp://{0}/{1}".format(
            lb_info.get("fallbackServer", stream_info.get("server")),
            stream_info.get("fallbackUrl").replace(" ", ""),
        )

        path = "/stream?{0}".format(
            urlencode({"url": rtmfp_url, "netgroup": rtmfp_netgroup, "fallbackurl": fallbackurl})
        )
        fallback_path = "/stream?{0}".format(urlencode({"url": fallbackurl}))
        return (urljoin(server, path), urljoin(server, fallback_path))

    def get_stream_cast(self, relayer):
        stream_info = json.loads(relayer)
        data = {
            "name": stream_info.get("name"),
            "peer": "true",
            "referer": a2b_hex("6d6f6264726f2e6d65").decode("utf-8"),
            "casting": "true",
            "wifi": "true",
            "token": self.get_token(),
            "playpath": stream_info.get("playpath"),
        }
        for tries in range(10):
            try:
                lb_info = self.api_request("/utils/loadbalancer", data)
            except ValueError:
                lb_info = {}
                break
            except RequestException:
                lb_info = {}
                continue
            try:
                test = socket.socket()
                test.settimeout(5)
                test.connect((lb_info.get("server"), stream_info.get("port", 80)))
                break
            except Exception:
                lb_info = {}
            finally:
                test.close()

        time_stamp = str(int(lb_info.get("epoch", time.time())) + int(lb_info.get("expiration_time", "36000")))
        to_hash = "{password}{time_stamp}/{dir}/{playpath}".format(time_stamp=time_stamp, **lb_info).encode("utf-8")
        out_hash = urlsafe_b64encode(md5(to_hash).digest()).rstrip(b"=").decode("utf-8")

        cast_url = "{0}://{1}:{2}/{3}/{4}/{5}/{6}".format(
            lb_info.get("protocol"),
            lb_info.get("server"),
            lb_info.get("port"),
            lb_info.get("app"),
            out_hash,
            time_stamp,
            lb_info.get("playpath"),
        )

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.0 Safari/537.36 CrKey/1.27.96538",
            "Cookie": lb_info.get("cookie"),
            "Referer": lb_info.get("referer"),
            "X-Requested-With": self.version,
        }

        if lb_info.get("ip"):
            headers["X-Real-IP"] = lb_info.get("ip")

        return (cast_url, headers)
