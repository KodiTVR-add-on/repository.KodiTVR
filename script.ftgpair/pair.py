###################################################################################
#(_)                                                                              #
# |________________________________________________                               #
# |*  *  *  *  *  *  * |##########################|                               #
# | *  *  *  *  *  *  *|==========================|                               #
# |*  *  *  *  *  *  * |##########################|                               #
# | *  *  *  *  *  *  *|==========================|                               #
# |*  *  *  *  *  *  * |##########################|      If your going to copy    #
# | *  *  *  *  *  *  *|==========================|         this addon just       #
# |*  *  *  *  *  *  * |##########################|         give credit!!!!       #
# |--------------------|==========================|                               #
# |###############################################|                               #
# |===============================================|                               #
# |###############################################|                               #
# |===============================================|                               #
# |###############################################|                               #
# |-----------------------------------------------|                               #
# |                                                                               #
# |    Pairing Add-on                                                             #
# |    Copyright (C) 2017 FTG                                                     #
# |                                                                               #
# |    This program is free software: you can redistribute it and/or modify       #
# |    it under the terms of the GNU General Public License as published by       #
# |    the Free Software Foundation, either version 3 of the License, or          #
# |    (at your option) any later version.                                        #
# |                                                                               #
# |    This program is distributed in the hope that it will be useful,            #
# |    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
# |    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
# |    GNU General Public License for more details.                               #
# |                                                                               #
###################################################################################

import urllib,urllib2,webbrowser,sys,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

def menu():
	dialog = xbmcgui.Dialog()
	items = [
			('[COLOR yellow]OpenLoad[/COLOR] -- https://olpair.com/', 'openload' ),
			('[COLOR yellow]The Video Me[/COLOR] -- https://tvad.me/pair', 'videome' ),
			('[COLOR yellow]vShare.eu[/COLOR] -- http://vshare.eu/pair', 'vshareeu' ),
			('[COLOR yellow]Vid Up Me[/COLOR] -- https://thevideo.me/pair', 'vidupme' ),
			('[COLOR yellow]Flash X[/COLOR] -- https://flashx.tv/pair - Login', 'flashx' )
			]
	select = selectDialog([i[0] for i in items], 'Select Site To Pair with')
	if select == -1: return
	items =  items[select][1]
	site(items)
	return

def site(items):
	if items == 'openload':
		site = 'https://olpair.com/'
		opensite(site)
	if items == 'videome':
		site = 'https://tvad.me/pair'
		opensite(site)
	if items == 'vidupme':
		site = 'https://thevideo.me/pair'
		opensite(site)
	if items == 'vshareeu':
		site = 'http://vshare.eu/pair'
		opensite(site)
	if items == 'flashx':
		site = 'https://flashx.tv/pair'
		opensite(site)

def opensite(site):
	os = platform()
	if os == 'android':
		xbmc.executebuiltin('StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
	if os == 'osx':
		os.system("open -a /Applications/Safari.app %s") % (site)
	else:
		webbrowser.open(site)

def platform():
	if xbmc.getCondVisibility('system.platform.android'):
		return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):
		return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'):
		return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):
		return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):
		return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):
		return 'ios'

def idle():
	return xbmc.executebuiltin('Dialog.Close(busydialog)')
addonInfo = xbmcaddon.Addon().getAddonInfo

def selectDialog(list, heading=addonInfo('name')):
	dialog = xbmcgui.Dialog()
	return dialog.select(heading, list)
menu()