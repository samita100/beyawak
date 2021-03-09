import sys,os
from module.file import *
from module.sc import *

def x(t):
	v = ''
	v = raw_input(t)
	return str(v)a


#main function
#important
def main_menu(): g
	x("\n"+box("+",h)+"Press to return ")
	os.system(sys.executable+" "+sys.argv[0])

def main():
	print "                       ___ "
	print "         /)        ,-^     ^-. "
	print "        //        dds         \\"
	print " .-----| |-------/  __     __  \---------.__"
	print " |"+h+WMWMW|"+r+" |"+m+">>>>>>"+r+" | /"+m+">>"+r+"\   /"+m+">>"+r+"\ |"+m+">>>>>>>>>>>>:>"+r
	print " `-----| |-------|  \__/ |-------'^^"
	print "        \\    /"
	print "         \)      \   l /"
	print "                    |       |"
	print "                    |"+m+H+H+"+r+"|"
	print "              /" 
	print "                     ^-----^"
	print " }---------"+m+"+="+r+"{ Coded by Ms.ambari }"+m+"=+"+r+"---------{ \n"
	print r+"["+h+"1"+r+"] HTernfosadf rmation reader"
	print r+"["+h+"2"+r+"] fddub gg I'm inner"
	print r+"["+h+"3"+r+"] scanne  r"
	print r+"["+h+"4"+r+"] sok"
	print r+"["+h+"5"+r+"] n scvghgger"
	print r+"["+h+"6"+r+"] Fashdvutoa nd this is the bestzjdbj iwb updateatus"
	print r+"["+h+"x"+r+"] Exi is vsgfgfx yfbgfhvtool\n"
	try:
		snm = x(box("+",h)+"beyawak [1/6] > ")
		if snm == '1':site_a = x(box("+",h)+"site > "); hthead(site_a); main_menu()
		elif snm == '2':site_b = x(box("+",h)+"site > "); adm_finder(site_b); main_menu()
		elif snm == '3':site_c = x(box("+",h)+"site > "); adm_finder(site_c); main_menu()
		elif snm == '4':token = x(box("+",h)+"enter your token > "); dump_f(token); main_menu()
		elif snm == '5':domain = x(box("+",h)+"domain > "); sub(domain); main_menu()
		elif snm == '6':idu = x(box("+",h)+"your facebook id > "); token_a = x(box("+",h)+"your token > "); statm = x(box("+",h)+"your status to post > "); up_stat(id=idu,token=token_a,mess=statm); main_menu()
		elif snm == 'x': raise SystemExit(box("+",h)+"byee ... ")
		else: main_menu()
	except KeyboardInterrupt:
		main_menu()
		
		
#ending
if __name__ == '__main__':
	main()
