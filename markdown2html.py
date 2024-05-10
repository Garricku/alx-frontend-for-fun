#!/usr/bin/python3
"""Module for markdown2html"""

import os
import sys
"""Imported modules"""


def markdown_to_html(readme, readme_html_file_name):
    """
    Takes 2 argument strings:
    First argument is the name of the Markdown file
    Second argument is the output file name

    Requirements:
    If the number of arguments is less than 2: print in STDERR
    Usage: ./markdown2html.py README.md README.html
    and exit 1

    If the Markdown file doesn’t exist: print in STDER
    Missing <filename>
    and exit 1

    Otherwise, print nothing and exit 0
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(readme):
        print(f"Missing {readme}")
        sys.exit(1)

    sys.exit(0)