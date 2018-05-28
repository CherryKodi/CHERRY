"""
    resolveurl XBMC Addon
    Copyright (C) 2015 tknorris

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
from lib import jsunpack
from lib import helpers
from resolveurl import common
from resolveurl.resolver import ResolveUrl, ResolverError
import string,requests

class CdaResolver(ResolveUrl):
    name = "cda"
    domains = ['cda.pl', 'www.cda.pl', 'ebd.cda.pl']
    pattern = '(?:\/\/|\.)(cda\.pl)\/(?:.\d+x\d+|video)\/(.*)'

    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        direct = re.findall("""file":"(.*)","file_cast""", requests.get(web_url).content)[0].replace("\\/","/")
        return direct
        raise ResolverError('Video Link Not Found')

    def get_url(self, host, media_id):
        return 'http://ebd.cda.pl/620x368/%s' % media_id
