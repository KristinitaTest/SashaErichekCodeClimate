# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 07:23:52
# @Last Modified time: 2018-01-22 18:45:58
"""Check files for body.

Check, contains files of directory <body> or no.
"""
import logbook

import os

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from pyfancy.pyfancy import pyfancy

from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS


LOG = logbook.Logger("eric_body logbook")

BODY_EXIST = True


def eric_body_function():
    """Check, contains body in a file, or no."""
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename in ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS:

        filename_without_path = os.path.basename(filename)

        # Check if string in a file
        # https://stackoverflow.com/a/4944929/5951529
        # Encoding for Travis CI, see
        # https://stackoverflow.com/a/31492722/5951529
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354674238
        # https://github.com/travis-ci/travis-ci/issues/8993#issuecomment-354681085
        if "<body>" in open(filename, encoding='windows-1251').read():
            LOG.debug(filename_without_path + " contains <body>")

        else:
            LOG.error(pyfancy().red().bold(
                "File " +
                filename_without_path +
                " not contain <body>. Please, add <body> in " +
                filename_without_path +
                "."))
            global BODY_EXIST
            BODY_EXIST = False


def eric_body_summary():
    """Report, contains <body> in all files or no.

    Use flags, see https://stackoverflow.com/a/48052480/5951529
    """
    eric_body_function()
    if BODY_EXIST:
        LOG.notice(pyfancy().green().bold(
            "All files contains <body>"))

    if not BODY_EXIST:
        LOG.error(pyfancy().red().bold(
            "Not all files contains <body>. Please, correct it."))
