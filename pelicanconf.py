#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Treelym'
SITENAME = 'Treelym'
SITEURL = 'https://treelym.com'
GITHUB_URL = 'https://github.com/treelym'
CURRENT_YEAR = date.today().year

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (('Home', SITEURL), )

DEFAULT_PAGINATION = 12

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
