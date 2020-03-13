# ----------------------------------------------------------------------------
# Copyright (c) 2020, Meta-Storms development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

import qiime2.plugin
from q2_types.feature_table import FeatureTable, Frequency

import q2_metastorms
from q2_metastorms._type import (MetaStormsOTUDatabase,
                                 MetaStormsSPDatabase,
                                 MetaStormsFUNCDatabase,
                                 MetaStormsSearchResults,
                                 MetaStormsMetaResults,
                                 MetaStormsMNSResults)
from q2_metastorms._format import (MetaStormsOTUDatabaseFmt,
                                   MetaStormsOTUDatabaseDirFmt,
                                   MetaStormsSPDatabaseFmt,
                                   MetaStormsSPDatabaseDirFmt,
                                   MetaStormsFUNCDatabaseFmt,
                                   MetaStormsFUNCDatabaseDirFmt,
                                   MetaStormsSearchResultsFmt,
                                   MetaStormsSearchResultsDirFmt,
                                   MetaStormsMetaResultsFmt,
                                   MetaStormsMetaResultsDirFmt,
                                   MetaStormsMNSResultsFmt,
                                   MetaStormsMNSResultsDirFmt)

plugin = qiime2.plugin.Plugin(
    name='metastorms',
    version='std 2.2.1',
    website='https://github.com/qibebt-bioinfo/q2-metastorms',
    package='q2_metastorms',
    citations=qiime2.plugin.Citations.load('citations.bib', package='q2_metastorms'),
    description='This QIIME 2 plugin supports standalone implementation of '
                'Microbiome Search Engine (MSE; http://mse.single-cell.cn).',
    short_description='Plugin for search in a micriobiome database.'
)

plugin.register_formats(MetaStormsOTUDatabaseFmt,
                        MetaStormsOTUDatabaseDirFmt)
plugin.register_formats(MetaStormsSPDatabaseFmt,
                        MetaStormsSPDatabaseDirFmt)
plugin.register_formats(MetaStormsFUNCDatabaseFmt,
                        MetaStormsFUNCDatabaseDirFmt)
plugin.register_formats(MetaStormsSearchResultsFmt,
                        MetaStormsSearchResultsDirFmt)
plugin.register_formats(MetaStormsMetaResultsFmt,
                        MetaStormsMetaResultsDirFmt)
plugin.register_formats(MetaStormsMNSResultsFmt,
                        MetaStormsMNSResultsDirFmt)

plugin.register_semantic_types(MetaStormsOTUDatabase)
plugin.register_semantic_type_to_format(
    MetaStormsOTUDatabase,
    artifact_format=MetaStormsOTUDatabaseDirFmt)

plugin.register_semantic_types(MetaStormsSPDatabase)
plugin.register_semantic_type_to_format(
    MetaStormsSPDatabase,
    artifact_format=MetaStormsSPDatabaseDirFmt)

plugin.register_semantic_types(MetaStormsFUNCDatabase)
plugin.register_semantic_type_to_format(
    MetaStormsFUNCDatabase,
    artifact_format=MetaStormsFUNCDatabaseDirFmt)

plugin.register_semantic_types(MetaStormsSearchResults)
plugin.register_semantic_type_to_format(
    MetaStormsSearchResults,
    artifact_format=MetaStormsSearchResultsDirFmt)

plugin.register_semantic_types(MetaStormsMetaResults)
plugin.register_semantic_type_to_format(
    MetaStormsMetaResults,
    artifact_format=MetaStormsMetaResultsDirFmt)

plugin.register_semantic_types(MetaStormsMNSResults)
plugin.register_semantic_type_to_format(
    MetaStormsMNSResults,
    artifact_format=MetaStormsMNSResultsDirFmt)

plugin.register_semantic_types(MetaStormsMASResults)
plugin.register_semantic_type_to_format(
    MetaStormsMASResults,
    artifact_format=MetaStormsMASResultsDirFmt)

plugin.methods.register_function(
    function=q2_metastorms.search_otu,
    inputs={'database': MetaStormsOTUDatabase,
            'table': FeatureTable[Frequency]},
    parameters={
            'n_matched' : qiime2.plugin.Str,
            'minimum_similarity' : qiime2.plugin.Str,
            'enable_exhaustive_search' : qiime2.plugin.Str,
            'if_weighted' : qiime2.plugin.Str,
            'cpu_core_number' : qiime2.plugin.Str
    },
    outputs=[
        ('results', MetaStormsSearchResults),
    ],
    input_descriptions={
        'database': 'A MetaStorms database based on OTU',
        'table': 'The table of query samples',
    },
    parameter_descriptions={
        'n_matched' : 'Number of the matched sample(s), default is 10',
        'minimum_similarity' : 'Minimum similarity of the matched sample(s), range (0.0 ~ 1.0], default is 0',
        'enable_exhaustive_search' : 'If enable the exhaustive search (low speed), T(rue) or F(alse), default is F',
        'if_weighted' : 'Abundance weighted or unweighted, T(rue) or F(alse), default is T',
        'cpu_core_number' : 'CPU core number, default is auto',
    },
    output_descriptions={
        'results': 'MetaStorms results',
    },
    name='Search for similar microbiomes from OTU database',
    description='Search for similar microbiomes from OTU database'
)

