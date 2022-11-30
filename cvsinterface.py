#!/usr/bin/python
class cvss:
	value="";
	valueA=[];
	linesep="\n";
	linecounts=0;
	def clears(cvss):
		cvss.valueA=[];
		cvss.linecounts=0;
	def adds(cvss,lines):
		cvss.valueA=cvss.valueA+[lines];
		cvss.linecounts=len(cvss.valueA);
	def setcvs(cvss,texts):
		cvss.valueA=texts.split(cvss.linesep);
		cvss.linecounts=len(cvss.valueA);
		return cvss.valueA;
	def getlinecount(cvss):
		cvss.linecounts=len(cvss.valueA);
		return cvss.linecounts;
	def getlines(cvss,indexs):
		if indexs<cvss.linecounts and indexs>-1:
			return cvss.valueA[indexs];
	def getcvs(cvss):
		n=0;
		cvss.value="";
		nn=range(0,cvss.linecounts);
		for n in nn:
			cvss.value=cvss.value+cvss.valueA[n]+cvss.linesep;
		return cvss.value;
	def report(cvss):
		n=0;
		nn=range(0,cvss.linecounts);
		for n in nn:
			print(cvss.valueA[n]);

b=0;
print("\033c\033[42;30m\n");
cvs0=cvss();
cvs0.setcvs("0,1,2,3\n4,5,6,7\n8,9,10,11");
n=0;
cvs0.adds("9,8,7,6");
print (cvs0.getcvs());
