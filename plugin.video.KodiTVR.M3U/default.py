# -*- coding: utf-8 -*-

"""
Copyright (C) 2021
KodiTVR ADD-ON
"""

import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon,base64,base64sf

plugin_handle = int(sys.argv[1])

mysettings = xbmcaddon.Addon(id = 'plugin.video.KodiTVR.M3U')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))

fan_al = xbmc.translatePath(os.path.join(home, 'al.png'))
fan_at = xbmc.translatePath(os.path.join(home, 'at.png'))
fan_be = xbmc.translatePath(os.path.join(home, 'be.png'))
fan_cz = xbmc.translatePath(os.path.join(home, 'cz.png'))
fan_de = xbmc.translatePath(os.path.join(home, 'de.png'))
fan_dk = xbmc.translatePath(os.path.join(home, 'dk.png'))
fan_fi = xbmc.translatePath(os.path.join(home, 'fi.png'))
fan_fr = xbmc.translatePath(os.path.join(home, 'fr.png'))
fan_gr = xbmc.translatePath(os.path.join(home, 'gr.png'))
fan_hu = xbmc.translatePath(os.path.join(home, 'hu.png'))
fan_it = xbmc.translatePath(os.path.join(home, 'it.png'))
fan_nl = xbmc.translatePath(os.path.join(home, 'nl.png'))
fan_no = xbmc.translatePath(os.path.join(home, 'no.png'))
fan_pl = xbmc.translatePath(os.path.join(home, 'pl.png'))
fan_pt = xbmc.translatePath(os.path.join(home, 'pt.png'))
fan_sk = xbmc.translatePath(os.path.join(home, 'sk.png'))
fan_es = xbmc.translatePath(os.path.join(home, 'es.png'))
fan_se = xbmc.translatePath(os.path.join(home, 'se.png'))
fan_tr = xbmc.translatePath(os.path.join(home, 'tr.png'))
fan_uk = xbmc.translatePath(os.path.join(home, 'uk.png'))



icon_al = xbmc.translatePath(os.path.join(home, 'albania.png'))
icon_at = xbmc.translatePath(os.path.join(home, 'austria.png'))
icon_be = xbmc.translatePath(os.path.join(home, 'belgium.png'))
icon_cz = xbmc.translatePath(os.path.join(home, 'czech.png'))
icon_de = xbmc.translatePath(os.path.join(home, 'germany.png'))
icon_dk = xbmc.translatePath(os.path.join(home, 'denmark.png'))
icon_fi = xbmc.translatePath(os.path.join(home, 'finland.png'))
icon_fr = xbmc.translatePath(os.path.join(home, 'france.png'))
icon_gr = xbmc.translatePath(os.path.join(home, 'greece.png'))
icon_hu = xbmc.translatePath(os.path.join(home, 'hungary.png'))
icon_it = xbmc.translatePath(os.path.join(home, 'italy.png'))
icon_nl = xbmc.translatePath(os.path.join(home, 'netherlands.png'))
icon_no = xbmc.translatePath(os.path.join(home, 'norway.png'))
icon_pl = xbmc.translatePath(os.path.join(home, 'poland.png'))
icon_pt = xbmc.translatePath(os.path.join(home, 'portugal.png'))
icon_sk = xbmc.translatePath(os.path.join(home, 'slovakia.png'))
icon_es = xbmc.translatePath(os.path.join(home, 'spain.png'))
icon_se = xbmc.translatePath(os.path.join(home, 'sweden.png'))
icon_tr = xbmc.translatePath(os.path.join(home, 'turkey.png'))
icon_uk = xbmc.translatePath(os.path.join(home, 'unitedkingdom.png'))



## Fuck you GRUPETA FN

albania_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/al.m3u"
austria_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/at.m3u"
belgium_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/be.m3u"
czech_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/cz.m3u"
germany_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/de.m3u"
denmark_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/dk.m3u"
finland_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/fi.m3u"
france_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/fr.m3u"
greece_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/gr.m3u"
hungary_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/hu.m3u"
italy_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/it.m3u"
netherlands_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/nl.m3u"
norvay_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/no.m3u"
poland_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/pl.m3u"
portugal_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/pt.m3u"
slovakia_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/sk.m3u"
spain_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/es.m3u"
sweden_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/se.m3u"
turkey_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/tr.m3u"
unitedkingdom_m3u ="https://raw.githubusercontent.com/KodiTVR-add-on/iptv/main/channels/uk.m3u"

xml_regex = '#(.+?),(.+)\s*(.+)\s*'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'

u_tube = 'http://www.youtube.com'

def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
					
def read_file(file):
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
			
