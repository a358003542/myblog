#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
from loguru import logger
import sys
import re

import six

from simple_pelican.settings import read_settings
from simple_pelican.log import init as init_logging
from simple_pelican.readers import Readers
from simple_pelican import signals
from simple_pelican.utils import (clean_output_dir, file_watcher,
                                  folder_watcher, maybe_pluralize)

__version__ = "0.0.1a0"
DEFAULT_CONFIG_NAME = 'pelicanconf.py'


class Pelican(object):

    def __init__(self, settings):
        """Pelican initialisation

        Performs some checks on the environment before doing anything else.
        """

        # define the default settings
        self.settings = settings
        self._handle_deprecation()

        self.path = settings['PATH']
        self.theme = settings['THEME']
        self.output_path = settings['OUTPUT_PATH']
        self.ignore_files = settings['IGNORE_FILES']
        self.delete_outputdir = settings['DELETE_OUTPUT_DIRECTORY']
        self.output_retention = settings['OUTPUT_RETENTION']

        self.init_path()
        self.init_plugins()
        signals.initialized.send(self)

    def init_path(self):
        if not any(p in sys.path for p in ['', os.curdir]):
            logger.debug("Adding current directory to system path")
            sys.path.insert(0, '')

    def init_plugins(self):
        self.plugins = []
        logger.debug('Temporarily adding PLUGIN_PATHS to system path')
        _sys_path = sys.path[:]
        for pluginpath in self.settings['PLUGIN_PATHS']:
            sys.path.insert(0, pluginpath)
        for plugin in self.settings['PLUGINS']:
            # if it's a string, then import it
            if isinstance(plugin, six.string_types):
                logger.debug("Loading plugin `%s`", plugin)
                try:
                    plugin = __import__(plugin, globals(), locals(),
                                        str('module'))
                except ImportError as e:
                    logger.error(
                        "Cannot load plugin `%s`\n%s", plugin, e)
                    continue

            logger.debug("Registering plugin `%s`", plugin.__name__)
            plugin.register()
            self.plugins.append(plugin)
        logger.debug('Restoring system path')
        sys.path = _sys_path

    def _handle_deprecation(self):

        if self.settings.get('CLEAN_URLS', False):
            logger.warning('Found deprecated `CLEAN_URLS` in settings.'
                           ' Modifying the following settings for the'
                           ' same behaviour.')

            self.settings['ARTICLE_URL'] = '{slug}/'
            self.settings['ARTICLE_LANG_URL'] = '{slug}-{lang}/'
            self.settings['PAGE_URL'] = 'pages/{slug}/'
            self.settings['PAGE_LANG_URL'] = 'pages/{slug}-{lang}/'

            for setting in ('ARTICLE_URL', 'ARTICLE_LANG_URL', 'PAGE_URL',
                            'PAGE_LANG_URL'):
                logger.warning("%s = '%s'", setting, self.settings[setting])

        if self.settings.get('AUTORELOAD_IGNORE_CACHE'):
            logger.warning('Found deprecated `AUTORELOAD_IGNORE_CACHE` in '
                           'settings. Use --ignore-cache instead.')
            self.settings.pop('AUTORELOAD_IGNORE_CACHE')

        if self.settings.get('ARTICLE_PERMALINK_STRUCTURE', False):
            logger.warning('Found deprecated `ARTICLE_PERMALINK_STRUCTURE` in'
                           ' settings.  Modifying the following settings for'
                           ' the same behaviour.')

            structure = self.settings['ARTICLE_PERMALINK_STRUCTURE']

            # Convert %(variable) into {variable}.
            structure = re.sub(r'%\((\w+)\)s', r'{\g<1>}', structure)

            # Convert %x into {date:%x} for strftime
            structure = re.sub(r'(%[A-z])', r'{date:\g<1>}', structure)

            # Strip a / prefix
            structure = re.sub('^/', '', structure)

            for setting in ('ARTICLE_URL', 'ARTICLE_LANG_URL', 'PAGE_URL',
                            'PAGE_LANG_URL', 'DRAFT_URL', 'DRAFT_LANG_URL',
                            'ARTICLE_SAVE_AS', 'ARTICLE_LANG_SAVE_AS',
                            'DRAFT_SAVE_AS', 'DRAFT_LANG_SAVE_AS',
                            'PAGE_SAVE_AS', 'PAGE_LANG_SAVE_AS'):
                self.settings[setting] = os.path.join(structure,
                                                      self.settings[setting])
                logger.warning("%s = '%s'", setting, self.settings[setting])

        for new, old in [('FEED', 'FEED_ATOM'), ('TAG_FEED', 'TAG_FEED_ATOM'),
                         ('CATEGORY_FEED', 'CATEGORY_FEED_ATOM'),
                         ('TRANSLATION_FEED', 'TRANSLATION_FEED_ATOM')]:
            if self.settings.get(new, False):
                logger.warning(
                    'Found deprecated `%(new)s` in settings. Modify %(new)s '
                    'to %(old)s in your settings and theme for the same '
                    'behavior. Temporarily setting %(old)s for backwards '
                    'compatibility.',
                    {'new': new, 'old': old}
                )
                self.settings[old] = self.settings[new]


def get_settings():
    config_file = None
    if config_file is None and os.path.isfile(DEFAULT_CONFIG_NAME):
        config_file = DEFAULT_CONFIG_NAME

    settings = read_settings(config_file)

    return settings


def main():
    # 方便调试配置一些参数
    logger.debug(f'Pelican version: {__version__}')
    logger.debug(f'Python version: {sys.version.split()[0]}')

    try:
        settings = get_settings()

        logger.debug(f'settings: {settings}')

        readers = Readers(settings)
        reader_descs = sorted(set(['%s (%s)' %
                                   (type(r).__name__,
                                    ', '.join(r.file_extensions))
                                   for r in readers.readers.values()
                                   if r.enabled]))

        print(reader_descs)

        res = readers.read_file('.', 'test.md')
        print(res)
        print(res.settings)
        print(res.metadata)
        print(res.content)

    except Exception as e:
        logger.critical('%s', e)
