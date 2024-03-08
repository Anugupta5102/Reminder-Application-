import time
from plyer import notification

def reminder():
   notification.notify(title = "**Take a break!!!", message= "For the love of your work,take a break! Everything Will Work If You Unplug It For A Few Minutes.", timeout = 5)
while True:  
  reminder()
  time.sleep(10)
 