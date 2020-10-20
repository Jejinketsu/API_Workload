import requests
import time
import json

file = open("config_experiment.json")
test_config = json.load(file)
file.close()

size = 1024*1024*test_config['size_in_MB']
rate = 1/test_config['arc_per_sec']

for i in range(test_config['n_arc']):
    file_dict = {'file': bytes(size)}
    time.sleep(rate)

    print("[client] sending...")
    response = requests.post('http://127.0.0.1:8000/uploadfile_mysql/', files=file_dict)
    print("[client] sended")
    print(response.text)