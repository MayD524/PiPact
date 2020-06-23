import json
import datetime
main_list = "bk.json"
logs = "logs.json"
users = []
host_MAC = ''
needed_data = {'safe':True, "macs": []}
safe = True
def make_log():
    log_time = datetime.datetime.now()
    with open(main_list, 'r') as f:
        data = json.load(f)
    data[log_time] = needed_data

    with open(main_list, 'w') as f:
        json.dump(data, f)
        
    
        

class estimate_distance_samsung(object):
    def __init__(self, dev2, rssi, mac):
        self.dev2 = dev2
        self.rssi = rssi
        self.mac = mac
        self.safe = True

    def is_safe(self):
        if self.safe:
            return True
        
        else:
            return False

    def get_distance(self):
        is_between = self.rssi <= 85
        if is_between:
            print(f'{self.mac} is too close')
            self.safe = False
        else:
            print('safe')

        SAFE = self.is_safe() 
        return SAFE
    
class estimate_distance_raspberrypi(object):
    def __init__(self, dev2,rssi, mac):
        self.dev2 = dev2
        self.rssi = rssi
        self.mac = mac
        self.safe = True
    def is_safe(self):
        if self.safe:
            return True
        
        else:
            return False

    def get_distance(self):
        is_between = self.rssi <= 85
        if is_between:
            print(f'{self.mac} is too close')
            self.safe = False
        else:
            print('safe')

        SAFE = self.is_safe() 
        return SAFE
            


def get_rssi(filename, mac):
    with open(logs, 'r') as f:
        data = json.load(f)
    rssi = int(data.get(mac)) * -1

    return rssi

def set_class_raspberrypi(name, rssi, mac):
    rpi_estd = estimate_distance_raspberrypi(name, rssi, mac)
    safe = rpi_estd.get_distance()
    return safe

def set_class_samsung(name, rssi, mac):
    sam_estd = estimate_distance_samsung(name, rssi, mac)
    safe = sam_estd.get_distance()
    return safe
    

if __name__ == "__main__":
    host_MAC = input('Host MAC>')
    name = input('Device type>').lower()
    mac = input("Dev2 MAC> ")
    rssi = get_rssi(logs, mac)
    if name == 'samsung':
        is_safe = set_class_samsung(name, rssi, mac)
    
    elif name == 'raspberry pi':
        is_safe = set_class_raspberrypi(name, rssi, mac)
    
    if not is_safe:
        needed_data['safe'] = False
        needed_data['macs'].append(host_MAC)
        needed_data['macs'].append(mac)
        make_log(host_MAC)
            


    