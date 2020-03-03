import os
import subprocess
import threading
import re
import time
import sys
#from uiautomator import Device#
#####By Ken######



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
def fastboot_oem_ramdunp():
    connectdevice = get_conn_dev_fastboot()
    commands = []


    for device in connectdevice:
        cmd = "fastboot -s %s oem ramdump" % (device)
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

def fastboot_oem_ramdunp_enable():
    connectdevice = get_conn_dev_fastboot()
    commands = []

    for device in connectdevice:
        cmd = "fastboot -s %s oem ramdump enable " % (device)
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


def adb_devices_reboot_bootloader():
    connectdevice = get_conn_dev_adb()
    commands = []
   #for device in connectdevice:#
        #d = Device(device)#
       # print(d.info)#
    

    for device in connectdevice:
        print(device+"  -----------Reboot bootloader-----------")
        cmd = "adb -s %s reboot bootloader" % (device)
        os.system(cmd)
 
     
    
  

    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
     t = threading.Thread(target = excute, args = (commands[i],))
     threads.append(t)

    for i in range(threads_count):
        time.sleep(0.5) 
        threads[i].start()
        
        

    for i in range(threads_count):
                threads[i].join()


def fastboot_reboot():
    connectdevice = get_conn_dev_fastboot()
    commands = []
   #for device in connectdevice:#
        #d = Device(device)#
       # print(d.info)#
    

    for device in connectdevice:
        cmd = "fastboot -s %s reboot" % (device)
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


def adb_root():
    connectdevice = get_conn_dev_adb()
    commands = []

    for device in connectdevice:
        cmd = "adb -s %s root " % (device)
        time.sleep(1)
        print(cmd)
        cmd ="adb  -s %s shell getprop vendor.debug.ramdump.full"% (device)
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

def adb_shell_pull_bugreport():
    connectdevice = get_conn_dev_adb()
    commands = []

    for device in connectdevice:
        cmd = "adb -s %s  pull /data/user_de/0/com.android.shell/files/bugreports/" % (device)
        time.sleep(1)
        print(cmd)
        # cmd1 ="adb  -s %s pull /data/user_de/0/com.android.shell/files/bugreports/"% (device)
        # print(cmd1)
        os.system(cmd)
        newname = device+"_bugreports"
        os.rename("bugreports",newname) 
        
       
  
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


def adb_shell_cat_freq_table_mhz():
    connectdevice = get_conn_dev_adb()
    commands = []

    for device in connectdevice:
        cmd = "adb -s %s  root" % (device)
        os.system(cmd)
        time.sleep(1)
        print(cmd)
        cmd ="adb  -s %s  shell cat /sys/class/kgsl/kgsl-3d0/freq_table_mhz"% (device)
        time.sleep(1)
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



def main():
    answer=0
    
    
    
    while  answer  is not "8":
        
        print("Author Ken \n1.Adb reboot bootloader \n2.Fastboot ramdunp  \n3.Fastboot enable ramdunp\n4.Fastboot reboot\n5.adb_shell_getprop_vendor_debug_ramdump_full\n6.adb_shell_/data/user_de/0/com.android.shell/files/bugreports/\n7.adb_shell_cat_freq_table_mhz(AAorAB)\n8.Exit")
        answer =input("please choose (1)(2)(3)(4)(5)(6)(7)(8)")
        
        
        if answer  =="1":
            print("############Reboot_bootloader#############")
            adb_devices_reboot_bootloader()
        elif answer =="2":
            print("############Fastboot_ramdunp#############")
            fastboot_oem_ramdunp()
        elif answer =="3":
            print("############Fastboot_ramdunp_enable#############")
            fastboot_oem_ramdunp_enable()
        elif answer =="4":
            print("############Fastboot_reboot#############")
            fastboot_reboot()       
        elif answer =="5":   
            print("############adb_shell_getprop_vendor_debug_ramdump_full#############")
            adb_root()  
        elif answer =="6":   
            print("############adb_shell_/data/user_de/0/com.android.shell/files/bugreports/#############")
            adb_shell_pull_bugreport()  
        elif answer =="7":   
            print("############adb shell cat /sys/class/kgsl/kgsl-3d0/freq_table_mhz#############")
            adb_shell_cat_freq_table_mhz()  
        elif answer =="8":   
            print("Exit")
            break
        else:
            continue
        
            



if __name__ == '__main__':
      main()
