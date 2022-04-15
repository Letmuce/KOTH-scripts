"""
This script changes the port ftp runs on every few seconds
This works with both proftpd & vsftpd
"""

import random
import time
import os
from os.path import exists

def ftp_check(version, text, reset_command):
  #check if file exists
  if (exists(version)):
    with open(version) as file:
      data = file.readlines()
  
    # replace port
    # check if Port is already specified, if not put in port
    # flag to see if line was found
    flag = False
    
    for num, line in enumerate(data, 1):
      if text in line:
        flag = True
        
        data[num - 1] = text
      # write to file
        with open('version', 'w') as file:
          file.writelines(data)
          file.close()
          
    # append to file
    if flag == False:
      append = open(version, 'a')
      append.write(text)
      append.close()
    
    
    # restart ftp
    os.system(reset_command)
  
    # delay (keep it above 1 so ftp has time to reset)
    time.sleep(3)

while True:
  ftp_check('/etc/vsftpd/vsftpd.conf', 'listen_port={}'.format(str(random.randrange(5000,65000,1))), 'service vsftpd restart')
  ftp_check('/etc/proftpd/proftpd.conf', "Port {}".format(str(random.randrange(5000,65000,1))), 'systemctl proftpd restart')
