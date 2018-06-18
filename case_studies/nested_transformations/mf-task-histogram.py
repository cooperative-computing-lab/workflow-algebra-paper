import sys
import json
import os

interval = 5

if __name__ == '__main__':
	cdf = None
	gnu = None
	if len(sys.argv) < 2:
		print("Please provide input from wqlog.tr")
		sys.exit(1)
#	if len(sys.argv) == 3:
#		cdf = open(sys.argv[2],'w+')
	if len(sys.argv) == 3:
		gnu = open(sys.argv[2],'w+')
	infile = open(sys.argv[1],'r')
	tasks = {}
	for line in infile:
		if '#' in line:
			continue
		sline = line.split()
		if len(sline) < 5:
			continue
		if sline[2] == 'WORKER':
			continue
		taskid = sline[3]
		timestamp = long(sline[0])
		state = sline[4]
		if not taskid in tasks:
			tasks[taskid] = {}
		if state == 'RUNNING':
			tasks[taskid]['start'] = timestamp
		if state == 'WAITING_RETRIEVAL':
			tasks[taskid]['end'] = timestamp
	infile.close()
	longest = 0
	for t in tasks:
		if tasks[t]['end'] - tasks[t]['start'] > longest:
			longest =  tasks[t]['end'] - tasks[t]['start']
	maxmult = longest//(interval*1000000) + 1
	hist={}
	for x in range(0,maxmult+1):
		hist[x] = 0
	alltimes = []
	for t in tasks:
		time = tasks[t]['end'] - tasks[t]['start']
		for x in range(0,maxmult+1):
			if time < x*interval*1000000:
				hist[x] += 1
				break
		alltimes.append(time)
	dat = []
	for y in hist:
		print("%i %i"%(y*interval,hist[y]))
		dat.append((y*interval, hist[y]))
	#if not cdf == None:
	#	alltimes.sort()
		#dat.sort(key=lambda x: x[0])
	#	msum = 0
		#for y in dat:
	#	for y in alltimes:
	#		datpoint = msum + 1
	#		msum = datpoint
	#		cdf.write("%f %i\n"%(y/(interval*100000.0),datpoint))
	#	cdf.close()
	if not gnu == None:
		for y in hist:
			gnu.write("%i\t%i\n"%(y*interval, hist[y]))
		gnu.close();


