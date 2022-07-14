#!/use/bin/evn python3

from zipfile import ZipFile
import sys
import os

argv=False
try:
	if (sys.argv[1]=="-version" or sys.argv[1]=="--version"):
		print("BlackZip - version 2.0")
		argv=True
	else:
		pass
except:
	pass

def print_help():
	print("""
	
     zipfile          :   Specify the zip file.
     password list    :   Specify the password list.
     help             :   Show help.
     quit             :   Exit from the tool.
     --version        :   Display the version of BlackZip.
     --help           :   Show help.
	""")


try:
	if (sys.argv[1]=="-help" or sys.argv[1]=="--help"):
		print_help()
		argv=True
	else:
		pass
except:
	pass

if (argv==True):
	sys.exit()
else:
	pass

os.system("clear")

print("""\033[1;96m


  ____    _                  _        _____  _         
 | __ )  | |   __ _    ___  | | __   |__  / (_)  _ __  
 |  _ \  | |  / _` |  / __| | |/ /     / /  | | | '_ \ 
 | |_) | | | | (_| | | (__  |   <     / /_  | | | |_) |
 |____/  |_|  \__,_|  \___| |_|\_\   /____| |_| | .__/ 
                                                |_|    
                                     BlackHat Thamizhan


\033[0;0m""")

while(True):
	try:
		exit=False
		action=input("\nBlackZip Path (ex:/home/Black.zip) :~ ")
		if(action=="quit"):
			exit=True
			break
		elif(action=="help"):
			print_help()
		else:
			pass
		try:
			zip=ZipFile(action,"r")
			break
		except:
			if(action=="" or action=="help"):
				pass
			else:
				print("\n\033[0;91m[!] Unable to locate the zip file!\033[0;0m")
	except:
		pass


if (exit==True):
	sys.exit()
else:
	pass

list=input("\nBlackZip Password list Path (ex:/home/BlackPass.txt) :~ ")

try:
	word=open(list,"rb")
	count=open(list,"r")
except:
	print("\n\033[0;91m[!] Unable to locate the password list!\033[0;0m")
	sys.exit()

print("\n")
line=count.readline()
condition=0
while(line):
	password=word.readline()
	try:
		zip.extractall(path="Extract BlackZip",pwd=password.strip())
		print("\n[Password Found!] :: {}".format(password.decode()))
		condition+=1
		break
	except:
		print(password.decode())
	line=count.readline()
	
if(condition==0):
	print("\n[Password not found!]")
else:
	pass

zip.close()
word.close()
count.close()
