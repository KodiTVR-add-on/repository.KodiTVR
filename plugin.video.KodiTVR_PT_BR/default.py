# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys,urllib

addon = xbmcaddon.Addon()
xbmcplugin.setContent(int(sys.argv[1]), 'movies')
addon_path = addon.getAddonInfo('path').decode('utf-8')

def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+'?url='+str(url)+'&mode='+str(mode)+'&name='+str(name)+'&Image='+str(iconimage)
    liz=xbmcgui.ListItem(name, iconImage=os.path.join(addon_path,'folder.png'), thumbnailImage=iconimage)
    liz.setInfo( type='Video', infoLabels={ 'Title': name } )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=1)

def add_item(url, infolabels, img):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, listitem)

def item_data_loader(my_data):
    if os.path.exists(os.path.join(addon_path,'resources','data',my_data)):
        stream_name = 'dailymotion.com/video/'
        stream_url = 'play_url = plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s'

        f = open(os.path.join(addon_path,'resources','data',my_data),'r')
        for line in f.readlines():
            line = line.strip()

            if line.startswith('#EXTINF:'):
                stream_name = line.split(',')[1]
            elif line.startswith('http:') or line.startswith('https:') or line.startswith('rtmp:') or line.startswith('mms:') or line.startswith('rtsp:'):
                stream_url = line

                if not stream_name == '' and not stream_url == '':
                    add_item(stream_url,{ 'title': stream_name}, os.path.join(addon_path,'resources','img','play.png'))

                else:
                    
                    stream_name = 'youtube'
                    stream_url = 'play_url = plugin://plugin.video.youtube/?action=play_video&videoid=%s'

if not sys.argv[2] == '' and 'url=' in sys.argv[2]:
    item_data_loader(urllib.unquote(sys.argv[2].split('url=')[1]).decode('utf8'))
else:
    addDir('[COLOR red]PORTUGUESE[/COLOR] [COLOR white]TV[/COLOR]','tv.txt', 1, os.path.join(addon_path,'resources','img','tv.png'))
    addDir('[COLOR red]PORTUGUESE[/COLOR] [COLOR white]RADIO[/COLOR]','radio.txt', 1, os.path.join(addon_path,'resources','img','radio.png'))
    addDir('[COLOR yellow]BRAZILIAN[/COLOR] [COLOR red]RADIO[/COLOR]','brradio.txt', 1, os.path.join(addon_path,'resources','img','brradio.png'))
    addDir('[COLOR yellow]BRAZILIAN[/COLOR] [COLOR red]TV[/COLOR]','brtv.txt', 1, os.path.join(addon_path,'resources','img','brtv.png'))
xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)