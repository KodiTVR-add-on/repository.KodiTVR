# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
# 
# 
# 
#------------------------------------------------------------

###########################################################################################################
#
# - PLUGIN.VIDEO.KodiTVR_desporto -  License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#   Version para Kodi 17, 18 & 19
#   Thanks to ALL
#   Python 3!
#
###########################################################################################################

# -----------------------------------------------------------------------
#  KodiTVR 2021
#   
# -----------------------------------------------------------------------


import os, re
import sys
import plugintools
import xbmc,xbmcaddon,xbmcgui
import six
import base64, marshal

from datetime import datetime

myaddon =xbmcaddon .Addon ()
icon = myaddon.getAddonInfo('icon') 
fanart = myaddon.getAddonInfo('fanart')
  

def run():
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        
        Guia_de_eventos(params)
    else:
        
        action = params.get("action")

        exec (action+"(params)")
    
    plugintools.close_item_list()

def base64dec(string):
    base64_message = string
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return(message) 

try:
    if six.PY2:
        exec(marshal.loads(base64.b64decode('YwAAAAAAAAAAAQAAAEAAAABzDQAAAGQAAIQAAFoAAGQBAFMoAgAAAGMAAAAAAwAAAAUAAABDAAAAc3QAAAB0AABqAQBkAQCDAQB9AABnAAB9AQB4PAB0AgBkAgB0AwB0BABqBQBkAwCDAQBqBgB8AACDAQCDAQCDAgBEXRMAfQIAfAEAagcAfAIAgwEAAXE9AFd0BABqBQBkAwCDAQBqBgB8AACDAQB0CAB8AQCDAQAZUygEAAAATnMdAAAAaHR0cHM6Ly90Lm1lL3MvZGFpbHlzcG9ydGluZm9pAAAAAHMhAAAAaHJlZj0iKGh0dHBzOlwvXC9kYWlseXNwb3J0W14iXSspKAkAAAB0CwAAAHBsdWdpbnRvb2xzdAQAAAByZWFkdAUAAAByYW5nZXQDAAAAbGVudAIAAAByZXQHAAAAY29tcGlsZXQHAAAAZmluZGFsbHQGAAAAYXBwZW5kdAMAAABtYXgoAwAAAHQEAAAAbGwxbHQGAAAAbGwxbGxsdAsAAABsMWwxbGwxbDFsMSgAAAAAKAAAAABzAgAAAGRndBAAAABnZXRfZGFpbHlfZG9tYWluAQAAAHMKAAAAAAEPAQYBLgERAU4oAQAAAFIMAAAAKAAAAAAoAAAAACgAAAAAcwIAAABkZ3QIAAAAPG1vZHVsZT4BAAAAdAAAAAA=')))
    elif six.PY3:
        exec(marshal.loads(base64.b64decode(b'4wAAAAAAAAAAAAAAAAAAAAACAAAAQAAAAHMMAAAAZABkAYQAWgBkAlMAKQNjAAAAAAAAAAAAAAAAAwAAAAYAAABDAAAAc1AAAAB0AKABZAGhAX0AZwB9AXQCZAJ0A3QEoAVkA6EBoAZ8AKEBgwGDAkQAXQ59AnwBoAd8AqEBAQBxKHQEoAVkA6EBoAZ8AKEBdAh8AYMBGQBTACkETnodaHR0cHM6Ly90Lm1lL3MvZGFpbHlzcG9ydGluZm/pAAAAAHohaHJlZj0iKGh0dHBzOlwvXC9kYWlseXNwb3J0W14iXSspKQlaC3BsdWdpbnRvb2xz2gRyZWFk2gVyYW5nZdoDbGVu2gJyZdoHY29tcGlsZdoHZmluZGFsbNoGYXBwZW5k2gNtYXgpA1oEbGwxbFoGbGwxbGxsWgtsMWwxbGwxbDFsMakAcgoAAADaAmRn2hBnZXRfZGFpbHlfZG9tYWluAQAAAHMKAAAAAAEKAQQBHgEMAXIMAAAATikBcgwAAAByCgAAAHIKAAAAcgoAAAByCwAAANoIPG1vZHVsZT4BAAAA8wAAAAA=')))    
except:

    raise ValueError("Unable to connect DailySport domain")

def Guia_de_eventos(params):
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    url = "https://dailysport.%s" % extension# + "/"
    url = plugintools.read_body_and_headers(url)[0]
    matches = re.findall(r'(?s)<td><b>([^<]+)<\/b>|<td>(\d+[^<]+)<\/td>\s*<td>([^<]+)<\/td>\s*|<td><a href="([^"]+)">([^<]+)', url, re.DOTALL)
    for data, evento, partida, url, canal in matches:
        status = ''
        if evento:
            if evento == 'LaLiga':
                thumbnail = 'https://i.imgur.com/itD6weP.jpg'
            if evento == 'FA Cup':
                thumbnail = 'https://i.imgur.com/XdJ6Ray.jpg'
            if evento == 'Premier League':
                thumbnail = 'https://i.imgur.com/ocRwlDK.png'
            if evento == 'LaLiga SmartBank':
                thumbnail = 'https://i.imgur.com/HTAtMiF.png'
            if evento == 'Serie A':
                thumbnail = 'https://i.imgur.com/JL4GzJz.png'
            if evento == 'Endesa':
                thumbnail = 'https://i.imgur.com/9wI6Irv.jpg'
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            for x in (re.compile(r'\d+\/\d+ - (\d+:\d+)').findall(evento)):
                if current_time < x: status = "KodiTVR | [COLORred]* [No Activo]  [/COLOR]"
                else: status = "KodiTVR | [COLORgreen]* [Activo]  [/COLOR]"

        if partida: partida = "[COLORyellow] {} [/COLOR]".format(partida)
        if canal: canal = "[COLORred] {} [/COLOR]".format(canal.replace('Channel','Canal:').replace('Portuguese','Portuguese').replace('English','Ingles').replace('Latin','Latino').replace('Portuguese (Low quality)','Portuguese (SD)'))
        plugintools.add_item(action = "play", title =  data + "{}[COLORsilver]{}[/COLOR] {} {}".format(status, evento, partida, canal), url = url, thumbnail = icon, fanart = fanart, folder = False, isPlayable = True)  

def play(params):
    finalurl = ''
    url = "https://dailysport.%s" % extension + "/" + params.get("url")
    url = plugintools.read(url)  
    finalurl = plugintools.find_single_match(url, r'(?s)loader: engine.createLoaderClass.*?}\);.*?source:.*?window.atob.*?"(.+?)"')
    if finalurl: 
        realfinalurl = base64dec(finalurl)
        plugintools.play_resolved_url(realfinalurl)
if __name__ == "__main__":
    domain = get_daily_domain().split(".")[1]
    extension = domain
    xbmcaddon.Addon().setSetting('extension', domain)
    run()