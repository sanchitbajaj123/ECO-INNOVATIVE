import pyrebase
import requests
from tkinter import filedialog
config={
    "apiKey": "AIzaSyBZ0o3kFzCTPiuITe0jTZNkBPEmMjQeZPE",
  "authDomain": "eco--innovative.firebaseapp.com",
  "databaseURL":"https://eco--innovative.firebaseapp.com",
  "projectId": "eco--innovative",
  "storageBucket": "eco--innovative.appspot.com",
  "messagingSenderId": "82699048675",
  "appId": "1:82699048675:web:de8df09341d451419397d6",
  "measurementId": "G-778911CZPV"
}
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
path="images/btn.png"
p="build/assets2/frame0/button_3.png" 
# #storage.child(path).put(p)
# local_filename = "test.jpg"
# url = storage.child(path).get_url(token=None)
# # Download the file using requests
# response = requests.get(url)
# with open(local_filename, 'wb') as file:
#     file.write(response.content)
file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
print(file_path)