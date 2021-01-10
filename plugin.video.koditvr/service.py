# -*- coding: utf-8 -*-

from resources.lib.modules import log_utils
from resources.lib.modules import control

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    AddonVersion = control.addon('plugin.video.koditvr').getAddonInfo('version')
    RepoVersion = control.addon('repository.KodiTVR').getAddonInfo('version')

    log_utils.log(' KODITVR PLUGIN VERSION: %s ' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log(' KODITVR REPOSITORY VERSION: %s ' % str(RepoVersion), log_utils.LOGNOTICE)
except:
    log_utils.log('CURRENT KODITVR VERSIONS REPORT ', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING KODITVR VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL KODITVR INSTALL. ', log_utils.LOGNOTICE)

