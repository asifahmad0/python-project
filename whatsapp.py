import pywhatkit as pyw
numbre= int(input('entre Mobile Numbre:- '))
msg = input("entre your Masseges:- ")
hh= int(input("Entre Time's houre only:- "))
mm= int(input("Entre Time's Minutse:- "))

pyw.sendwhatmsg(numbre, msg, hh,mm)