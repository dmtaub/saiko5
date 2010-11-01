#!/usr/bin/python
import liblo
import time
addresses = [liblo.Address("192.168.1.122","2222")]#,liblo.Address("192.168.1.4","2222"),liblo.Address("192.168.1.5","2222"),liblo.Address("192.168.1.6","2222"),liblo.Address("192.168.1.7","2222"),liblo.Address("192.168.1.8","2222"),liblo.Address("192.168.1.9","2222"),liblo.Address("192.168.1.10","2222"),liblo.Address("192.168.1.11","2222"),liblo.Address("192.168.1.12","2222"),liblo.Address("192.168.1.13","2222"),liblo.Address("192.168.1.14","2222"),liblo.Address("192.168.1.15","2222"),liblo.Address("192.168.1.16","2222"),liblo.Address("192.168.1.17","2222")]


r=0
g=0
b=0
#not sure about the k.op section yet.. it's open to ideas, but let me save and
#stash.

rformula = lambda k: (k.r+k.step if k.op == plus else k.r-k.step)
gformula = lambda k: (k.r*.22)
bformula = lambda k: (k.r*.22)
#i've been working on this file but i never finished cuz it got late..
#basically its a simple scripting where you define the movements of
#colors by lambda formulae 
#stepcorners = 
stepmin = 0.0
stepmax = .6

step = 1.0/256
delay = 0.01

while True:
	while r < colormax :
		for address in addresses:
			liblo.send(address,'/l22',('f', r),('f', g),('f', b))
		r=rformula(step)
		g=(r+step)*gratio
		time.sleep(delay)
    
	while r > colormin :
		for address in addresses:
			liblo.send(address,'/l22',('f', r),('f', g),('f', b))
		r=r-step
		g=(r+step)*gratio
		time.sleep(delay)
