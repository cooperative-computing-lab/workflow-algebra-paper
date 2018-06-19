
all : result.dat

result.dat : result_10.dat result_100.dat result_1000.dat result_10000.dat
	cat $? > $@

div_by_0 : div_by_0.c
	gcc div_by_0.c -o div_by_0 -ggdb

core_result_% : div_by_0 core_dump.mf
	makeflow --jx core_dump.mf --wrapper stacktrace.jx --jx-define="LIMIT"=$* -g ref_cnt
	echo $* > limit.conf

result_%.dat : core_result_% core_dump_size.pl
	cat ls*.dat > complete.out
	rm -rf ls*.dat
	perl core_dump_size.pl complete.out result_$*.dat $*

clean : 
	makeflow -c --jx core_dump.mf --jx-define="LIMIT"=`cat limit.conf`
	rm -f core_result* div_by_0 complete.out

