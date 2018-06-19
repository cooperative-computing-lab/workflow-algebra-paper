
DEF_LIMIT=20

all : result_${DEF_LIMIT}.tar.gz


B_OPTS=-T wq -N vc3-dist -p 9050
#B_OPTS=-T local
D_OPTS=-d all -o mf_vc3.dbg -g ref_cnt

vc3-builder : 
	cp `which vc3-builder` ./

mf_%.done : vc3-builder vc3-builder.jx vc3-builder.mf
	echo $* > limit.conf
	makeflow ${B_OPTS} -L wq_$*.log -l mf_$*.log ${D_OPTS} --jx vc3-builder.mf --wrapper vc3-builder.jx --jx-define="LIMIT"=$*

mf_%.exe_info : mf_%.done wq_task_exe.py
	python wq_task_exe.py wq_$*.log.tr $@

result_%.tar.gz : mf_%.exe_info
	mkdir -p result_$*
	mv builder_*.log result_$*
	cp wq_$*.log result_$*
	cp wq_$*.log.tr result_$*
	cp mf_$*.log result_$*
	cp mf_$*.exe_info result_$*
	cp mf_*.dbg result_$*
	tar czf $@ result_$**

clean : 
	rm -f builder_*.log  t_*.sh
	rm -f mf_*.log mf_*.dbg wq_*.log
	makeflow -c --jx vc3-builder.mf --jx-define="LIMIT"=`cat limit.conf`

