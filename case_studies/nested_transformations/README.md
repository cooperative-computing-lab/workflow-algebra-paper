This directory outlines the nested transformations case study.

This relies on the following software to be install and in your PATH:\
Makeflow : https://github.com/cooperative-computing-lab/cctools.git
Resource Monitor : https://github.com/cooperative-computing-lab/cctools.git
Makeflow-Examples : git@github.com:cooperative-computing-lab/makeflow-examples.git

The instructions outlined in Makeflow-Examples:BWA clarify how to install BWA
and the general design of the workflow.

This can be accerlated using Work Queue, though it is not required.
The default is local.

The workflow will run all 4 configuration by default, each in a 
separate directory, compile the figure used in the paper, and then
tarball the results.

The scale used for the paper used these values:
`
REF_LENGTH=100000
REF_WIDTH =1000

QUE_LENGTH=300000
QUE_MATCH =500

NUM_SEQ   =5000
`

Smaller values are here for default as example.
