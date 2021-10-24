
import socket
import time


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
   try:
      s.settimeout(1)
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
        return False
flag = 0
flagOld = 0
print("Monitoring is ON!")
while (True):
    
    if isOpen("192.168.1.105","28001") == False  :
        if flag == 0:
           #print("State Monitor is DOWN" + " "  + time.asctime() + "\n-----------------------------------------------")
            with open("OutputFlag.txt", "a") as text_file:
              print(f"Service is DOWN" + " "  + time.asctime() + "\n-----------------------------------------------", file=text_file)
              flag = 1
              time.sleep(360)
        else:
           print("Service is is DOWN" + " "  + time.asctime() + "\n-----------------------------------------------")
           if flagOld == flag:
                #flagOld = flag
                time.sleep(360)
           else:
               flagOld = 1
               time.sleep(360)
		
    else:
        #print("State Monitor is UP" + " "  + time.asctime() + "\n-----------------------------------------------")
        if flag == 0:
            with open("OutputFlag.txt", "a") as text_file:
              print(f"Service is UP" + " "  + time.asctime() + "\n-----------------------------------------------", file=text_file)
              flag = 1
              time.sleep(60)
        else:
           print("Service is UP" + " "  + time.asctime() + "\n-----------------------------------------------")
           if flagOld == flag:
                #flagOld = flag
                time.sleep(60)
           else:
               flagOld = 1
               time.sleep(60)
		   
            

