import cv2 
import serial 
port=" /dev/tty.usbmodem1101" 
bt=serial.Serial (port, 9600) 
while True:
  d=0
  A = int (input ( 'How many members: '))
  B = int (input ( 'How much have you paid(TOTAL) : '))
  if A*100<=B:
  d=1 string='X(0)'.format (d)
  bt.write(string.encode ( ))
  C=int(bt.readline ( ) )
  print ("For you its slot " ,C)
  print ("\n" )
  if C==10:
    print ("The slot is Full")
    break;
  elif A*100>B:
    print ("Pay the remaining Amount of Rs: ", (A*100) -B)
