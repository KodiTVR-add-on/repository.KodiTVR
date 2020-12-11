# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Brasileirão TV by KodiTVR
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: KodiTVR
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.KodiTVR_Brasileirao'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "Brasileirão Série A"
YOUTUBE_CHANNEL_ID_2 = "flamengo"
YOUTUBE_CHANNEL_ID_3 = "santostvoficial"
YOUTUBE_CHANNEL_ID_4 = "UCP33_u-7GF2erCCiMuQlC3g"
YOUTUBE_CHANNEL_ID_5 = "palmeirascombr"
YOUTUBE_CHANNEL_ID_6 = "BOTAFOGOFRoficial"
YOUTUBE_CHANNEL_ID_7 = "Fludigital"
YOUTUBE_CHANNEL_ID_8 = "vasco"
YOUTUBE_CHANNEL_ID_9 = "GREMIOTVERADIO"
YOUTUBE_CHANNEL_ID_10 = "saopaulofctv"
YOUTUBE_CHANNEL_ID_11 = "corinthiansoficial"
YOUTUBE_CHANNEL_ID_12 = "TvBahea"
YOUTUBE_CHANNEL_ID_13 = "assessoriainter"
YOUTUBE_CHANNEL_ID_14 = "tvsportrecife"
YOUTUBE_CHANNEL_ID_15 = "tvatleticopr"
YOUTUBE_CHANNEL_ID_16 = "tvgaloweb"
YOUTUBE_CHANNEL_ID_17 = "UCHtqrolH5tlrj4vB97kF-AA"
YOUTUBE_CHANNEL_ID_18 = "TVGoiasoficial"
YOUTUBE_CHANNEL_ID_19 = "vozaotv"
YOUTUBE_CHANNEL_ID_20 = "siteoficialfortaleza"
YOUTUBE_CHANNEL_ID_21 = "coritibaoficial"
YOUTUBE_CHANNEL_ID_22 = "Brasileirão Série B"
YOUTUBE_CHANNEL_ID_23 = "OficialCruzeiro"
YOUTUBE_CHANNEL_ID_24 = "ACFChapecoense"
YOUTUBE_CHANNEL_ID_25 = "americadecacampeao"
YOUTUBE_CHANNEL_ID_26 = "sampaiomania"
YOUTUBE_CHANNEL_ID_27 = "UCnvMjCptspOne0ztN7z-KHg"
YOUTUBE_CHANNEL_ID_28 = "UCrY4s3Eq7zSa5SE1LjoW_xg"
YOUTUBE_CHANNEL_ID_29 = "UCeHwAWfEdPiqe-fpxilx2NQ"
YOUTUBE_CHANNEL_ID_30 = "UCGCLl9d9aJA1GFPfMqhDa0w"
YOUTUBE_CHANNEL_ID_31 = "tvponte"
YOUTUBE_CHANNEL_ID_32 = "UCN2KzyGQ7Zrg2cHb_kTCoqg"
YOUTUBE_CHANNEL_ID_33 = "AvaiOficial"
YOUTUBE_CHANNEL_ID_34 = "UCxWEfjeAzBzoW5idREGLDFQ"
YOUTUBE_CHANNEL_ID_35 = "UCdkvLmZHJySBCj26_Q--1XA"
YOUTUBE_CHANNEL_ID_36 = "redeleaooficial"
YOUTUBE_CHANNEL_ID_37 = "UCY5G5pM9oJwAsBMBnfJKWxg"
YOUTUBE_CHANNEL_ID_38 = "figueirensefutebol"
YOUTUBE_CHANNEL_ID_39 = "UCjVRdz4KO2F18d9K1gTdD9g"
YOUTUBE_CHANNEL_ID_40 = "TVBotafogoOficial"
YOUTUBE_CHANNEL_ID_41 = "UCE7T-Ns_XNdyk3OFQrt9hqw"
YOUTUBE_CHANNEL_ID_42 = "UCmWlRgypRQbPkp8bE1el9oQ"
YOUTUBE_CHANNEL_ID_43 = "Brasileirão Série C"
YOUTUBE_CHANNEL_ID_44 = "UCrNM81bcQPt1yhzRsqJsyyA"
YOUTUBE_CHANNEL_ID_45 = "UCsLGx5V5iv-JHbG10oDZOcw"
YOUTUBE_CHANNEL_ID_46 = "vilanovafcoficial"
YOUTUBE_CHANNEL_ID_47 = "papaotv"
YOUTUBE_CHANNEL_ID_48 = "UCNjYPqi1uceoV1h2POiXAJQ"
YOUTUBE_CHANNEL_ID_49 = "UC7cEcIwIZrF3f_SDIlCdv4w"
YOUTUBE_CHANNEL_ID_50 = "ferroviarioaclube"
YOUTUBE_CHANNEL_ID_51 = "UCeImPJKqNPGHtT9x4mH5Stw"
YOUTUBE_CHANNEL_ID_52 = "UChFwpEBAY4Dy49LS7ixFf5g"
YOUTUBE_CHANNEL_ID_53 = "UCRlUskL6UxiGE6z8aqcFHNQ"
YOUTUBE_CHANNEL_ID_54 = "UChzZFnmaj3OjHT5Lq25SOAA"
YOUTUBE_CHANNEL_ID_55 = "UCga4i1NKw7B6aDyPjIu-5qw"
YOUTUBE_CHANNEL_ID_56 = "UC05gx_9c-OoH575hsNNrjvQ"
YOUTUBE_CHANNEL_ID_57 = "UCpRrPE0jMZUDk435OEcshHQ"
YOUTUBE_CHANNEL_ID_58 = "UCrKt2Un8wp3lVNSA4pdc0Ew"
YOUTUBE_CHANNEL_ID_59 = "UCma5VSL6N4CQielSrnOcuEw"
YOUTUBE_CHANNEL_ID_60 = "UC1X38rEQ1qTDJ5J2851YZEQ"
YOUTUBE_CHANNEL_ID_61 = "imprensacriciuma"
YOUTUBE_CHANNEL_ID_62 = "UCiBJpmIt63S1tPb3MpO11sA"
YOUTUBE_CHANNEL_ID_63 = "UCRpuxdZGkUpiqPfsrqe1xoQ"
YOUTUBE_CHANNEL_ID_64 = "UCU6JLYuerEUb7VrDd4zLihg"
YOUTUBE_CHANNEL_ID_65 = "ogbvideos"
YOUTUBE_CHANNEL_ID_66 = "MsTeoCRi"
YOUTUBE_CHANNEL_ID_67 = "UCl2sD-nfbfx1CncbBD2JLKg"


