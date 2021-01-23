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
import urllib
import urlparse
import traceback

from koditvrscrapers.modules import client, debrid, log_utils, source_utils
from koditvrscrapers.sources_koditvrscrapers import cfScraper


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['rlsbb.com', 'rlsbb.ru', 'rlsbb.to']
        self.base_link = 'http://rlsbb.ru/'
        self.search_base_link = 'http://search.rlsbb.ru/'
        self.search_cookie = 'serach_mode=rlsbb'
        self.search_link = '/lib/search526049.php?phrase=%s&pindex=1&content=true'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('RLSBB - Exception: \n' + str(failure))
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('RLSBB - Exception: \n' + str(failure))
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url is None:
                return

            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('RLSBB - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None:
                return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            hdlr = 'S%02dE%02d' % (int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else data['year']
            premDate = ''

            query = '%s S%02dE%02d' % (
                data['tvshowtitle'],
                int(data['season']),
                int(data['episode'])) if 'tvshowtitle' in data else '%s %s' % (
                data['title'],
                data['year'])
            query = re.sub('(\\\|/| -|:|;|\*|\?|"|\'|<|>|\|)', '', query)

            query = query.replace("&", "and")
            query = query.replace("  ", " ")
            query = query.replace(" ", "-")

            url = self.search_link % urllib.quote_plus(query)
            url = urlparse.urljoin(self.base_link, url)

            url = "http://rlsbb.ru/" + query

            r = cfScraper.get(url).content

            if r is None and 'tvshowtitle' in data:
                season = re.search('S(.*?)E', hdlr)
                season = season.group(1)
                query = title
                query = re.sub('(\\\|/| -|:|;|\*|\?|"|\'|<|>|\|)', '', query)
                query = query + "-S" + season
                query = query.replace("&", "and")
                query = query.replace("  ", " ")
                query = query.replace(" ", "-")
                url = "http://rlsbb.ru/" + query
                r = cfScraper.get(url).content

            for loopCount in range(0, 2):
                if loopCount == 1 or(
                        r is None and 'tvshowtitle' in data):

                    #premDate = re.sub('[ \.]', '-', data['premiered'])
                    query = re.sub('[\\\\:;*?"<>|/\-\']', '', data['tvshowtitle'])
                    query = query.replace(
                        "&", " and ").replace(
                        "  ", " ").replace(
                        " ", "-")  # throw in extra spaces around & just in case
                    #query = query + "-" + premDate

                    url = "http://rlsbb.ru/" + query
                    url = url.replace('The-Late-Show-with-Stephen-Colbert', 'Stephen-Colbert')

                    r = cfScraper.get(url).content

                posts = client.parseDOM(r, "div", attrs={"class": "content"})
                hostDict = hostprDict + hostDict
                items = []
                for post in posts:
                    try:
                        u = client.parseDOM(post, 'a', ret='href')
                        for i in u:
                            try:
                                name = str(i)
                                if hdlr in name.upper():
                                    items.append(name)
                                #elif len(premDate) > 0 and premDate in name.replace(".", "-"):
                                    #items.append(name)
                            except Exception:
                                failure = traceback.format_exc()
                                log_utils.log('RLSBB - Exception: \n' + str(failure))
                                pass
                    except Exception:
                        failure = traceback.format_exc()
                        log_utils.log('RLSBB - Exception: \n' + str(failure))
                        pass

                if len(items) > 0:
                    break

            seen_urls = set()

            for item in items:
                try:
                    info = []

                    url = str(item)
                    url = client.replaceHTMLCodes(url)
                    url = url.encode('utf-8')

                    if url in seen_urls:
                        continue
                    seen_urls.add(url)

                    host = url.replace("\\", "")
                    host2 = host.strip('"')
                    host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(host2.strip().lower()).netloc)[0]

                    if host not in hostDict:
                        raise Exception()
                    if any(x in host2 for x in ['.rar', '.zip', '.iso', '.part']):
                        continue

                    quality, info = source_utils.get_release_quality(host2)

                    #try:
                    #    size = re.findall('((?:\d+\,\d+\.\d+|\d+\.\d+|\d+\,\d+|\d+)\s*(?:GiB|MiB|GB|MB))', post)[0]
                    #    div = 1 if size.endswith(('GB', 'GiB')) else 1024
                    #    size = float(re.sub('[^0-9|/.|/,]', '', size.replace(',', '.'))) / div
                    #    size = '%.2f GB' % size
                    #    info.append(size)
                    #except:
                    #    pass

                    info = ' | '.join(info)

                    host = client.replaceHTMLCodes(host)
                    host = host.encode('utf-8')
                    sources.append({'source': host, 'quality': quality, 'language': 'en',
                                    'url': host2, 'info': info, 'direct': False, 'debridonly': True})
                except Exception:
                    failure = traceback.format_exc()
                    log_utils.log('RLSBB - Exception: \n' + str(failure))
                    pass
            check = [i for i in sources if not i['quality'] == 'CAM']
            if check:
                sources = check
            return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('RLSBB - Exception: \n' + str(failure))
            return sources

    def resolve(self, url):
        return url