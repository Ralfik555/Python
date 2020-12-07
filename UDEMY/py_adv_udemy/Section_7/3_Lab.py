import requests
import os
import shutil

def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)

url = 'http://www.mobilo24.eu/spis/'
#url = 'oamfoafnmos'
#url = 'http://asdsa'
dir = 'C:/Users/Ralfik/Desktop/Python/py_adv_udemy/Section_7/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

#save_url_to_file(url,tmpfile_path)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
        print("Temporary file has been removed")

    save_url_to_file(url,tmpfile_path)
    print("Site {} has been save to {}".format(url,tmpfile_path))

    shutil.copy(tmpfile_path,file_path)
    print("Temporary file copy to {}".format(file_path))

except requests.exceptions.ConnectionError as e:
    print("This site does not exist or wrong url adress\nDetails\n{}".format(e))

except PermissionError:
    print('Problem accessing a file: {}'.format(file_path))

except FileNotFoundError as e:
    print("File {} does not exist\nDetails\n{}".format(tmpfile,e))

except Exception as e:
    print('Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print("Success")
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
