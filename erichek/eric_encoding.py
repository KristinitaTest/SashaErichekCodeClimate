# -*- coding: utf-8 -*-
# @Author: SashaChernykh
# @Date: 2018-01-22 18:30:38
# @Last Modified time: 2018-01-22 19:34:01
"""Encoding checker.

Check, that files in Windows-1251 encoding.

Bugs:
    1. if no Cyrillic symbols in a file, chardet detect file encoding as ASCII;
    2. chardet can detect Windows-1251 as MacCyrillic.
"""
import chardet
import codecs
import logbook
import os

# Do not use «from <module> import *»
# http://bit.ly/2CuW5GS
from pyfancy.pyfancy import pyfancy
from erichek.eric_config import ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS

LOG = logbook.Logger("eric_encoding logbook")


# Flags, see https://www.computerhope.com/jargon/f/flag.htm
# https://stackoverflow.com/a/48052480/5951529
ENCODING_WINDOWS_1251 = True


def eric_encoding_function():
    # Get list all filenames in a directory
    # https://stackoverflow.com/a/1120736/5951529
    for filename in ALL_TXT_IN_ERIC_ROOM_WIHTOUT_SUBFOLDERS:

        filename_without_path = os.path.basename(filename)

        # Not 100%, see https://stackoverflow.com/a/436299/5951529
        # Can doesn't work for Latin packages
        # Check decoding — http://bit.ly/2C3xSUD
        # https://stackoverflow.com/a/37531241/5951529
        rawdata = open(filename, "rb").read()
        chardet_data = chardet.detect(rawdata)
        # Python dictionary
        fileencoding = (chardet_data['encoding'])
        chardet_confidence = (chardet_data['confidence'])

        # Needs MacCyrillic, because chardet can check Windows-1251
        # as MacCyrillic
        if fileencoding == 'windows-1251':
            LOG.debug(filename_without_path + " in windows-1251 encoding")
        # Integer to string:
        # https://stackoverflow.com/a/961638/5951529
        elif fileencoding == 'MacCyrillic':
            LOG.info(pyfancy().green("Encoding of file " + filename_without_path +
                                     " chardet detect as MacCyrillic with confidence " +
                                     str(chardet_confidence)))
        else:
            # Convert file from UTF-8 to Cyrillic 1251
            # https://stackoverflow.com/q/19932116/5951529
            with codecs.open(filename, "r", "utf-8") as file_for_conversion:
                read_file_for_conversion = file_for_conversion.read()
            with codecs.open(filename, "w", "windows-1251") as file_for_conversion:
                if read_file_for_conversion:
                    file_for_conversion.write(read_file_for_conversion)
            LOG.critical(pyfancy().red_bg().bold(filename_without_path +
                                                 " in " +
                                                 fileencoding +
                                                 ", not in Windows-1251 encoding! Please, save " +
                                                 filename_without_path + " in Windows-1251 encoding."))
            LOG.notice(pyfancy().green().bold("If encoding of file " + filename_without_path +
                                              " is UTF-8 and you see message above in local wwtd testing, " +
                                              filename_without_path +
                                              " automatically will converted from UTF-8 to Windows-1251."))
            global ENCODING_WINDOWS_1251
            ENCODING_WINDOWS_1251 = False


def eric_encoding_summary():
    eric_encoding_function()
    if ENCODING_WINDOWS_1251:
        LOG.notice(pyfancy().green().bold("All files in Windows-1251 encoding"))

    if not ENCODING_WINDOWS_1251:
        LOG.critical(pyfancy().red_bg().bold(
            "One or more your files not in Windows-1251 encoding. Please, convert it (them) to Windows-1251."))
