#!/usr/bin/env python
from __future__ import unicode_literals

AUTHOR = 'Ondřej Podsztavek'
SITENAME = 'podondra site'
SITESUBTITLE = 'just a computer science student\'s essays'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# My new stuff
THEME = 'theme'
DIRECT_TEMPLATES = ['index', 'categories']
STATIC_PATHS = ['images', 'extra', '../README.rst']
EXTRA_PATH_METADATA = {
        'extra/keyboard.png': {'path': 'keyboard.png'},
        'extra/CNAME': {'path': 'CNAME'},
        '../README.rst': {'path': 'README.rst' },
        }
DEFAULT_DATE = 'fs'
SUMMARY_MAX_LENGTH = 15