plugin.methods.register_function(
    function=q2_metastorms.search_sp,
    inputs={'database': MetaStormsSPDatabase,
            'table': FeatureTable[Frequency]},
    parameters={
            'n_matched' : qiime2.plugin.Str,
            'minimum_similarity' : qiime2.plugin.Str,
            'enable_exhaustive_search' : qiime2.plugin.Str,
            'if_weighted' : qiime2.plugin.Str,
            'cpu_core_number' : qiime2.plugin.Str
    },
    outputs=[
        ('results', MetaStormsSearchResults),
    ],
    input_descriptions={
        'database': 'A MetaStorms database',
        'table': 'The table of query samples',
    },
    parameter_descriptions={
        'n_matched' : 'Number of the matched sample(s), default is 10',
        'minimum_similarity' : 'Minimum similarity of the matched sample(s), range (0.0 ~ 1.0], default is 0',
        'enable_exhaustive_search' : 'If enable the exhaustive search (low speed), T(rue) or F(alse), default is F',
        'if_weighted' : 'Abundance weighted or unweighted, T(rue) or F(alse), default is T',
        'cpu_core_number' : 'CPU core number, default is auto',
    },
    output_descriptions={
        'results': 'MetaStorms results',
    },
    name='Search for similar microbiomes from Species database',
    description='Search for similar microbiomes from Species database'
)

plugin.methods.register_function(
    function=q2_metastorms.search_func,
    inputs={'database': MetaStormsFUNCDatabase,
            'table': FeatureTable[Frequency]},
    parameters={
            'n_matched' : qiime2.plugin.Str,
            'minimum_similarity' : qiime2.plugin.Str,
            'enable_exhaustive_search' : qiime2.plugin.Str,
            'if_weighted' : qiime2.plugin.Str,
            'cpu_core_number' : qiime2.plugin.Str
    },
    outputs=[
        ('results', MetaStormsSearchResults),
    ],
    input_descriptions={
        'database': 'A MetaStorms database',
        'table': 'The table of query samples',
    },
    parameter_descriptions={
        'n_matched' : 'Number of the matched sample(s), default is 10',
        'minimum_similarity' : 'Minimum similarity of the matched sample(s), range (0.0 ~ 1.0], default is 0',
        'enable_exhaustive_search' : 'If enable the exhaustive search (low speed), T(rue) or F(alse), default is F',
        'if_weighted' : 'Abundance weighted or unweighted, T(rue) or F(alse), default is T',
        'cpu_core_number' : 'CPU core number, default is auto',
    },
    output_descriptions={
        'results': 'MetaStorms results',
    },
    name='Search for similar microbiomes from KO database',
    description='Search for similar microbiomes from KO database'
)

plugin.methods.register_function(
    function=q2_metastorms.make_otu,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    outputs=[
        ('results', MetaStormsOTUDatabase),
    ],
    input_descriptions={
        'table': 'The table of subject samples',
    },
    parameter_descriptions={},
    output_descriptions={
        'results': 'MetaStorms database',
    },
    name='Make a Meta-Storms database by OTU table',
    description='Make a Meta-Storms database by OTU table'
)

plugin.methods.register_function(
    function=q2_metastorms.make_sp,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    outputs=[
        ('results', MetaStormsSPDatabase),
    ],
    input_descriptions={
        'table': 'The table of subject samples',
    },
    parameter_descriptions={},
    output_descriptions={
        'results': 'MetaStorms database',
    },
    name='Make a Meta-Storms database by Species table',
    description='Make a Meta-Storms database by Species table'
)

plugin.methods.register_function(
    function=q2_metastorms.make_func,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    outputs=[
        ('results', MetaStormsFUNCDatabase),
    ],
    input_descriptions={
        'table': 'The table of subject samples',
    },
    parameter_descriptions={},
    output_descriptions={
        'results': 'MetaStorms database',
    },
    name='Make a Meta-Storms database by KO table',
    description='Make a Meta-Storms database by KO table'
)

plugin.methods.register_function(
    function=q2_metastorms.parse_meta,
    inputs={'query_results': MetaStormsSearchResults},
    parameters={
            'metadata': qiime2.plugin.Metadata,
            'number_predicted' : qiime2.plugin.Str,
            'base_of_similarity' : qiime2.plugin.Str,
            'max_number_matches' : qiime2.plugin.Str,
            'number_of_skipped' : qiime2.plugin.Str,
    },
    outputs=[
        ('results', MetaStormsMetaResults),
    ],
    input_descriptions={
        'query_results': 'Results from a metaastorms search'
    },
    parameter_descriptions={
        'metadata': 'The sample metadata.',
        'number_predicted' : 'Number of predictd meta-data, default is 1',
        'base_of_similarity' : 'Base of the similarity in the input file, default is 0',
        'max_number_matches' : 'Max number of matches in the input file, default is 10',
        'number_of_skipped' : '-s Number of skipped matches in the input file, default is 0'
    },
    output_descriptions={
        'results': 'The observed samples',
    },
    name='Meta-data prediction by search results',
    description='Meta-data prediction by search results'
)


plugin.methods.register_function(
    function=q2_metastorms.parse_mns,
    inputs={'query_results': MetaStormsSearchResults},
    parameters={
            'base_of_similarity' : qiime2.plugin.Str,
            'max_number_matches' : qiime2.plugin.Str,
            'number_of_skipped' : qiime2.plugin.Str,
    },
    outputs=[
        ('results', MetaStormsMNSResults),
    ],
    input_descriptions={
        'query_results': 'Results from a metaastorms search',
    },
    parameter_descriptions={
        'base_of_similarity' : 'Base of the similarity in the input file, default is 0',
        'max_number_matches' : 'Max number of matches in the input file, default is 10',
        'number_of_skipped' : '-s Number of skipped matches in the input file, default is 0'
    },
    output_descriptions={
        'results': 'The observed samples',
    },
    name='MNS (Microbiome Novelty Score) calculation by search results',
    description='MNS (Microbiome Novelty Score) calculation by search results'
)


importlib.import_module('q2_metastorms._transformer')