# Entry point
def run():
    plugintools.log("docu.run")
    
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
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item(
        #action="", 
        title="[COLORlime]---●★| ⚽️ KodiTVR *Brasileirão Série A* Channels ⚽️|★●---[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.imgur.com/eE1f0UQ.jpg",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="FLA TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhLEocUcPiHswB9JUvhscpyGFXuCep9DHe1ngLu=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Santos Futebol Clube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhVsE3oJ6O4CEWOuJrLhQHG_q18E0PWCy31KBrTCJw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Red Bull Bragantino TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniiz5ab7vENzOarsQttt_sZHnYpSx0jqtxF7M4F=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Palmeiras/FAM",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhvxBcMVwoRLXylkoiANvv7UOTtVZ1pdd021nkxqQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Botafogo TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngbLgmsfBtdlcR09ymIv1lZtYgXZtDEwzPUQnhm5A=s88-c-k-c0x00ffffff-no-rj",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Fluminense Football Club",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjAXULFyrF8Cgz058nZRksy7mVNnwQPe8p6huzoOg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Vasco TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwng4Ki0Y6qdHZ4fBCo2FsrrQmMZE9laU_01FAmSYUA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Grêmio FBPA",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniLgCoqMZy-5yV8MnaoawlsGs7pTdFA39Gs32MRClo=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="São Paulo FC",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhrv_bG9jKMq9_MTVMmN1IA7PXmMaPsD4fGF9l0YA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Corinthians TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnh1D4ajctapDONjQqDihNl9GEqHkE5A3hroBlErYvs=s88-c-k-c0x00ffffff-no-rj",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="TV BAHÊA",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhKGZswIb4XIRoTafj5xG9zq3Xhrt1R90NTVD1PNg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Sport Club Internacional",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhI1Hh-RjldsWV3kZYPzp-m8yvdDx3ukVk70BKPDw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="TV Sport Recife",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj--eNhAZP0qPSbgsHivr2JjfFkM7hBIZmoo5Shcg=s88-c-k-c0x00ffffff-no-rj",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Athletico Paranaense",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngwXDMmNm4So4TR7AY232Uwgw81I5KHGeuDcO0nzA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dragão TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni1zzknj4GQ73EzfN4QI2leV7SRBBBGOA94pMKD1w=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Galo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngWa2Ms7_C3kkvqzgWxtYpRC5DQNobFU45pXDKJPQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Goiás Esporte Clube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj8DTpAAdPnJAiB2dPXKEFf3cHY4GCun-UmWiu1eg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vozão TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwng4dZ5ytmJSf6D6ExDqXNb2Vbm9TSDoHKaHdWGnBA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Leão",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj9-l88U8KMGbjiBEco95ImxKs6omGOZRpge8Zimg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="coritibaoficial",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngvEhDpZoreK8utGG1oH1GqRhrIL5COjgAR7Dz0hw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLORdarkblue]---●★| ⚽️ KodiTVR *Brasileirão Série B* Channels ⚽️|★●---[/COLOR]", 
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://i.imgur.com/eE1f0UQ.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cruzeiro Esporte Clube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngw_iMZGwhEgyu2grvtHuzFarmvVPuql50nFPYjcw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Associação Chapecoense De Futebol",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngk5YhWZK1f6j1eGW4kCzyS6WbfBTKiSS3b1cEIAg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Coelho Keno Minas",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjyxre8iDLt5Gha4Ujb0M3KqpTbdfDqKxedA-3Oog=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Sampaio",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnghcDE1rrmSPdOhgbKLQeEH6luD5MTBAldzuYeQJg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cuiabá Esporte Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnh7h1JzuHZ8LnxZHKECYxIRHDLdnkD57sLwa2YBzg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="E.C. Juventude Oficial",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniOAY4PazXnQ_9snDwJ_jmKk46LPIWIuNr0rc80sw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CSA Oficial",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjV4fx_S1JfiR6H6Px2XUzPmgQlbedKsQmvzxOT=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Guarani",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj6E5pBHkp3p7CLbQ2_Ul5pt49IuPR7B2DBznFsJA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PonTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngX4WEDCC3kvn8-6nD_QsKUBpZ45D9C2D3ETt-hrA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="TV Dragão",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngGuD80VhSQdQPAAV1uL38psGwg3-sOptipWVuIRQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="TV Avaí",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhEsKV7xRPme7enb3wpXn1Zw-yJ74L8NIn-J4TDqg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Galo TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj1pHHOIWYrnQy0pQ4UHniwbV1jf95r3fbe1mE0=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Operário Ferroviário Esporte Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniVQGvm5beCyx1dqNI1I0Gbym_3Pwe0KG7TfK-wzQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Vitória",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnitELHY26lgaJNZ170B_NzBFwubX0uTuXUCdamzcw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Paraná Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni7n4e261xdfxVQzxmCamwQ54YLs7MuMEyLZMHWzQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="TV Figueira",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjsPR6g_zI_hBxXDkn_UcPbYT3gl7qxjmFUJaXD=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="NáuticoPE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniKJSpXRW2peNAoXIzxvAtVuNarROQeY57nKl6fAA=s88-c-k-c0x00ffffff-no-rj",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="TV Botafogo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj3oXHS5oWcPUtJfRkIX6MvFN87CtqU-A6ZbfPj=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="OESTE BARUERI FUTEBOL CLUBE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjGtV-SH-kEsINOo50AKZGRDQmGl_EswGQIZw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item(
        #action="", 
        title="Canal Nacional De Futebol",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhuvMJc_bRZWs4SPAPMQbRNHFTOoT9XiFAWkNVWjQ=s88-c-k-c0x00ffffff-no-rj",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="[COLORyellow]---●★| ⚽️ KodiTVR *Brasileirão Série C (Grupo A - Grupo B)* Channels ⚽️|★●---[/COLOR]", 
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://i.imgur.com/eE1f0UQ.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aqui é Santa Cruz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni-3NrkMBC-jzCi3sysni4VghNmyybZ0oNPL_ITaQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Remo TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni3gEVvw4yDeISj1bfNEyM8jcCkRqGkzTEhsll0Ig=s88-c-k-c0x00ffffff-no-rj",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="TigrãoTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniUfiBaxPE1uztIHT7ZBpL4fIyJ7rgOPJqD8N4nJQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PapãoTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngEpTJnU7GLxe0sWWt1XbIUpYVyOPk1QBJ7Ck-RnQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ManausFC TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwng9JqAH-1hauYa_so3EWqrABLX1lQr84R2NaMHo=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tv Jacupa",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngkNQ8SR8xZPHlelyhGsJH66Bc_fZhMtVlXpRYY=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Ferrão",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngID9t_G8wpfL5YnLRhA5EnWrTXKJnc7qMGznvgfQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="TV13 Oficial",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhSnXsirY7QQejBpyXQrV-LAYU6fEWWOCUwtJg2=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="TV Aço Nação Cavalina",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjYjK_dyHrsfwg4Rug5BFenqtmHLnxeZRJnGMk5=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MyCujoo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjy_MoDmp36iw_m300x9bHXe7rqP0MJJTcIc2lGBQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Ypiranga Futebol Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniXH2sK9etwR-GrAr0lr0BFivHhRN71Oi_9hy5sxg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ituano Futebol Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngaIuTas0MzW7z3V--V9OKLmfkkdWcoPd7Dyy8x_A=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV LEC",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni01YZ7UfBY7HH0rOr2DF8c4Hml80qYTWynCD4X=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV BRUSCÃO",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngGwmyv18nhnOlzvnq_Fz0AtVk5xsh7RHKGrpu8Nw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV TOMBENSE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhcUkMmwVfQtFlSXOaUUwQPV37BR1KmFoHcXmFJ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="VoltaçoTV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni75nfDq6AyQS0_MiLkPUlrlg0OKgx1FuSUFFzd=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="São José Esporte Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjbqu03pD--EpxHOCjYKT-tYuhZskG4WLDlZNPa=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tv Tigre",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjK9ERm04aLDK1mHBJ_3awclR3SnZO06lOGdskIAw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Futebol Brasileiro",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhLPngnQz_TqWe5OymEjinXObC0iuh3OCBtdbgT=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Futebol Nacional",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngi7B4jup4EIE5vUrvnRwv0U-Om5XbYN-9RVWSdBw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SportsHD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjQda_47iFtxaIa1fec1ZK5kpnWFMnrrisqnJIv=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="OGB Videos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngYccjVBZeLCrUrW8UG0deS2Wn7cpMIrYqUh5Zb=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Teo CRi",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniqeq_e-bc2tYIxtaXz2LuscDOvC8k19yqVWgNfIg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="All Football",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwng_Og1q2ZPVw2mBouUCwJdU2hfe4W6nqP7NGfhc7Q=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
run()
