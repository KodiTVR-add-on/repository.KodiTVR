import xbmc
import urllib
import urllib2

def mensagem():
    MSG2 = "https://raw.githubusercontent.com/KodiTVR-add-on/KodiTVR-ADULT-XXL/master/alarme.txt"				
    MSG = MSG2
    __ADDONNAME__ = "KodiTVR-iptv"
    addon = xbmcaddon.Addon('plugin.video.KodiTVR-ADULT-XXL')
    home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
    icon = os.path.join(home, 'icon.png')
    LINE1 = urllib2.urlopen(MSG).read()
    TIME = 15000 #IN MILISECONDS
    xbmc.executebuiltin('NOTIFICATION(%S, %S, %D, %S)'%(__ADDONNAME__,LINE1, TIME, __ICON__))
