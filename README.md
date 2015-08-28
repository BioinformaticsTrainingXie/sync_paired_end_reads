#sync_paired_end_reads

sync_paired_end_reads is a python tool to synchronise paired-end reads when reads1 or reads2 were modified.

When working with paired-end sequencing data, it is common to filter out reads that do not pass the quality control.
This lead to pairs that are not synced anymore. This tool streams reads1 and search for the associated read2 in reads2.
Additionally  it synchronises the sequence identifiers of the reads so if a software modified the sequence identifier of
the reads1 then same identifiers will be used in reads2. Finally it replaces all space characters by an arbitrary '___' pattern. 

This tool was mainly developed to process the output of tagdust2 when ran in single-end mode 
which appends the UMIs found in the raw sequences to the sequence identifier. 
 
## Install

run tthe following command from the sync_paired_end_reads directory:
`python setup.py install`

This step will install the command line tool 'syncpairs' and add it to the PATH.

## How to use

from the command line type:

`syncpairs MY_READS1 MY_READS2 OUTPUT_READS1 OUTPUT_READS2`
 
