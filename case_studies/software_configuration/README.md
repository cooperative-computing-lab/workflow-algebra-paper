This directory outlines the software configuration case study.

This relies on the following software to be install and in your PATH:\
Makeflow : https://github.com/cooperative-computing-lab/cctools.git\
Work Queue : https://github.com/cooperative-computing-lab/cctools.git\
VC3-Builder : https://github.com/vc3-project/vc3-builder.git

This workflow is configured to run a simple `maker -v` command to verify that 
MAKER was installed and configured correctly.

As mentioned in the paper, there are several restricted packages that are
needed to install and configure MAKER. Information on where and how to get
these packages is provided by VC3-Builder when attempting to install MAKER.

The build used for this paper required these packages:\
trf409 at https://tandem.bu.edu/trf/trf.html\
repeatmaskerlibraries-LATEST.tar.gz at http://www.girinst.org\
maker-2.31.8.tgz at http://www.yandell-lab.org/software/maker.html

The downloaded files were tarred into `manual-distribution.tar.gz`

This workflow is configured for Work Queue, but can be changed in the Makefile for local
execution. 

To run workers you can either:
Start a local worker:
`work_queue_worker -N vc3-dist --cores 8`
-- or --
Run a worker factory:
Local: `work_queue_factory -T slurm -w0 -W1 -N vc3-dist`
SLURM(Stampede2): `work_queue_factory -T slurm -w0 -W1 -N vc3-dist -B "-p development -N 1 -n 1 -t 00:30:00" -E "--cores 8"`
SLURM(Comet)    : `work_queue_factory -T slurm -w0 -W1 -N vc3-dist -B "--partition=debug --nodes=1 --ntasks-per-node=1 -t 00:30:00 --wait=0" -E "--cores 8"`
HTCondor(ND): `work_queue_factory -T condor -w0 -W1 -N vc3-dist --cores 8`
SGE(CRC.ND) : `work_queue_factory -T sge -w0 -W1 -N vc3-dist -B "-pe smp 8" -E "--cores 8"`

