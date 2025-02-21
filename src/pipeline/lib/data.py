#!/usr/bin/env python3
"""
Fetch BlobToolKit Pipeline data.

NOT YET IMPLEMENTED

Usage: blobtools pipeline data --config YAML

Options:
    --config YAML  YAML format configuration filename.
"""

import logging
import re
import sys
from collections import defaultdict

from docopt import DocoptExit
from docopt import docopt

logger_config = {
    "level": logging.INFO,
    "format": "%(asctime)s [%(levelname)s] line %(lineno)d %(message)s",
    "filemode": "w",
}
logging.basicConfig(**logger_config)
logger = logging.getLogger()


def main():
    """Entry point."""
    try:
        args = docopt(__doc__)
    except DocoptExit:
        raise DocoptExit
