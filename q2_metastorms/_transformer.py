# ----------------------------------------------------------------------------
# Copyright (c) 2018, Meta-Storms development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import shutil

from .plugin_setup import plugin
from q2_metastorms._format import (MetaStormsSearchResultsDirFmt,
                                 MetaStormsDatabaseDirFmt,
                                 MetaStormsMetaResultsDirFmt,
                                 MetaStormsMNSResultsDirFmt)

@plugin.register_transformer
def _1(path: str) -> MetaStormsDatabaseDirFmt:
    ff = MetaStormsDatabaseDirFmt()
    shutil.copy(path, str(ff))
    return ff

@plugin.register_transformer
def _2(path: str) -> MetaStormsSearchResultsDirFmt:
    ff = MetaStormsSearchResultsDirFmt()
    shutil.copy(path, str(ff))
    return ff

@plugin.register_transformer
def _3(path: str) -> MetaStormsMetaResultsDirFmt:
    ff = MetaStormsMetaResultsDirFmt()
    shutil.copy(path, str(ff))
    return ff

@plugin.register_transformer
def _4(path: str) -> MetaStormsMNSResultsDirFmt:
    ff = MetaStormsMNSResultsDirFmt()
    shutil.copy(path, str(ff))
    return ff

