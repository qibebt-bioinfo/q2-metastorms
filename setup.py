# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, Meta-Storms development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-metastorms",
    packages=find_packages(),
    author="Gongchao Jing",
    author_email="jinggc@qibebt.ac.cn",
    description="Search engine designed to efficiently search a database of microbiome samples and identify similar samples based on phylogenetic relatedness",
    license='BSD-3-Clause',
    url="http://mse.single-cell.cn",
    entry_points={
        'qiime2.plugins': ['q2-type-example=q2_metastorms.plugin_setup:plugin']
    },
    zip_safe=False,
)
