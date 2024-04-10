import argparse
import pprint

import requests
import logging

from src.try_cogapp.argparser import create_parser

logging.basicConfig()
logger = logging.getLogger(__name__)


def main():
    args = create_parser().parse_args()
    logger.debug(args)

    response = requests.get(args.url)
    pprint.pprint(response.status_code)
    pprint.pprint(response.json())


if __name__ == "__main__":
    main()
