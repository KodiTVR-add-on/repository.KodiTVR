# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2020 - KodiTVR BOLA TV
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.KodiTVR_BOLA'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("KodiTVR BOLA TV", "playlist/PLLIGi5hjtUnNFyQyDyrzl6Wy4z05GvJtB", 'https://i.imgur.com/5m5QFDM.png'),
        ("Legasus", "channel/UCvYTbKjy-e7Ky3LgPYn6fLA", 'https://yt3.ggpht.com/ytc/AAUvwnibG6lp7emsqkZF6Es-J_js1w948bqA_ZFTIWaeXg=s88-c-k-c0x00ffffff-no-rj'),
        ("Daily Dose Of Football", "channel/UCU-ZyUKT3qiLzPuod6-pa-Q", 'https://yt3.ggpht.com/ytc/AAUvwnhOmUtZuPfPJsaK3AKnSCQ7j5WF3R6Fkb3TMZON=s88-c-k-c0x00ffffff-no-rj'),
		("SBFootball", "channel/UCx9gQwpsX0XNVXD6EF-xHTw", 'https://yt3.ggpht.com/ytc/AAUvwnjkNMDbLSetCJ3UQ4gEe1jO-hBvI2yemic03VI7kg=s88-c-k-c0x00ffffff-no-rj'),
        ("Esportudo", "channel/UCww-wBF9lE68jfcVvlYb31A", 'https://yt3.ggpht.com/ytc/AAUvwnhSTPDf-3MouL_--1F7_2qgjlZu0AnGxW0mYFQhmg=s88-c-k-c0x00ffffff-no-rj'),
		("TopPassion", "user/TopHDPassion", 'https://yt3.ggpht.com/ytc/AAUvwniWTcvzZ0CZCij7VcVDVYKwr8nnOs-DjeT64NR90A=s88-c-k-c0x00ffffff-no-rj'),
		("FUTUBER 26", "channel/UCQMvoaftIlXh-zrSrOEQTYA", 'https://yt3.ggpht.com/ytc/AAUvwnjzAw6g8FT3XclvDaB1Yk0nDmN7YzFnVGAAJ6Raog=s88-c-k-c0x00ffffff-no-rj'),
		("Football Memories", "channel/UCmronZpCU8sUFqZuYk82eDw", 'https://yt3.ggpht.com/ytc/AAUvwnidnpvGTWTrZX0u6PWVD_pmb1_ToyFAJWGZvt9_0A=s88-c-k-c0x00ffffff-no-rj'),
		("FootballNerd", "channel/UCCeBXYN2sBPmihr7U7jHiRg", 'https://yt3.ggpht.com/ytc/AAUvwnii6MMnTh3Bcy3inJjkU-gwW7hZsMT1kC4lRZzY=s88-c-k-c0x00ffffff-no-rj'),
		("Sports 360", "channel/UC8MXV8Y2LWMJIjrvRpr_wjg", 'https://yt3.ggpht.com/ytc/AAUvwnhAJSjLx2lBGVqzYoX_WFPid8NuqRt7mDTncksc=s88-c-k-c0x00ffffff-no-rj'),	    				
		("Nonstop Football", "channel/UCURd3HGqSfVpkzY2VG0gPZg", 'https://yt3.ggpht.com/ytc/AAUvwnhaeNSrjfUifdBaF4xRV0zzie8wQ60Uc_7mIFkk=s88-c-k-c0x00ffffff-no-rj'),	    				
]



# Entry point
def run():
    plugintools.log("youtubeAddon.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("youtubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()