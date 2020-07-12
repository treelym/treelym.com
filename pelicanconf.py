#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Treelym'
SITENAME = 'Treelym'
SITEURL = ''

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
LINKS = (('Home', SITEURL),
         ('Posts', SITEURL + '/posts'),
         ('About', SITEURL + '/about'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 12

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True