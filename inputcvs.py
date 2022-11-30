#!/usr/bin/python
class inputcvs:
	value=[];
	Rvalue="";
	separator=",";
	def adds(inputcvss,texts):
		inputcvss.value=inputcvss.value+[texts];
	def reportwasks(inputcvss):
		print(inputcvss.value);
	def inputs(inputcvss):
		s="";
		ss="";
		n=0;
		nn=len(inputcvss.value);
		nnn=range(0,nn);
		for n in nnn:
			print(inputcvss.value[n]+":?");
			ss=raw_input();
			s=s+ss;
			if n<nn-1:
				s=s+inputcvss.separator;
		return s;

	
b=0;
print("\033c\033[42;30m\n");
inputcvs0=inputcvs();
inputcvs0.adds("date");
inputcvs0.adds("ref");
inputcvs0.adds("ref2");
inputcvs0.adds("values");
print(inputcvs0.inputs());