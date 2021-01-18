# -*- coding: UTF-8 -*-
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

import re
import urlparse

from koditvrscrapers.modules import cleantitle
from koditvrscrapers.modules import client
from koditvrscrapers.modules import log_utils
from koditvrscrapers.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['fmoviesto.to']
        self.base_link = 'https://fmoviesto.to'
        self.search_link = '/search.html?keyword=%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            search_id = cleantitle.getsearch(title)
            url = urlparse.urljoin(self.base_link, self.search_link)
            url = url % (search_id.replace(':', ' ').replace(' ', '+'))
            search_results = client.request(url)
            match = re.compile('<a href="/watch/(.+?)" title="(.+?)">', re.DOTALL).findall(search_results)
            for row_url, row_title in match:
                row_url = self.base_link + '/watch/%s' % row_url
                if cleantitle.get(title) in cleantitle.get(row_title):
                    return row_url
            return
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url == None:
                return sources
            html = client.request(url)
            quality = re.compile('<div>Quanlity: <span class="quanlity">(.+?)</span></div>', re.DOTALL).findall(html)
            for qual in quality:
                quality = source_utils.check_url(qual)
                info = qual
            links = re.compile('var link_.+? = "(.+?)"', re.DOTALL).findall(html)
            for url in links:
                if not url.startswith('http'):
                    url = "https:" + url
                valid, host = source_utils.is_host_valid(url, hostDict)
                if valid:
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': url,
                                    'direct': False, 'debridonly': False})
            return sources
        except:
            return sources

    def resolve(self, url):
        if 'vidcloud' in url:
            r = client.request(url)
            url = re.compile('(?:file|source)(?:\:)\s*(?:\"|\')(.+?)(?:\"|\')').findall(r)[0]
        return url
