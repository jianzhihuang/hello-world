import os
import subprocess
import threading
import re
import time
import sys
#from uiautomator import Device#
#####By Ken######


system_raw_gz="./system.raw.gz"
boot_img="./boot-debug.img "


def excute(cmd):
    subprocess.Popen(cmd, shell=True)

def get_conn_dev_fastboot():
    connectdeviceid = []
    p = os.popen('fastboot devices')
    outStr = p.read()
    print(outStr)
    connectdeviceid = re.findall(r'(\w+)\s+fastboot\s', outStr) #filter SN
    return connectdeviceid
    
def get_conn_dev_adb():
    connectdeviceid = []
    p = os.popen('adb devices')
    outstr =  p.read()
    print (outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr) 
    return connectdeviceid
def fastboot_unlock():
    connectdevice = get_conn_dev_fastboot()
    commands = []


    for device in connectdevice:
        cmd = "fastboot -s %s flashing  unlock" % (device)
        os.system(cmd)
        
    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
     t = threading.Thread(target = excute, args = (commands[i],))
     threads.append(t)

    for i in range(threads_count):
        time.sleep(1) 
        threads[i].start()
        

    for i in range(threads_count):
                threads[i].join()

def flash_boot():
    connectdevice = get_conn_dev_fastboot()
    commands = []

    for device in connectdevice:
        cmd = "fastboot -s %s flash boot  %s " % (device,boot_img)
        os.system(cmd)
        time.sleep(1)
       
  
    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
     t = threading.Thread(target = excute, args = (commands[i],))
     threads.append(t)

    for i in range(threads_count):
        time.sleep(1) 
        threads[i].start()
        

    for i in range(threads_count):
                threads[i].join()
def flash_system_raw_gz():
    connectdevice = get_conn_dev_adb()
    commands = []
   #for device in connectdevice:#
        #d = Device(device)#
       # print(d.info)#
    
    check_file=os.path.isfile('./system.raw.gz')

    if check_file == True:
     print( "system.raw.gz is exist already.") 
    else:
        print( "compressioning===========>system.raw.gz") 
        os.system("gzip -c system.img > system.raw.gz")

    for device in connectdevice:
        cmd = "adb -s %s push  %s /storage/emulated/0/Download" % (device,system_raw_gz)
        os.system(cmd)
        time.sleep(20)
 
        cmd = "adb -s %s shell setprop persist.sys.fflag.override.settings_dynamic_system true" % (device)
        os.system(cmd)
        time.sleep(1)
 
        cmd = "adb -s %s shell am start-activity \
-n com.android.dynsystem/com.android.dynsystem.VerificationActivity \
-a android.os.image.action.START_INSTALL \
-d file:///storage/emulated/0/Download/system.raw.gz \
--el KEY_SYSTEM_SIZE $(du -b system.img|cut -f1) \
--el KEY_USERDATA_SIZE 8589934592" % (device)
        os.system(cmd)
        time.sleep(1)
        
    
  

    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
     t = threading.Thread(target = excute, args = (commands[i],))
     threads.append(t)

    for i in range(threads_count):
        time.sleep(1) 
        threads[i].start()
        

    for i in range(threads_count):
                threads[i].join()




def main():
    answer=0
    
    
    
    while  answer  is not "4":
        
        print("Author Ken \n1.fastboot unlock \n2.flash boot.img  \n3.flash system.raw.gz\n4.exit")
        answer =input("please choose (1)(2)(3)(4)")
        
        
        if answer  =="1":
            print ("############UNLOCK#############")
            fastboot_unlock()
        elif answer =="2":
            print ("############FLASH BOOT.IMG#############")
            flash_boot()
        elif answer =="3":
            print ("############FLASH GSI.IMG#############")
            flash_system_raw_gz()
        elif answer =="4":
            break
        else:
            continue
        
            



if __name__ == '__main__':
      main()
