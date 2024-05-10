#!/usr/bin/python3
"""Module for markdown2html"""

import os
import sys
import re
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

    with open(readme, "r") as md_file:
        markdown_content = md_file.read()

    html_content = re.sub(r"(#+)\s+(.*)", lambda match: f"<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>", markdown_content)
    html_content = re.sub(r"^\s*-\s+(.*)", r"<ul><li>\1</li></ul>", html_content, flags=re.MULTILINE)
    html_content = re.sub(r"^\s*\*\s+(.*)", r"<ol><li>\1</li></ol>", html_content, flags=re.MULTILINE)
    html_content = re.sub(r"(\S.*?)(\n\n|\Z)", r"<p>\1</p>", html_content, flags=re.DOTALL)
    html_content = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", html_content)
    html_content = re.sub(r"__(.*?)__", r"<em>\1</em>", html_content)

    with open(readme_html_file_name, "w") as html_file:
        html_file.write(html_content)

    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_markdown_file = sys.argv[1]
    output_html_file_name = sys.argv[2]
    markdown_to_html(input_markdown_file, output_html_file_name)