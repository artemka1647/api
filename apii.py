import requests

file_path = os.path.join('test.txt')
print(file_path)

token = AgAAAAAHykP1AADLW3ucfaeP-UwahOoiExVLeRE
class Yadisk:

    def __init__(self,token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type':'application/json',
            'Authorization': 'OAuth{}'.format(self.token)
        }


    def get_upload_link(self,disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resourses/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path,'overwrite':'true'}
        response= requests.get(upload_url, headers= headers, params = params)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self,disk_file_path,filename):
        href = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename,'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Успешно')

ya= Yadisk(token= 'AgAAAAAHykP1AADLW3ucfaeP-UwahOoiExVLeRE')
ya.upload_file_to_disk(disk_file_path, 'test.txt')

disk_file_path = os.path.join(test.txt)
print(file_path)