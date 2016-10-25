AUTHOR = 'Sam'
SITENAME = 'Bike Bike Run – Un blog sur le triathlon (entre autres)'
#SITEURL = 'http://bikebike.run/'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

DATE_FORMATS = {"fr": ("fr_FR", "%A %d %B %Y")}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Thank God I Run', 'http://thankgodirun.com/'),
         ('Runner Mais Pas Que', 'http://runnermaispasque.com/'),
         ('Triathlon For Fun', 'https://triathlonforfun.com'),
         #('City Run', 'http://city-run.fr/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

THEME = "themes/bikebikerun"

DEFAULT_PAGINATION = 10

PLUGINS = [
    "plugins.filetime_from_git",
]

DEFAULT_DATE = 'fs'
STATIC_PATHS = ['images']

DEFAULT_METADATA = {
    'status': 'draft',
    "lang": "fr",
}

MD_EXTENSIONS = [
    "markdown.extensions.footnotes",
    "markdown.extensions.smarty",
    "markdown.extensions.attr_list",
]

GIT_GENERATE_PERMALINK = False
