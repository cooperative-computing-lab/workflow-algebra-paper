This directory outlines the failure analysis case study.

This relies on the following software to be install and in your PATH:\
Makeflow : https://github.com/cooperative-computing-lab/cctools.git

`div_by_0.c` is code that allocates 1MB of memory and fails depending on the input number.

`make` will compile `div_by_0` and run a makeflow at several predefined number of tasks: 10, 100, 1000, 10000

This will produce result_SIZE.dat files that are concatenated into a single result.dat,
which was used to produce the table in the paper.

Note, this provided transformation is similar to what was defined in the paper, 
but instead of sending either the stack trace or core-dump, we send the information
provided by `ls -l` on the files' sizes.

