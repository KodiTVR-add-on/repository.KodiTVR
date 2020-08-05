# -*- coding: utf-8 -*-

from resources.lib import kodilogging
from resources.lib import plugin

import logging
import xbmcaddon

# Keep this file to a minimum, as Kodi
ADDON = xbmcaddon.Addon()
kodilogging.config()

plugin.run()


