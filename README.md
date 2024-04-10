# try-cogapp

This project demonstrates using cogapp.

## Usage

```bash
pip install pre-commit
pip install pdm
pre-commit run --all
```

You should see:

```
cog......................................................................Passed
```

# Example CLI


<!-- [[[cog
import cog
import argparse
import src.try_cogapp.main

HELP_WIDTH = 80
parser = src.try_cogapp.main.create_parser()
formatter = lambda prog: argparse.RawTextHelpFormatter(prog, width=HELP_WIDTH)
parser.formatter_class = formatter
help_msg = parser.format_help().strip()
cog.out(f"""
```
{help_msg}
```
""")
]]] -->

```
usage: My CLI [-h] [--path PATH]

options:
  -h, --help   show this help message and exit
  --path PATH  A useful path
```
<!-- [[[end]]] -->
