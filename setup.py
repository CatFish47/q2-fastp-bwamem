# Copied and modified from https://github.com/qiime2/q2-cutadapt/blob/master/setup.py

from setuptools import find_packages, setup

import versioneer


setup(
    name='q2-fastp-bwamem',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD-3-Clause',
    packages=find_packages(),
    author='Grant Cheng',
    author_email="gxcheng@ucsd.edu",
    url='https://github.com/CatFish47/q2-fastp-bwamem',
    entry_points={
        'qiime2.plugins':
        ['q2-fastp-bwamem=q2_fastp_bwamem.plugin_setup:plugin']
    },
    package_data={
        'q2_fastp_bwamem': ['citations.bib'],
        'q2_fastp_bwamem.tests': [
            'data/*',
            'data/single-end/*',
            'data/paired-end/*',
            'data/paired-end-unordered/*',
            'data/mixed-orientation/*',
        ],
    },
    zip_safe=False,
)