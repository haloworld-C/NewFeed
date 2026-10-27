#!/usr/bin/env python3
"""Minimal Markdown -> HTML converter for NewFeed archive files.

Handles only the subset used in news/*.md and great-books/*.md:
# / ## / ### headings, paragraphs, **bold**, [text](url), > blockquotes.
Usage: md2html.py <file.md>  -> HTML on stdout
"""
import html
import re
import sys


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def convert(md: str) -> str:
    out = []
    para = []

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    for raw in md.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1)) + 1  # h1->h2 etc. (reader already shows title)
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        if line.startswith(">"):
            flush()
            out.append(f"<blockquote>{inline(line.lstrip('> '))}</blockquote>")
            continue
        para.append(line)
    flush()
    return "\n".join(out)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        print(convert(f.read()))
