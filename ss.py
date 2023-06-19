import os
import time
from time import sleep

os.system("pkg install bastet -y")
os.system("pkg indtall ninvaders -y")
os.system("apt install toilet -y")
os.system("apt install libcaca -y")
os.system("apt install cmatrix")
os.system("clear")

os.system("toilet BYY-STAV")
time.sleep(1)
print("    ")
print("1:Тетрис")
print("2:star wars")
print("3:Костёр")
print("4:matrix")

a = int(input())

if a == 1:
	os.system("bastet")

elif a == 2:
	os.system("ninvaders")

elif a == 3:
	os.system("cacafire")

elif a == 4:
	os.system("cmatrix")

else:
	print("ERROR!!!")