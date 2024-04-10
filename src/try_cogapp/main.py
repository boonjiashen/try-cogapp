import argparse
import pprint

import requests
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


def create_parser():
    parser = argparse.ArgumentParser("URL-getter")
    parser.add_argument("--url", default='https://api.github.com', help="URL to get")

    return parser


def main():
    args = create_parser().parse_args()
    logger.debug(args)

    response = requests.get(args.url)
    pprint.pprint(response.status_code)
    pprint.pprint(response.json())


if __name__ == "__main__":
    main()
