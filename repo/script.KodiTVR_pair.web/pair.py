import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
		function4,
		function5,
		function6,
		function7,
		function8,
		function9,
		function10,
		function11,
		function12,
		function13
        )
        
    call = dialog.select('[B][COLOR=gold]KodiTVR Select Site To Pair with System[/COLOR][/B]', [
	'[B][COLOR=green]   Servidor OpenLoad[/COLOR][/B]', 
    '[B][COLOR=green]   Servidor The Video Me[/COLOR][/B]',
    '[B][COLOR=green]   Servidor Vid Up Me[/COLOR][/B]',
	'[B][COLOR=green]   Servidor vShare.eu[/COLOR][/B]',
	'[B][COLOR=green]   Servidor Sign For Real Debrid[/COLOR][/B]',
	'[B][COLOR=green]   Servidor Alluc[/COLOR][/B]',
	'[B][COLOR=green]   Servidor Tmdb[/COLOR][/B]',
    '[B][COLOR=green]   Servidor Ororo Tv[/COLOR][/B]',
    '[B][COLOR=green]   Servidor Trakt Tv[/COLOR][/B]',
    '[B][COLOR=green]   Servidor Movieplant.Is[/COLOR][/B]',
    '[B][COLOR=green]   Servidor Stremlord[/COLOR][/B]',
    '[B][COLOR=green]   Servidor Imdb[/COLOR][/B]',
	'[B][COLOR=gold]  Autorize seu dispositivo media center no servidor escolhido.  [/COLOR][/B]',])
#	'[B][COLOR=red]      Follow me on Twitter @KodiTVR[/COLOR][/B]',
#	'[B][COLOR=red]      Add-ons KodiTVR[/COLOR][/B]',
#	'[B][COLOR=red]      Kodi Apps[/COLOR][/B]',
#	'[B][COLOR=red]      Best For Kodi[/COLOR][/B]',
#	'[B][COLOR=red]      KodiTVR Website https://koditvr.wixsite.com/website [/COLOR][/B]',
#	'[B][COLOR=red]      Where To Watch[/COLOR][/B]',
#	'[B][COLOR=silver] **** KodiTVR Help/Support & Updates **** [/COLOR][/B]',
#	'[B][COLOR=green]      KodiTVR Facebook[/COLOR][/B]',])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-13]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

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

myplatform = platform()

def function1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://olpair.com/' ) )
    else:
        opensite = webbrowser . open('https://olpair.com/')

def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://tvad.me/pair' ) )
    else:
        opensite = webbrowser . open('https://tvad.me/pair')
        
def function3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://thevideo.me/pair' ) )
    else:
        opensite = webbrowser . open('https://thevideo.me/pair')
		
def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://vshare.eu/pair' ) )
    else:
        opensite = webbrowser . open('http://vshare.eu/pair')		
		
def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://real-debrid.com' ) )
    else:
        opensite = webbrowser . open('https://real-debrid.com/')
		
def function6():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://accounts.alluc.ee' ) )
    else:
        opensite = webbrowser . open('https://accounts.alluc.ee/')	
				
def function7():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.themoviedb.org/account/signup' ) )
    else:
        opensite = webbrowser . open('https://www.themoviedb.org/account/signup')

def function8():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://ororo.tv/en/users/sign_up' ) )
    else:
        opensite = webbrowser . open('https://ororo.tv/en/users/sign_up')

def function9():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://trakt.tv/join' ) )
    else:
        opensite = webbrowser . open('https://trakt.tv/join')

def function10():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.moviesplanet.tv/register' ) )
    else:
        opensite = webbrowser . open('https://www.moviesplanet.tv/register')

def function11():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://www.streamlord.com/register.html' ) )
    else:
        opensite = webbrowser . open('http://www.streamlord.com/register.html')

def function12():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://m.imdb.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fap-signin-handler&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_mobile_web_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl9tb2JpbGVfd2ViX3VzIiwicmVkaXJlY3RUbyI6Imh0dHA6Ly9tLmltZGIuY29tLz9yZWZfPW1fbG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&tag=imdbtag_reg-20' ) )
    else:
        opensite = webbrowser . open('https://m.imdb.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fap-signin-handler&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_mobile_web_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl9tb2JpbGVfd2ViX3VzIiwicmVkaXJlY3RUbyI6Imh0dHA6Ly9tLmltZGIuY29tLz9yZWZfPW1fbG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&tag=imdbtag_reg-20')		
		
 
def function13(): 0	
	
 
menuoptions()
