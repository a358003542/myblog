#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from pelican import signals
from pelican.readers import BaseReader

from nbconvert.exporters import HTMLExporter
import nbformat


def ipynb_to_html(filepath, start=0, end=None):
    """Convert ipython notebook to html
    Return: html content of the converted notebook
    """
    exporter = HTMLExporter(template_file='basic')
    content, info = exporter.from_filename(filepath)

    return content, info


def read_metadata(filepath):
    ipynb_file = open(filepath, encoding='utf-8').read()
    notebook_metadata = nbformat.reads(ipynb_file, as_version=4)['metadata']

    for item in ('kernelspec', 'language_info'):
        if item in notebook_metadata:
            del notebook_metadata[item]

    return notebook_metadata


class IPythonNB(BaseReader):
    """
    Extend the Pelican.BaseReader to `.ipynb` files can be recognized
    as a markup language:

    Setup:

    `pelicanconf.py`:
    ```
    MARKUP = ('md', 'ipynb')
    ```
    """
    enabled = True
    file_extensions = ['ipynb']

    def read(self, filepath):
        metadata = {}
        metadata['ipython'] = True

        notebook_metadata = read_metadata(filepath)

        # Change to standard pelican metadata
        for key, value in notebook_metadata.items():
            metadata[key] = self.process_metadata(key, value)

        content, info = ipynb_to_html(filepath)

        return content, metadata


def add_reader(readers):
    readers.reader_classes['ipynb'] = IPythonNB


def register():
    signals.readers_init.connect(add_reader)
