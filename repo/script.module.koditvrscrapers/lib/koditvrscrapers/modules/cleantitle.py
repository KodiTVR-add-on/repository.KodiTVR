# -*- coding: utf-8 -*-

"""
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
"""

import re
import unicodedata

from koditvrscrapers.modules import control

def get(title):
    if title is None: return
    try:
        title = control.six_encode(title)
    except:
        pass
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace('–', '-').replace('!', '')
    title = re.sub('\n|([[].+?[]])|([(].+?[)])|\s(vs|v[.])\s|(:|;|-|–|"|,|\'|\_|\.|\?)|\s', '', title).lower()
    return title


def get_title(title):
    if title is None: return
    try:
        title = control.six_encode(title)
    except:
        pass
    title = str(title)
    title = re.sub('&#(\d);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace('–', '-').replace('!', '')
    title = re.sub('\n|([[].+?[]])|([(].+?[)])|\s(vs|v[.])\s|(:|;|-|"|,|\'|\_|\.|\?)|\s', '', title)
    return title.lower()


def geturl(title):
    if title is None: return
    title = title.lower()
    title = title.rstrip()
    title = title.translate(None, ':*?"\'\.<>|&!,')
    title = title.replace('/', '-')
    title = title.replace(' ', '-')
    title = title.replace('--', '-')
    title = title.replace('–', '-')
    title = title.replace('!', '')
    return title


def get_url(title):
    if title is None: return
    title = title.replace(' ', '%20').replace('–', '-').replace('!', '')
    return title


def get_query_(title):
    if title is None: return
    title = title.replace(' ', '_').replace(':', '').replace('.-.', '.').replace('\'', '').replace(",", '').replace("'", '').replace('–', '-').replace('!', '')
    return title


def get_simple(title):
    if title is None: return
    title = title.lower()
    title = re.sub('(\d{4})', '', title)
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace('–', '-')
    title = re.sub('\n|\(|\)|\[|\]|\{|\}|\s(vs|v[.])\s|(:|;|-|–|"|,|\'|\_|\.|\?)|\s', '', title).lower()
    return title


def getsearch(title):
    if title is None: return
    title = title.lower()
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace('–', '-')
    title = re.sub('\\\|/|-|–|:|;|!|\*|\?|"|\'|<|>|\|', '', title).lower()
    return title


def query(title):
    if title is None: return
    title = title.replace('\'', '').rsplit(':', 1)[0].rsplit(' -', 1)[0].replace('-', ' ').replace('–', ' ').replace('!', '')
    return title


def get_query(title):
    if title is None: return
    title = title.replace(' ', '.').replace(':', '').replace('.-.', '.').replace('\'', '').replace('–', '.').replace('!', '')
    return title


def normalize(title):
    try:
        try: return control.six_encode(control.six_decode(title, char='ascii'))
        except: pass
        return str(''.join(c for c in unicodedata.normalize('NFKD', unicode(control.six_decode(title))) if unicodedata.category(c) != 'Mn'))
    except:
        return title


def clean_search_query(url):
    url = url.replace('-','+').replace(' ', '+').replace('–', '+').replace('!', '')
    return url