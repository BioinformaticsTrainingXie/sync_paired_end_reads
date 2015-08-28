from setuptools import setup

setup(
    name='sync_paired_end_reads',
    version='1.0',
    packages=['sync_paired_end_reads'],
    url='',
    license='GPL 2.0',
    author='mickael',
    author_email='mendez.mickael@gmail.com',
    description='Synchronises paired-end reads when either read1 or read2 was modified but not both,',

    entry_points={'console_scripts': ['syncpairs=sync_paired_end_reads.syncpairs:main'],
                  }
)

