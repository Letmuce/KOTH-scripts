"""
This script changes the port Apache runs on every few seconds
"""

import random
import time
import os

while True:
  
  with open('/etc/apache2/ports.conf') as file:
    data = file.readlines()
  
  # replace port
  data[4] = 'Listen {}'.format(str(random.randrange(5000,65000,1)))
  data.close()
  
  # write to file
  with open('/etc/apache2/ports.conf', 'w') as file:
    file.writelines(data)
    file.close()
  
  
  # restart Apache
  os.system('/etc/init.d/apache2 restart')

  # delay (keep it above 3 so Apache has time to reset)
  time.sleep(4)
