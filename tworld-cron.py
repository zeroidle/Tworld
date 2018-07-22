#!/usr/local/bin/python3.6
import sys
import time
from Tworld.Tworld import Tworld
from tworld_auth import data
import json

def save_data(user_id, data):
    f = open('/tmp/' + user_id, 'w');
    s = f.write(data)
    f.close()

def get_discovery(data):
    datadict = []
    for item in data:
        raw = {
                '{#TWORLDNAME}': item,
                '{#TWORLDID}': data[item][0],
                }
        datadict.append(raw)
    rtn_array = {'data':datadict}
    return rtn_array

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Arguments required.")
        exit(0)
    elif sys.argv[1] == "--list":
        print(json.dumps(get_discovery(data),  ensure_ascii=False))
        exit(0)
    elif sys.argv[1] != "run":
        user_id = sys.argv[1]
        f = open('/tmp/' + user_id, 'r');
        s = f.read()
        print(s)
        f.close()
        exit(0)

    while True:
        try:
            for key in data:
                tworld = Tworld()
                print("%s 처리중" % key)
                auth_info = data.get(key)
                if tworld.login(auth_info[0], auth_info[1]):
                    result = tworld.get_available_data_in_mb()
                    save_data(auth_info[0], str(result))
                    print(result)
        except Exception as e:
            print(e)
        finally:
            print("휴식")
            time.sleep(3600)