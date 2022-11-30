#!/usr/bin/python
import string;
class infosini:
	value="";
	listsA=[];
	listsB=[];
	listlen=0;
	linesep="\n";
	symbollike="="
	def adds(infos,texts,values):
		n=0;
		nn=len(infos.listsA);
		nnn=range(0,nn)
		list1tr=texts.strip();
		for n in nnn:
			if infos.listsA[n]==list1tr:
				infos.listsB[n]=values;
				return;
		infos.listsA=infos.listsA+[list1tr];
		infos.listsB=infos.listsB+[values];
	def finds(infos,texts):
		n=0;
		nn=len(infos.listsA);
		nnn=range(0,nn)
		list1tr=texts.strip();
		for n in nnn:
			if infos.listsA[n]==list1tr:
				return infos.listsB[n];
		return "";
	def clears(infos):
		infos.listsA=[];
		infos.listsB=[];
		infos.listlen=0;
	def setValue(infos,texts):
		infos.listsA=[];
		infos.listsB=[];
		infos.listlen=0;
		n=0;
		nn=0;
		l=0;
		nnn=0;
		nnnn=0;		
		list1=[];
		list2=[];
		list1=texts.split(infos.linesep);
		l=len(list1);
		nn=range(0,l)
		for n in nn:
			list2=list1[n].split(infos.symbollike);
			nnn=len(infos.listsA);
			list2tr=list2[0].strip()
			nnnn=len(list2);
			if list2tr!="":
				infos.listsA=infos.listsA+[list2tr];
				if nnnn>1: 
					infos.listsB=infos.listsB+[list2[1]];
				else:
					listsB=listsB[""];
		infos.listlen=len(infos.listsA);
		list1=[];
		list2=[];
	def getValue(infos):
		values="";
		n=0;
		nn=len(infos.listsA);
		nnn=range(0,nn)
		for n in nnn:
			values=values+infos.listsA[n]+"="+infos.listsB[n]+""+infos.linesep;
		return values;
	def report(infos):
		n=0;
		nn=len(infos.listsA);
		nnn=range(0,nn)
		for n in nnn:
			print(infos.listsA[n]+"="+infos.listsB[n]);
b=0;
print("\033c\033[42;30m\n");
infosini1=infosini();
infosini1.setValue("mem=10k\nfile=my.txt\nmath=9+9");
infosini1.adds(" file ","hello.txt");
infosini1.adds(" txt ","txt.txt");
print(infosini1.getValue());