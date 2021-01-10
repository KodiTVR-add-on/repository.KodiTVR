# -*- coding: utf-8 -*-
# --[ Streamlive v1.0 ]--|--[ From KodiTVR-add-on ]--
# IPTV Indexer made just for the one site as of now.

import re, os, sys, urllib
from resources.lib.modules import client
from resources.lib.modules import control


class streamlive:
    def __init__(self):
        self.list = []
        self.base_link = 'https://www.streamlive.to/%s'
        self.headers = {'User-Agent': client.agent()}

    def root(self):
        channels = [
            ('A&E', 'view/76672/A&E-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('ABC', 'view/68969/ABC-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('ABC HD', 'view/46476/ABC-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('AMC', 'view/76666/AMC-(SD)', 'https://github.com/KodiTVR-add-on/IPTV_Logos/blob/master/misc/IPTV%201.png?raw=true'),
            ('Animal Planet', 'view/76673/Animal-Planet-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Big Ten Network BTN HD', 'view/76730/Big-Ten-Network-BTN-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Cartoon Network', 'view/76674/Cartoon-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('CNN', 'view/68967/CNN-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Disney HD', 'view/38804/Disney-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Disney', 'view/76679/Disney-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('ESPN HD', 'view/57977/ESPN-2-(HD)', 'https://github.com/KodiTVR-add-on/IPTV_Logos/blob/master/misc/IPTV%201.png?raw=true'),
            ('ESPN 2', 'view/69028/ESPN-2-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('ESPN Deportes HD', 'view/76738/ESPN-Deportes-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('ESPN U HD', 'view/76663/ESPN-U-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Food Network', 'view/69023/Food-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Food Network NY HD', 'view/77023/Fox-Network-NY-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Fox News', 'view/68968/Fox-News-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Fox Network HD', 'view/56002/Fox-Network-(HD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Fox Movie Channel', 'view/38449/Fox-Movie-Channel', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Fox Sports 2', 'view/76681/Fox-Sports-2-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Fox Business', 'view/76680/Fox-Business-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('FXM', 'view/79283/FXM', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Hallmark', 'view/76683/Hallmark-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('HBO', 'view/69021/HBO-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('NBC Sport Network', 'view/71137/NBC-Sport-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('MLB Network', 'view/76688/MLB-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('MTV - Music Television SD', 'view/69037/MTV---Music-Television-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Nickelodeon HD', 'view/71112/Nickelodeon-(HD)', 'https://github.com/KodiTVR-add-on/IPTV_Logos/blob/master/misc/IPTV%201.png?raw=true'),
            ('Nickelodeon', 'view/76702/Nickelodeon-(SD)', 'https://github.com/KodiTVR-add-on/IPTV_Logos/blob/master/misc/IPTV%201.png?raw=true'),
            ('NFL Network', 'vview/72886/NFL-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('MSNBC', 'view/76689/MSNBC-(SD)', 'https://github.com/KodiTVR-add-on/IPTV_Logos/blob/master/misc/IPTV%201.png?raw=true'),
            ('OWN - Oprah Winfrey Network', 'view/76670/OWN-Oprah-Winfrey-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Science', 'view/76693/Science-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Showtime', 'view/69036/Showtime-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Starz', 'view/76705/StarZ-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('TNT', 'view/69020/TNT-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('Travel channel', 'view/69019/Travel-chanel-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('TruTV', 'view/73009/TruTV-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('USA Network', 'view/73018/USA-Network-(SD)', 'https://raw.githubusercontent.com/KodiTVR-add-on/IPTV_Logos/master/misc/IPTV%201.png'),
            ('VH1', 'view/76699/VH1-(SD)', 'https://github.com/KodiTVR-add-on/IPTV_Logos/blob/master/misc/IPTV%201.png?raw=true'),
        ]
        for channel in channels:
            self.list.append({'name': channel[0], 'url': self.base_link % channel[1], 'image': channel[2], 'action': 'streamlivePlay'})
        self.addDirectory(self.list)
        return self.list

    def play(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            result = re.compile("return([[\a-zA-Z]+]).join").findall(stream)
            for result in result:
                result = result.strip('([]').replace('\/', '/').replace(',', '').replace('"', '')
                result = 'https:' + result
                link = result + self.code(url) + self.code2(url)
                link = '%s|Referer=%s' % (link, url)
                control.execute('PlayMedia(%s)' % link)
        except Exception:
            return

    def code(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            result2 = re.compile("\+ (.+?).join").findall(stream)[0]
            result3 = re.findall("var (.+?) = \[(.+?)\];", stream)
            for link, code in result3:
                if result2 in link:
                    code = code.replace(',','').replace('"', '')
                    return code
        except:
            return

    def code2(self, url):
        try:
            stream = client.request(url, headers=self.headers)
            result4 = re.compile("id=(.+?)>(.+?)</span").findall(stream)
            result5 = re.findall('\+ document.getElementById(.+?).innerHTML', stream)[0]
            result5 = result5.strip('("")')
            for link, code2 in result4:
                if 'success' in link: continue
                if result5 in link:
                    return code2
        except:
            return

    def addDirectory(self, items, queue=False, isFolder=True):
        if items is None or len(items) is 0:
            control.idle()
            sys.exit()
        sysaddon = sys.argv[0]
        syshandle = int(sys.argv[1])
        addonFanart, addonThumb, artPath = control.addonFanart(), control.addonThumb(), control.artPath()
        for i in items:
            try:
                name = i['name']
                if i['image'].startswith('http'):
                    thumb = i['image']
                elif artPath is not None:
                    thumb = os.path.join(artPath, i['image'])
                else:
                    thumb = addonThumb
                item = control.item(label=name)
                if isFolder:
                    url = '%s?action=%s' % (sysaddon, i['action'])
                    try:
                        url += '&url=%s' % urllib.quote_plus(i['url'])
                    except Exception:
                        pass
                    item.setProperty('IsPlayable', 'false')
                else:
                    url = '%s?action=%s' % (sysaddon, i['action'])
                    try:
                        url += '&url=%s' % i['url']
                    except Exception:
                        pass
                    item.setProperty('IsPlayable', 'true')
                    item.setInfo("mediatype", "video")
                    item.setInfo("audio", '')
                item.setArt({'icon': thumb, 'thumb': thumb})
                if addonFanart is not None:
                    item.setProperty('Fanart_Image', addonFanart)
                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)
            except Exception:
                pass
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
