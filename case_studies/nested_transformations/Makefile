
REF_LENGTH=1000
REF_WIDTH =1000

QUE_LENGTH=1000
QUE_MATCH =100

NUM_SEQ   =100


CORES=1
MEM=1000
DISK=10000

all: result_${REF_LENGTH}_${REF_WIDTH}_${QUE_LENGTH}_${QUE_MATCH}_${NUM_SEQ}.tar

ref.fastq : fastq_generate.pl
	./fastq_generate.pl ${REF_LENGTH} ${REF_WIDTH} > $@	

query.fastq : fastq_generate.pl ref.fastq
	./fastq_generate.pl ${QUE_LENGTH} ${QUE_MATCH} ref.fastq > $@	

ref.fastq.sa : ref.fastq
	./bwa index ref.fastq

resource_monitor :
	cp `which resource_monitor` ./

test% : ref.fastq.sa query.fastq resource_monitor
	mkdir -p $@
	cp bwa bwa.jx bwa-args.jx cat_bwa singularity.jx fastq_reduce resource_monitor* ref.fastq* query.fastq $@/


BATCH=wq 
BATCH=local 
BATCH_OPT=-N bwa_wrapped -p 9050 -L bwa.wq
JX_OPT=--jx-define="SEQ_PER_SPLIT"=${NUM_SEQ} --jx-define="TOTAL_SEQ"=${QUE_LENGTH}
MF_OPT= -d all -o bwa.dbg -g ref_cnt
MF_OUT= > bwa.stdout 2> bwa.stderr

result_1 : test1 
	cd $<; makeflow --jx bwa.jx --jx-args bwa-args.jx ${JX_OPT} -T ${BATCH} ${BATCH_OPT} ${MF_OPT} --wrapper resource_monitor.jx --wrapper singularity.jx ${MF_OUT}
	cd $<; rm query.fastq* ref.fastq*
	touch $@

result_2 : test2
	cd $<; makeflow --jx bwa.jx --jx-args bwa-args.jx ${JX_OPT} -T ${BATCH} ${BATCH_OPT} ${MF_OPT} --wrapper singularity.jx ${MF_OUT}
	cd $<; rm query.fastq* ref.fastq*
	touch $@

result_3 : test3
	cd $<; makeflow --jx bwa.jx --jx-args bwa-args.jx ${JX_OPT} -T ${BATCH} ${BATCH_OPT} ${MF_OPT} --wrapper resource_monitor.jx ${MF_OUT}
	cd $<; rm query.fastq* ref.fastq*
	touch $@

result_4 : test4
	cd $<; makeflow --jx bwa.jx --jx-args bwa-args.jx ${JX_OPT} -T ${BATCH} ${BATCH_OPT} ${MF_OPT} --sandbox ${MF_OUT}
	cd $<; rm query.fastq* ref.fastq*
	touch $@

result_%.dat : result_%
	if [ -s test$*/result_$*.dat ] 
	then
		cd test$*; python ../task-histogram.py bwa.wq.tr ../result_$*.dat
	else
		cd test$*; python ../task-histogram.py bwa.mf    ../result_$*.dat
	fi

%.pdf : result_1.dat result_2.dat result_3.dat result_4.dat %.plg
	gnuplot %.plg > $@


result_${REF_LENGTH}_${REF_WIDTH}_${QUE_LENGTH}_${QUE_MATCH}_${NUM_SEQ}.tar : result_1 result_2 result_3 result_4 histogram_separate.pdf histogram_combined.pdf
	tar -czf $@ test* result*.dat *.pdf

clean : 
	rm -rf test1 test2 test3 test4
	rm -f result_1 result_2 result_3 result_4

clear : 
	rm -rf test1 test2 test3 test4
	rm -f result_1 result_2 result_3 result_4
	rm -rf bwa.mf
	rm query.fastq* ref.fastq*
