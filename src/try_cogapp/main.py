import argparse


def create_parser():
    parser = argparse.ArgumentParser("My CLI")
    parser.add_argument("--path", help="A useful path")

    return parser


def main():
    print(create_parser().parse_args())


if __name__ == "__main__":
    main()
