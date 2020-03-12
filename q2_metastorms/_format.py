# ----------------------------------------------------------------------------
# Copyright (c) 2018, Meta-Storms development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin.model as model


class MetaStormsOTUDatabaseFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


class MetaStormsSPDatabaseFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


class MetaStormsFUNCDatabaseFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


class MetaStormsSearchResultsFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


class MetaStormsMetaResultsFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


class MetaStormsMNSResultsFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


class MetaStormsMASResultsFmt(model.TextFileFormat):
    def sniff(self):
        # Not sure what should be done to validate the contents
        return True


MetaStormsOTUDatabaseDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsOTUDatabaseDirFmt', 'database.mdb', MetaStormsOTUDatabaseFmt)
MetaStormsSPDatabaseDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsSPDatabaseDirFmt', 'database.mdbs', MetaStormsSPDatabaseFmt)
MetaStormsFUNCDatabaseDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsFUNCDatabaseDirFmt', 'database.mdbf', MetaStormsFUNCDatabaseFmt)
MetaStormsSearchResultsDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsSearchResultsDirFmt', 'query.out', MetaStormsSearchResultsFmt)
MetaStormsMetaResultsDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsMetaResultsDirFmt', 'query.out.meta', MetaStormsMetaResultsFmt)
MetaStormsMNSResultsDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsMNSResultsDirFmt', 'query.out.mns', MetaStormsMNSResultsFmt)
MetaStormsMASResultsDirFmt = model.SingleFileDirectoryFormat(
    'MetaStormsMASResultsDirFmt', 'query.out.mns', MetaStormsMASResultsFmt)
