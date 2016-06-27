#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'First M. Last'
SITENAME = 'First M. Last'
SITESUBTITLE = 'Things and Stuff, Stuff and Things'
SITEURL = 'localhost:8000'

PATH = 'content'
STATIC_PATHS = ['img','presentations','publications', 'misc']

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'academia'
AVATAR = 'blank_avatar.png'
# Links widget
LINKS = (('cv', '/misc/Fake_CV.pdf'),
         ('email', 'mailto:username@domain_name'),
         ('github', 'https://github.com/your_real_username'))

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 90
DIRECT_TEMPLATES = ('index', 'posts_index', 'tags', 'archives')
PAGINATED_DIRECT_TEMPLATES = ['posts_index']

POSTS_PATHS = ['posts']
POSTS_URL = 'posts/'
POSTS_INDEX_SAVE_AS = 'posts/index.html'

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
