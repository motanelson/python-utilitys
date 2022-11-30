#!/usr/bin/python
class menus():
	values="0=Exit\n";
	returnsep="\n";
	def adds(menuss,valuess):
		menuss.values=menuss.values+valuess+menuss.returnsep;
	def clears(menuss):
		menuss.values="0=Exit\n";
	def report(menuss):
		print(menuss.values);
		try: 
			return input();
		except:
			return 0;
b=0;
print("\033c\033[42;30m\n");
menu0=menus();
menu0.adds("1=hello world");
menu0.adds("2=hi");
menu0.adds("1=there");
print (menu0.report())
