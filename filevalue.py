#!/usr/bin/python
class filesvalues:
	names="";
	ext=".txt";
	value="";
	def setname(files,Tnames):
		files.names=Tnames;
	def setext(files,Tnames):
		files.ext=Tnames;
	def setvalue(files,Tnames):
		files.value=Tnames;
	def getname(files):
		return files.names;
	def getext(files):
		return files.ext;
	def getvalue(files):
		return files.value;
	def checks(files):
		try:
			f=open(files.names+files.ext,"r");
			f.close()
		except:
			files.saves();
		files.loads();
	def saves(files):
		f=open(files.names+files.ext,"w+");
		f.write(files.value);
		f.close();
	def loads(files):
		f=open(files.names+files.ext,"r");	
		files.value=f.read()
		f.close();
b=0;
filesvalues0=filesvalues();
print("\033c\033[42;30m\n");
filesvalues0.setvalue("new file");
filesvalues0.setname("my");
print(filesvalues0.getname());
filesvalues0.setext(".tx");
print(filesvalues0.getext());
print(filesvalues0.getvalue())
filesvalues0.checks();
print(filesvalues0.getvalue());
filesvalues0.setvalue("old file");
filesvalues0.saves();
filesvalues0.loads();
print(filesvalues0.getvalue());