if __name__ == "__main__":
    import sys
    import os
    import json
    # ugly hack, but oh well
    sys.path.append("%s/.kodi/addons/plugin.video.KodiTVR_Streams" % os.getenv("HOME"))


from helpers import log

import generic_m3u8_searcher
import ovostreams
import liveonscorenet
import liveonscoretv
import hdstreamsclub
import streamcr7net
import techobestcom
import hazmowatch
import footballstreamto
import soccer24hdcom
import dubsstreamzcom
import oomovienet
import papahdlive
import _60fpslive
import myoplaylive
import sportstreampw
import b9streamclub
import redsoccerinfo
import worldstreamsnet
import buffstreamlive
import streamfoottk
import redditstreamsblogspotcom
import daddylivelive
import fightpasssite
import mazymediascom
import hhdstreamsclub
import hockeynewssite
import buffstream1com

# list of sources
all_sources = [
    generic_m3u8_searcher,
    ovostreams,
    liveonscorenet,
    liveonscoretv,
    hdstreamsclub,
    streamcr7net,
    techobestcom,
    hazmowatch,
    footballstreamto,
    soccer24hdcom,
    dubsstreamzcom,
    oomovienet,
    papahdlive,
    _60fpslive,
    myoplaylive,
    sportstreampw,
    b9streamclub,
    redsoccerinfo,
    worldstreamsnet,
    buffstreamlive,
    streamfoottk,
    redditstreamsblogspotcom,
    daddylivelive,
    fightpasssite,
    mazymediascom,
    hhdstreamsclub,
    hockeynewssite,
    buffstream1com,
]

def url_to_source(url, fallback = generic_m3u8_searcher):
    for s in all_sources:
        if s.can_handle(url):
            return s
    return fallback

if __name__ == "__main__":
    def test():
        url = "http://www.sportstream.pw/football6/index.html"
        r = url_to_source(url)
        print(r)

    test()
