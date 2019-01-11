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
    author="",   #### Please correct the author information
    author_email="",
    description="",
    license='BSD-3-Clause',
    url="na",   ### This should be the URL for MSE or its github page etc etc
    entry_points={
        'qiime2.plugins': ['q2-type-example=q2_metastorms.plugin_setup:plugin']
    },
    zip_safe=False,
)
