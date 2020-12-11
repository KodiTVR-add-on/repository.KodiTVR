# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Liga Nos TV by KodiTVR
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

addonID = 'plugin.video.KodiTVR_Liga-Nos'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "Add-on KodiTVR(Fuck_You_Grupeta)"
YOUTUBE_CHANNEL_ID_2 = "slbenfica"
YOUTUBE_CHANNEL_ID_3 = "SportingCP"
YOUTUBE_CHANNEL_ID_4 = "fcporto"
YOUTUBE_CHANNEL_ID_5 = "1921scbraga"
YOUTUBE_CHANNEL_ID_6 = "VSCoficial"
YOUTUBE_CHANNEL_ID_7 = "rafc1939"
YOUTUBE_CHANNEL_ID_8 = "MarketingBoavista"
YOUTUBE_CHANNEL_ID_9 = "FCFamalicao1931"
YOUTUBE_CHANNEL_ID_10 = "UC1fMA-YLirbPBTs3mjuaUBQ"
YOUTUBE_CHANNEL_ID_11 = "CDNacionalTV"
YOUTUBE_CHANNEL_ID_12 = "UCkeEgKzqUIS_T4V1w-fOmOA"
YOUTUBE_CHANNEL_ID_13 = "FCPF1950"
YOUTUBE_CHANNEL_ID_14 = "GilVicenteFutebolC"
YOUTUBE_CHANNEL_ID_15 = "MoreirenseFC38"
YOUTUBE_CHANNEL_ID_16 = "UCj7TKcvf3y82tGW_0QZIiyQ"
YOUTUBE_CHANNEL_ID_17 = "UCHtqrolH5tlrj4vB97kF-AA"
YOUTUBE_CHANNEL_ID_18 = "cdtondela"
YOUTUBE_CHANNEL_ID_19 = "TheCFBelenenses"
YOUTUBE_CHANNEL_ID_20 = "*Segunda Liga Portuguesa(e S.C. Vila Real)*"
YOUTUBE_CHANNEL_ID_21 = "academicaoaf"
YOUTUBE_CHANNEL_ID_22 = "UCJYN6zWIQ5iO9JUoK2vd77w"
YOUTUBE_CHANNEL_ID_23 = "webmasterLSC"
YOUTUBE_CHANNEL_ID_24 = "GDEPraia"
YOUTUBE_CHANNEL_ID_25 = "CDFeirense1918"
YOUTUBE_CHANNEL_ID_26 = "FCAroucaOficial"
YOUTUBE_CHANNEL_ID_27 = "UC6QUrvNjXlYj6cOtRpL-IbQ"
YOUTUBE_CHANNEL_ID_28 = "UC7i9tYzX3DjiIVBoVcqXKtw"
YOUTUBE_CHANNEL_ID_29 = "UCkU0iBsXJ6JxH0zE2QDXRhg"
YOUTUBE_CHANNEL_ID_30 = "UCRYHkejS-vpVtSPMlxBGkhQ"
YOUTUBE_CHANNEL_ID_31 = "UCBJLEXBu0Jw334iBrdOaEcQ"
YOUTUBE_CHANNEL_ID_32 = "UCV7WROfx5_aIQNoXKsG4pLg"
YOUTUBE_CHANNEL_ID_33 = "UCs2UKNwnvVwy3UtSjVO5yfg"
YOUTUBE_CHANNEL_ID_34 = "tvfcpenafiel"
YOUTUBE_CHANNEL_ID_35 = "UCO5SilnKmvajcWSh3YBZ79g"
YOUTUBE_CHANNEL_ID_36 = "ClubeDesportivoMafra"
YOUTUBE_CHANNEL_ID_37 = "mktvfc"
YOUTUBE_CHANNEL_ID_38 = "FPFutebolOficial"
YOUTUBE_CHANNEL_ID_39 = "UCsIoK3XP-cVcpoCC_SdjZdg"
YOUTUBE_CHANNEL_ID_40 = "UCuIlu5oGIj1RzHOYmeSV5Eg"
YOUTUBE_CHANNEL_ID_41 = "SCVilaReal"
YOUTUBE_CHANNEL_ID_42 = "*Football - International*"
YOUTUBE_CHANNEL_ID_43 = "realmadridcf"
YOUTUBE_CHANNEL_ID_44 = "fcbarcelona"
YOUTUBE_CHANNEL_ID_45 = "LiverpoolFC"
YOUTUBE_CHANNEL_ID_46 = "UC6yW44UGJJBvYTlfC7CRg2Q"
YOUTUBE_CHANNEL_ID_47 = "chelseafc"
YOUTUBE_CHANNEL_ID_48 = "fcbayern"
YOUTUBE_CHANNEL_ID_49 = "bvb"
YOUTUBE_CHANNEL_ID_50 = "EintrachtMedia"
YOUTUBE_CHANNEL_ID_51 = "werderbremen"
YOUTUBE_CHANNEL_ID_52 = "milanchannel"
YOUTUBE_CHANNEL_ID_53 = "juventus"
YOUTUBE_CHANNEL_ID_54 = "INTER"
YOUTUBE_CHANNEL_ID_55 = "asroma"
YOUTUBE_CHANNEL_ID_56 = "clubatleticodemadrid"
YOUTUBE_CHANNEL_ID_57 = "mcfcofficial"
YOUTUBE_CHANNEL_ID_58 = "ArsenalTour"
YOUTUBE_CHANNEL_ID_59 = "PSGofficiel"
YOUTUBE_CHANNEL_ID_60 = "UCzHCZXmqIdjqRnpdp0l_T6g"
YOUTUBE_CHANNEL_ID_61 = "ASMONACOFCSA"
YOUTUBE_CHANNEL_ID_62 = "2galatasaray"
YOUTUBE_CHANNEL_ID_63 = "FBSKTV"
YOUTUBE_CHANNEL_ID_64 = "ajax"
YOUTUBE_CHANNEL_ID_65 = "bocaentretenimientos"
YOUTUBE_CHANNEL_ID_66 = "cariverplatetv"
YOUTUBE_CHANNEL_ID_67 = "spursofficial"


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
        title="[COLORgold]---●★| ⚽️ KodiTVR *Primeira Liga* Channels ⚽️|★●---[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.imgur.com/PnCLBbA.png",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="Sport Lisboa e Benfica",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjzSxx_y2GKfFZSzXNX_8cR4kag8GVmCtg29_J4uVo=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sporting Clube de Portugal",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngx42x8UpciT6ReI3-iznMCEvvyVD7511uwXb6bKw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FC Porto",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngASODO6HOlp05X8AcjHngDtTNPkp403dNvTRxzy_Q=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SC Braga",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhWd5Pl7eqvsmnjrCa5Hlwni2bC2GvbPVVlJVBKtA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vitória SC",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniWilm110vOBMuSlFtIP-cp41EnjsF6KXwTjl4l_w=s88-c-k-c0x00ffffff-no-rj",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Rio Ave Futebol Clube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwng4kpQOVj2I5f_zhTLe3fQK480hTsH8xW8ZnBs-ug=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Boavista Futebol Clube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjakFGRLbP_LWpnVBRAJxYXWyQQ-WP6851GNGdcFA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Futebol Clube de Famalicão",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjZeGkBX9VtAx2cRNyo47RG8W8kQMeQ-9FnjaCbxQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Clube Desportivo Santa Clara, Açores",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni46aeqNbGPl7ORz5WLnuqyQXSh2SIK2iekMtqMFw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CDNacionalTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhCX6cFogxBAqyLaJ0Pi4KA7YmEq9UbS7ZUpE_d=s88-c-k-c0x00ffffff-no-rj",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="CS Maritimo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniNIfwJ0Xm_tYWQCdM0Yw56EuBi7VCLz3Zm84gb=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="FC Paços de Ferreira",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnh2-WGNv6l_lgKO9p1_vdDMa6NlgNEHolcpm_Wu5A=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Gil Vicente",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhp0oOea-AEiLMAkD8BD4QfXfMP9HJIXLNQ8iFo=s88-c-k-c0x00ffffff-no-rj",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="MOREIRENSE FUTEBOL CLUBE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngfvuXcOHDB7GS2HzNlnYXr-KviOQVAXltehMVUPQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Oficial Portimonense Televisão",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniitm_kq4hhQ2b5XHFxt0Pas854ogZR_pOKUSo1zQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FARENSE TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngGq-WzFY9JzOL6Viy11z-8dEpv2FtQSLkaX-KE=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CD Tondela",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngExzVQcHrYHXYhP5Hrx_NfrwEb3bxdSFRpXoYckQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Belém TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhdlB8-b36JsMZjadSi9zLC_y1-bjQLPB-KshEj=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLORgold]---●★| ⚽️ KodiTVR *Segunda Liga* Channels ⚽️|★●---[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://i.imgur.com/B4OpkDW.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="academicaoaf",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngMMnkmMjRphajWtJhZluVgnvT2X5NmBmDW0Yri=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Grupo Desportivo Chaves",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjJ_rveDVxsCao9Q9b2hj1cqLUVNM_ZWBemB-bp0A=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Leixões Sport Club",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhbOuerATSqMCKluT4jC8CD3nK2U9xEYVSNwv3x=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Grupo Desportivo Estoril Praia",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngOVyAnXuW_Bmqi4rNR0WYdNM0PVmytgfbZ_EQUnQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Clube Desportivo Feirense",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjZxujIJgTWGNnYGmDV4gL6hnpScA0epLpPk6RT4A=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FCAroucaOficial",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhVrkS5XX3hRhloefZryrcShEKrpnkISbps5Jxp=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Casa Pia AC Comunicação",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjQAKQURkELV-l61wRJHUL0dVj5cygeMjJ4f1KIJA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CD Cova Piedade",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnidt1mswBaKM-XJ6ayLtWtrpsEyVrHJfIJWnuUV=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="adeptos F.C. VIZELA",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjuPRWo3GUaQTOzJHWaakjE-QurEgBRVZt8uZA8=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sporting Clube da Covilhã",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngjP1VLYBHB8JjQn_yNHN0FFBc2Phk_DXDRPZiH=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="União Desportiva Vilafranquense",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnglf-wp2JkWkGMAPGCmXY3AsI2Q2qaocL1skwXG=s88-c-k-c0x00ffffff-no-rj",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Académico de Viseu Futebol Clube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngHhVPGGeUv8GvkUhtbLGShQnJmjVENXDveaumc=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Varzim Sport Club Multimédia",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniXrWex4QwtRtcAUhfZ2Pyz0qLc6vCajuTFy0kD=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FC Penafiel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjurnjKyCR_eUV46jaOVz0nWE5TshIHIqYxG7VZZg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="UD Oliveirense",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhpw0VaQw8b4mVDo-XJvgbrxdC_2AUZgvKuVDIQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ClubeDesportivoMafra",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniKfwcF7YrnFkhs93nXDi0Nu3ih8qcfLP8_SVSS=s88-c-k-c0x00ffffff-no-rj",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Vitória Futebol Clube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhNhUcIOEV_AJClAx5zRjYWc0OXIgH8mOVaMOMZjQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Canal11",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjfwCgUV9uLMgFIScqVV_YhGcRYRAYEyEi0dehd=s88-c-k-c0x00ffffff-no-rj",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Federação Portuguesa de Futebol",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj_Oi9_lsJbI24yZay7u0aVX3yGKHu-w3aVwaln=s88-c-k-c0x00ffffff-no-rj",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="VSPORTS - Liga NOS",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj7_HJavihTdjwmnNh2-y8J6uaOhk_6853Se2QFWA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SCVilaReal",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjpc-qRTjJ8udnfCeCAEI8cgziditd5d770IvcW=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item(
        #action="", 
        title="[COLORgold]---●★| ⚽️ KodiTVR *Football - International* Channels ⚽️|★●---[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://i.imgur.com/U2h6k0E.jpg",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="Real Madrid",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjLWwm1cDoFo65P-dqKbmG45ozzrFgv87XdfdLnYa0=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FC Barcelona",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnilINlipkvw1ijwWsp_0I3YGmb_9bHk6TshlpYGzVM=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Liverpool FC",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhFDKPrdtata8maXMqPwhhC5sq_lJpEpZP76hUHk0o=s88-c-k-c0x00ffffff-no-rj",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Manchester United",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwng1lhnPSqypAfQhEuoUeOyT6e3Yu9QoPh6QddCz0w=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chelsea Football Club",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngV_tkwdihGaN2NulJrALp6itU0FtIbDyc49i3F2FY=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FC Bayern München",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-2Y_1_ERp2EE/AAAAAAAAAAI/AAAAAAAAAAA/WjpNzvZ-s_g/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Borussia Dortmund",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni73kTBQcUzx6j4guzVE-71DW9hoU3Y1KfjKU9ukjc=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Eintracht Frankfurt",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni0F0d8Vier5y1wEV07z2LnKcji93FTQsU0xEPiPpU=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Werder Bremen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniTio3VIodty4s6_GmovPwz77brqJqEus3W5UiOb7I=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="AC Milan",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjueHi1ZtRb3hGwDSEC_NjCbB16PJARVF8lwm6PFXQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Juventus",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj6QbT689dmT3xCfSPUGN8oBmMHQ3hXH9EzEnj4Imo=s88-c-k-c0x00ffffff-no-rj",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Inter",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniN-SITdzcufUyT8AYwW8IHtT0prvgFfPibokpz5w=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AS Roma",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngwX_cvj9lft0OlfYaUXc-8hWqjzr9XtCxHbdwuig=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Atlético de Madrid",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnh3gU9MAYRT-Y8NjBFsP7WypmfxC-h4tIQwR2gZjvU=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Man City",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhhZ0utnNy_q2zvrt_1uwfy-MAue6exlFO4ye-xo28=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Arsenal",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhtlTU4PV85s58rqOnGLRQP4p498PhQw_YxUCF6Y2Q=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="PSG - Paris Saint-Germain",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjgIjnDfoh_yW0iky4Tck-bHeLJ6fo0N18R1UfWUxs=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Olympique Lyonnais",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngKPWCsORbipbOfitDA8bLvEMSadWWOCuuGNAulgUg=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AS MONACO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniSrSnFhliYDmji0Z3EP_wJRjkZBj6G5yXtBOU6lQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Galatasaray",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnieXeDBee5gMzA9aiHfudpWQMEyOhvFhim3Un8oGYQ=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fenerbahçe SK",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwngB8gx6HENrn4UZkcrkGqrUAW-wvNNTK8CDzM54hGA=s88-c-k-c0x00ffffff-no-rj",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AFC Ajax",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnig6NZKZRPR6C0DyIp1DGfj4cUk3uoBfMz4l89pew=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Club Atlético Boca Juniors",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwni5Hf_vRhFiUpxsX7w5y1UhjYSE1QvBV381c8rePw=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Club Atlético River Plate",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjVH6m97wVSBG7KVzx17EV1_WwbQ4m0fFGZGyA97Q=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="Tottenham Hotspur",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="https://yt3.ggpht.com/ytc/AAUvwniWmCvWqErL14F1kNa7bgF_xoLOoeISQJ_4IXzfMsU=s88-c-k-c0x00ffffff-no-rj",
        folder=True )
run()
