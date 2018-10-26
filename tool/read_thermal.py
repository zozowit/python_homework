import os

print(os.popen('adb version').read())
print(os.popen('adb devices').read())

def read_thermal_zone(index):
    patch = 'sys/class/thermal/thermal_zone' + index + '/'
    t_type = os.popen('adb shell cat ' + patch + 'type').read()
    t_temp = os.popen('adb shell cat ' + patch + 'temp').read()
    
    print("thermal_zone"+index+" info:"+t_type+t_temp)
    
def main():
    for index in range(50, 65):
        read_thermal_zone(str(index))
        
    input('press any key to exit。。。')
        
if __name__ == "__main__":
    main()
    