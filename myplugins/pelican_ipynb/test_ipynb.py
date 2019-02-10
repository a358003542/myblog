#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
use pytest do some test
"""

from . import ipynb

def test_ipynb_to_html():
    content, info = ipynb.ipynb_to_html('test.ipynb')

    with open('test.html', 'w', encoding='utf8') as f:
        print(content, file=f)

def test_read_metadata():
    """
    :return:
    """
    metadata = ipynb.read_metadata('test.ipynb')
    assert 'date' in metadata