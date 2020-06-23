import json

save = {}
json_file = "logs.json" ## json file
white = "white_list.json" ## white list

def save_to_json(log):
    with open(json_file, 'w') as f: ## write to json
        json.dump(log, f, indent=4)       


def get_BT_DATA(line):
    with open(white, 'r') as f:
        wlist = json.load(f)
    if len(line) > 5:
        mac = line[2]
        rssi = line[7]
        if mac not in wlist['usr']:
            return
        else:
            save[mac] = rssi ## saves the mac and rssi value
    else:
        return
            

def read_file(filename):
    get_file = open(filename, 'r')
    lines = get_file.readlines()
    for line in lines:
        line = line.split(' ')
        get_BT_DATA(line)



if __name__ == "__main__":
    log_file = "rssi_log.txt" ## Log file
    read_file(log_file) ## reads file
    save_to_json(save)  