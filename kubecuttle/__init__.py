"kubectl alternative for kubectl"

from __future__ import absolute_import
from .kubecuttle import apply


__project__      = 'kubecuttle'
__version__      = '1.0'
__keywords__     = ['kubecuttle']
__author__       = 'Prabhu Thangaraj'
__author_email__ = 'thangaraj.prabhu@gmail.com'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 1 - Demo",
    "Topic :: Utilities",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3"
]

__entry_points__ = {
    'console_scripts': [
        'kubecuttle = kubecuttlecli.kubecuttlecmd:main'
    ],
}

__requires__ = []

__extra_requires__ = {
    'doc':   ['mkdocs']
}
