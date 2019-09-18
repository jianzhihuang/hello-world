import os
import subprocess
import threading
import re
import time

apk_path="/home/jianzhi/5771379[QP1A.190711.018]CTS-V/android-cts-verifier/CtsForceStopHelper.apk"
apk_path1="/home/jianzhi/5771379[QP1A.190711.018]CTS-V/android-cts-verifier/CtsPermissionApp.apk"
apk_path2="/home/jianzhi/5771379[QP1A.190711.018]CTS-V/android-cts-verifier/CtsEmptyDeviceAdmin.apk"
apk_path3="/home/jianzhi/5771379[QP1A.190711.018]CTS-V/android-cts-verifier/CtsVerifierUSBCompanion.apk"
apk_path4 = "/home/jianzhi/5771379[QP1A.190711.018]CTS-V/android-cts-verifier/CtsVerifier.apk"
apk_path5 = "/home/jianzhi/5771379[QP1A.190711.018]CTS-V/android-cts-verifier/NotificationBot.apk"


def excute(cmd):
    subprocess.Popen(cmd, shell=True)

def get_conn_dev():
    connectdeviceid = []
    p = os.popen('adb devices')
    outstr =  p.read()
    print (outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid

def main():
    connectdevice = get_conn_dev()
    commands = []
    
    
    for device in connectdevice:
        cmd = "adb -s %s install    %s" % (device,apk_path)
        os.system(cmd)
        time.sleep(2)
        cmd1 = "adb -s %s install   %s" % (device,apk_path1)
        os.system(cmd1)
        time.sleep(2)
        cmd2 = "adb -s %s install   %s" % (device,apk_path2)
        os.system(cmd2)
        time.sleep(2)
        cmd3 = "adb -s %s install   %s" % (device,apk_path3)
        os.system(cmd3)
        time.sleep(2)
        cmd4 = "adb -s %s install  -r  -g  %s" % (device,apk_path4)
        os.system(cmd4)
        time.sleep(2)
        cmd5 = "adb -s %s install   %s" % (device,apk_path5)
        os.system(cmd5)
        time.sleep(2)
        commands.append(cmd)
        time.sleep(2)
  

    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
     t = threading.Thread(target = excute, args = (commands[i],))
     threads.append(t)

    for i in range(threads_count):
        time.sleep(5) 
        threads[i].start()
        

    for i in range(threads_count):
                threads[i].join()


if __name__ == '__main__':
      main()