def main():
	if len(albania_m3u) > 0:	
		add_dir('[COLOR white][B]ALBANIA[/B][/COLOR]', u_tube, 2, icon_al, fan_al)
	if len(austria_m3u) > 0:	
		add_dir('[COLOR white][B]AUSTRIA[/B][/COLOR]', u_tube, 3, icon_at, fan_at)
	if len(belgium_m3u) > 0:	
		add_dir('[COLOR white][B]BELGIUM[/B][/COLOR]', u_tube, 4, icon_be, fan_be)   	
	if len(czech_m3u) > 0:	
		add_dir('[COLOR white][B]CZECH REPUBLIC[/B][/COLOR]', u_tube, 5, icon_cz, fan_cz)
	if len(germany_m3u) > 0:	
		add_dir('[COLOR white][B]GERMANY[/B][/COLOR]', u_tube, 6, icon_de, fan_de)
	if len(denmark_m3u) > 0:	
		add_dir('[COLOR white][B]DENMARK[/B][/COLOR]', u_tube, 7, icon_dk, fan_dk)
	if len(finland_m3u) > 0:	
		add_dir('[COLOR white][B]FINLAND[/B][/COLOR]', u_tube, 8, icon_fi, fan_fi)
	if len(france_m3u) > 0:	
		add_dir('[COLOR white][B]FRANCE[/B][/COLOR]', u_tube, 9, icon_fr, fan_fr)   
	if len(greece_m3u) > 0:	
		add_dir('[COLOR white][B]GREECE[/B][/COLOR]', u_tube, 10, icon_gr, fan_gr)    
	if len(hungary_m3u) > 0:	
		add_dir('[COLOR white][B]HUNGARY[/B][/COLOR]', u_tube, 11, icon_hu, fan_hu)    
	if len(italy_m3u) > 0:	
		add_dir('[COLOR white][B]ITALY[/B][/COLOR]', u_tube, 12, icon_it, fan_it)    
	if len(netherlands_m3u) > 0:	
		add_dir('[COLOR white][B]NETHERLANDS[/B][/COLOR]', u_tube, 13, icon_nl, fan_nl)    
	if len(norvay_m3u) > 0:	
		add_dir('[COLOR white][B]NORWAY[/B][/COLOR]', u_tube, 14, icon_no, fan_no)     
	if len(poland_m3u) > 0:	
		add_dir('[COLOR white][B]POLAND[/B][/COLOR]', u_tube, 15, icon_pl, fan_pl)        
	if len(portugal_m3u) > 0:	
		add_dir('[COLOR white][B]PORTUGAL[/B][/COLOR]', u_tube, 16, icon_pt, fan_pt)    
	if len(slovakia_m3u) > 0:	
		add_dir('[COLOR white][B]SLOVAKIA[/B][/COLOR]', u_tube, 17, icon_sk, fan_sk)    
	if len(spain_m3u) > 0:	
		add_dir('[COLOR white][B]SPAIN[/B][/COLOR]', u_tube, 18, icon_es, fan_es)
	if len(sweden_m3u) > 0:	
		add_dir('[COLOR white][B]SWEDEN[/B][/COLOR]', u_tube, 19, icon_se, fan_se)
	if len(turkey_m3u) > 0:	
		add_dir('[COLOR white][B]TURKEY[/B][/COLOR]', u_tube, 20, icon_tr, fan_tr)       
	if len(unitedkingdom_m3u) > 0:	
		add_dir('[COLOR white][B]UNITED KINGDOM[/B][/COLOR]', u_tube, 21, icon_uk, fan_uk)
        
        
def m3u_albania():		
	content = make_request(albania_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
			
def m3u_austria():			
	content = make_request(austria_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_belgium():		
	content = make_request(belgium_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_czech():			
	content = make_request(czech_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
             
def m3u_germany():			
	content = make_request(germany_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass  
			
def m3u_denmark():
	content = make_request(denmark_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_finland():
	content = make_request(finland_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_france():
	content = make_request(france_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_greece():
	content = make_request(greece_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass             
            
def m3u_hungary():
	content = make_request(hungary_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass 
            
def m3u_italy():
	content = make_request(italy_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass 
            
def m3u_netherlands():
	content = make_request(netherlands_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
			
def m3u_norway():
	content = make_request(norway_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_poland():
	content = make_request(poland_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_portugal():
	content = make_request(portugal_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
def m3u_slovakia():
	content = make_request(slovakia_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass  

def m3u_spain():
	content = make_request(spain_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass             
            
def m3u_sweden():
	content = make_request(portugal_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass 
            
def m3u_turkey():
	content = make_request(turkey_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass 
            
def m3u_unitedkingdom():
	content = make_request(unitedkingdom_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:	
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
            
   
           

			


            
				
def m3u_playlist(name, url, thumb):	
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')			
			add_dir(name, url, '', thumb, thumb)			
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			add_link(name, url, 1, thumb, thumb)			
		else:				
			add_link(name, url, 1, icon, fanart)	
					
def play_video(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def add_dir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  
		
params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass  

#print "Mode: " + str(mode)
#print "URL: " + str(url)
#print "Name: " + str(name)
#print "iconimage: " + str(iconimage)		

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	play_video(url)

elif mode == 2:
	m3u_albania()
	
elif mode == 3:
	m3u_austria()
    
elif mode == 4:
	m3u_belgium()
    
elif mode == 5:
	m3u_czech()
    
elif mode == 6:
	m3u_germany()
    
elif mode == 7:
	m3u_denmark()
    
elif mode == 8:
	m3u_finland()
    
elif mode == 9:
	m3u_france()

elif mode == 10:
	m3u_greece()

elif mode == 11:
	m3u_hungary()

elif mode == 12:
	m3u_italy()
	
elif mode == 13:
	m3u_netherlands()
    
elif mode == 14:
	m3u_norway()
	
elif mode == 15:
	m3u_poland()
    
elif mode == 16:
	m3u_portugal()
    
elif mode == 17:
	m3u_slovakia()
    
elif mode == 18:
	m3u_spain()
    
elif mode == 19:
	m3u_sweden()

elif mode == 20:
	m3u_turkey()

elif mode == 21:
	m3u_unitedkingdom()
    
xbmcplugin.endOfDirectory(plugin_handle)