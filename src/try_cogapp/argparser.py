"""Defines argument parser.

This module is standalone so that cogapp can have a smaller dependency graph.
"""

import argparse
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


def create_parser():
    parser = argparse.ArgumentParser("URL-getter")
    parser.add_argument("--url", default='https://api.github.com', help="URL to get")

    return parser
