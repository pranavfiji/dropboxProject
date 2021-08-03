import dropbox
import os 

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def uploadFile(self,file_to,file_from):
        dbx = dropbox.Dropbox(self.access_token)
        for roots,dirs,files in os.walk(file_from):
            relative_path=os.path.relpath(file_to,file_from)
            dropbox_path=os.path.join(file_to,relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
               
def main:
     access_token = 'sJnnBy9xN_UAAAAAAAAAAbIeX345CVk5CvfK6KWM3SFpeA8p5TozpshUl6J2e5-w'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/12029/OneDrive/Shiel/fortnite folder'
    file_to = '/c101_dropbox/'  # The full path to upload the file to, including the file name

    #input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")
main()