"""
This script changes the port ssh runs on, rewrites the sshd_config file to change the port, then restarts ssh
change sleep() time at the end to delay how often port changes
"""

import random
import time
import os

while True:
  text = 'Port '
  
  #open file
  with open('/etc/ssh/sshd_config') as file:
    data = file.readlines()

  # find line with 'Port' and replace it with random port
  for num, line in enumerate(data, 1):
    if text in line:
      data[num - 1] = 'Port {}\n'.format(str(random.randrange(5000,65000,1)))
  
  # write to file
  with open('/etc/ssh/sshd_config', 'w') as file:
    file.writelines(data)
    
  # restart ssh
  os.system('systemctl restart ssh.service')

  # delay (keep it above 1 so ssh has time to reset)
  time.sleep(3)
