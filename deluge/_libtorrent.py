# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Andrew Resch <andrewresch@gmail.com>
#
# This file is part of Deluge and is licensed under GNU General Public License 3.0, or later, with
# the additional special exception to link portions of this program with the OpenSSL library.
# See LICENSE for more details.
#

"""
This module is used to handle the importing of libtorrent and also controls
the minimum versions of libtorrent that this version of Deluge supports.

Example:
    >>> from deluge._libtorrent import lt

"""

from deluge.common import VersionSplit, get_version

try:
    import deluge.libtorrent as lt
except ImportError:
    import libtorrent as lt

REQUIRED_VERSION = '1.0.7.0'

if VersionSplit(lt.__version__) < VersionSplit(REQUIRED_VERSION):
    raise ImportError('Deluge %s requires libtorrent >= %s' % (get_version(), REQUIRED_VERSION))
