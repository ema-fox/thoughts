#!/usr/bin/env python

from os import listdir
from re import compile, sub
from subprocess import run

link_re = compile('(?<!\w)-(\w+(?:-\w+)*)')

def link_sub(m):
    name = m.group(1)
    return 'link:{}.html[{}]'.format(
        name,
        name.replace('-', ' ')
    )

for name in listdir():
    if name.endswith('.adoc'):
        with open(name) as f:
            text = f.read(None)
        text = sub(link_re, link_sub, text)
        run(['asciidoc',
             '--backend=html',
             '--out-file=rendered/{}.html'.format(name[:-len('.adoc')]),
             '-'],
            input=bytes(text, 'utf-8'))
