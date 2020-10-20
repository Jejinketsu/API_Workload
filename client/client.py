import requests

""" with open('900214.png', 'rb') as a_file:
    file_dict = {'file': a_file}
    response = requests.post('http://127.0.0.1:8000/uploadfile/', files=file_dict) """

response = requests.get('http://127.0.0.1:8000/downloadfile/humaru.jpg')
new_file = open('humaru.jpg', 'wb')
new_file.write(response.content)
new_file.close()