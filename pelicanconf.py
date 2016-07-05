#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick Sadil'
SITENAME = 'Patrick Sadil'
SITESUBTITLE = 'Graduate Student, Year 2'
SITEURL = 'http://people.umass.edu/psadil'

PATH = 'content'
STATIC_PATHS = ['img','presentations','publications', 'misc']

PLUGIN_PATHS = ["plugins", "/media/psadil/Data/git/pelican-plugins"]
PLUGINS = ["rmd_reader"]

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme/academia'
AVATAR = 'Patrick_Sadil.jpg'
# Links widget
LINKS = (('CV', 'misc/PatrickSadil_CV.pdf'),
         ('email', 'mailto:psadil@umass.edu'),
         ('github', 'https://github.com/psadil'))

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
