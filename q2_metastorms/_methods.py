# ----------------------------------------------------------------------------
# Copyright (c) 2018, Meta Storms development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import os
import subprocess
import tempfile
import biom

from qiime2 import Artifact, Metadata
from q2_metastorms._format import (MetaStormsDatabaseDirFmt,
                                   MetaStormsSearchResultsDirFmt)
from q2_metastorms._type import (MetaStormsSearchResults,
                                 MetaStormsDatabase,
                                 MetaStormsMetaResults,
                                 MetaStormsMNSResults)

_default_params = {
        'n_matched' : '10',
        'minimum_similarity' : '0',
        'enable_exhaustive_search' : 'F',
        'if_weighted' : 'T',
        'cpu_core_number' : None,
        'number_predicted' : '1',
        'base_of_similarity' : '0',
        'max_number_matches' : '10',
        'number_of_skipped' : '0'
}

def run_command(cmd, verbose=True):
    if verbose:
        print("Running external command line application. This may print "
              "messages to stdout and/or stderr.")
        print("The command being run is below. This command cannot "
              "be manually re-run as it will depend on temporary files that "
              "no longer exist.")
        print("\nCommand:", end=' ')
        print(" ".join(cmd), end='\n\n')
    subprocess.run(cmd, check=True)


def _build_search_command(table_fname, database_fname, result_fname,
                          n_matched, minimum_similarity, enable_exhaustive_search, 
                          if_weighted, cpu_core_number):
    cmd = ['MetaDB-search', '-T', table_fname, '-d', database_fname, '-o', result_fname, 
            '-n', n_matched, '-m', minimum_similarity, '-e', enable_exhaustive_search,
            '-w', if_weighted]
    if (cpu_core_number):
        cmd += ['-t', cpu_core_number]
    return cmd

def _build_parse_meta_command(query_fname, metadata_fname, result_fname, 
                              number_predicted, base_of_similarity, 
                              max_number_matches, number_of_skipped):
    return ['MetaDB-parse-meta', '-i', query_fname, '-m', metadata_fname,
            '-o', result_fname, '-r', number_predicted, '-b', base_of_similarity,
            '-n', max_number_matches, '-s', number_of_skipped]

def _build_parse_mns_command(query_fname, result_fname, base_of_similarity, 
                             max_number_matches, number_of_skipped):
    return ['MetaDB-parse-mns', '-i', query_fname,
            '-o', result_fname, '-b', base_of_similarity,
            '-n', max_number_matches, '-s', number_of_skipped]

def _build_make_command(input_otu_table, output_database_name):
    return ['MetaDB-make', '-T', input_otu_table, '-o', output_database_name]


def _write_counts_table(table_fname, table):
    out = open(table_fname, 'w')
    out.write('SampleID\t')
    # out.write('\t'.join(table.ids()))
    out.write('\t'.join(table.ids(axis='observation')))
    out.write('\n')

    for values, id_, _ in table.iter(dense=True):
        out.write(id_)
        out.write('\t')
        # out.write('\t'.join(map(str, ids)))
        out.write('\t'.join(map(str, values)))
        out.write('\n')
    out.close()


def search(database: MetaStormsDatabaseDirFmt, table: biom.Table,
           n_matched: str = _default_params['n_matched'],
           minimum_similarity: str = _default_params['minimum_similarity'],
           enable_exhaustive_search: str = _default_params['enable_exhaustive_search'],
           if_weighted: str = _default_params['if_weighted'],
           cpu_core_number: str = _default_params['cpu_core_number']) -> str:
    tmpdir = tempfile.mkdtemp()
    table_fname = os.path.join(tmpdir, 'table.counts')
    result_fname = os.path.join(tmpdir, 'query.out')
    db_path = os.path.join(str(database), 'database.mdb')
    _write_counts_table(table_fname, table)
    run_command(_build_search_command(table_fname, db_path, result_fname, 
                n_matched, minimum_similarity, enable_exhaustive_search, if_weighted, cpu_core_number))
    return result_fname


def make(table: biom.Table) -> str:
    tmpdir = tempfile.mkdtemp()
    table_fname = os.path.join(tmpdir, 'table.counts')
    result_fname = os.path.join(tmpdir, 'database')
    _write_counts_table(table_fname, table)
    run_command(_build_make_command(table_fname, result_fname))
    return result_fname + '.mdb'


def parse_meta(query_results: MetaStormsSearchResultsDirFmt,
               metadata: Metadata, 
               number_predicted: str = _default_params['number_predicted'], 
               base_of_similarity: str = _default_params['base_of_similarity'], 
               max_number_matches: str = _default_params['max_number_matches'], 
               number_of_skipped: str = _default_params['number_of_skipped']) -> str:
    tmpdir = tempfile.mkdtemp()
    qr_path = os.path.join(str(query_results), 'query.out')
    result_fname = os.path.join(tmpdir, 'query.out.meta')
    md_fname = os.path.join(tmpdir, 'metadata.tsv')
    metadata.to_dataframe().to_csv(md_fname, sep='\t', index=True, header=True)
    run_command(_build_parse_meta_command(qr_path, md_fname,
                                          result_fname, number_predicted, base_of_similarity, 
                                          max_number_matches, number_of_skipped))
    return result_fname


def parse_mns(query_results: MetaStormsSearchResultsDirFmt,
              base_of_similarity: str = _default_params['base_of_similarity'], 
              max_number_matches: str = _default_params['max_number_matches'], 
              number_of_skipped: str = _default_params['number_of_skipped']) -> str:
    tmpdir = tempfile.mkdtemp()
    qr_path = os.path.join(str(query_results), 'query.out')
    result_fname = os.path.join(tmpdir, 'query.out.mns')
    run_command(_build_parse_mns_command(qr_path, result_fname, base_of_similarity, 
                                         max_number_matches, number_of_skipped))
    return result_fname

