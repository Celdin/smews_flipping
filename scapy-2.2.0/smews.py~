# coding= latin1
import sys, os
from scapy.all import *
from types import *
from forge import *

idt = 42
seq = ack = 0
#poignée de main(SYN)
print("handcheck")
sync,idt = newSync(idt)
ack = 0
seq = 0
reponse = sr1(sync,timeout=5)
if not(type(reponse) is NoneType):
	print("reponse:")
	reponse.show()
	seq = reponse.ack
	ack = reponse.seq + 1
	#ACK
	ACK,idt = newAck(idt,seq,ack)
	reponse = sr1(ACK,timeout=5)
	if not(type(reponse) is NoneType):
		print("reponse:")
		reponse.show()
		seq = reponse.ack
		ack = reponse.seq + 1
		print("\n")

#get index.html
print("get index")
req,idt = newReq(idt,seq,ack,'GET / HTTP/1.1\r\nHost: 192.168.1.4\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n')
reponse = sr1(req,timeout=5)
if not(type(reponse) is NoneType):
	print("reponse:")
	reponse.show()
	seq = reponse.ack
	if Raw in reponse:
		ack = reponse.seq + len(reponse[Raw])
	else:
		ack = reponse.seq + 1
	#ACK
	ACK,idt = newAck(idt,seq,ack)
	reponse = sr1(ACK,timeout=5)
	if not(type(reponse) is NoneType):
		print("reponse:")
		reponse.show()

#fin
fin,idt = newFin(idt,seq,ack)
reponse = sr1(fin,timeout=5)
if not(type(reponse) is NoneType):
	print("reponse:")
	reponse.show()
	seq = reponse.ack
	if Raw in reponse:
		ack = reponse.seq + len(reponse[Raw])
	else:
		ack = reponse.seq + 1
	#ACK
	ACK,idt = newAck(idt,seq,ack)
	reponse = sr1(ACK,timeout=5)
	if not(type(reponse) is NoneType):
		print("reponse:")
		reponse.show()
		seq = reponse.ack
		ack = reponse.seq + 1
		print("\n")
