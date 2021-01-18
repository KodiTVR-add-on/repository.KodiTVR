# -*- coding: utf-8 -*-

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re, urllib, urlparse
from koditvrscrapers.modules import cleantitle
from koditvrscrapers.modules import source_utils, log_utils
from koditvrscrapers.sources_koditvrscrapers import cfScraper


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['ganool.ws', 'ganol.si', 'ganool123.com', 'fmovies.tw']
        self.base_link = 'https://soapgate.online'
        self.search_link = '/search/?q=%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except BaseException:
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if url is None:
                return sources
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            q = '%s' % cleantitle.get_gan_url(data['title'])
            url = self.base_link + self.search_link % q
            r = cfScraper.get(url).content
            v = re.compile('<a href="(.+?)" class="ml-mask jt" title="(.+?)">\s+<span class=".+?">(.+?)</span>').findall(r)
            for url, check, qual in v:
                t = '%s (%s)' % (data['title'], data['year'])
                if t in check:
                    key = url.split('-hd')[1]
                    url = 'https://fmovies.tw/moviedownload.php?q=%s' % key
                    r = cfScraper.get(url).content
                    r = re.compile('<a rel=".+?" href="(.+?)" target=".+?">').findall(r)
                    for url in r:
                        if any(x in url for x in ['.rar']): continue
                        quality, info = source_utils.get_release_quality(qual, url)
                        valid, host = source_utils.is_host_valid(url, hostDict)
                        if valid:
                            info = ' | '.join(info)
                            sources.append(
                                {'source': host, 'quality': quality, 'language': 'en', 'url': url,
                                 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('---Ganool Testing - Exception: \n' + str(failure))
            return sources

    def resolve(self, url):
        return url
