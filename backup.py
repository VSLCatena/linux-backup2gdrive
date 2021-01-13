from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from pydrive.auth import ServiceAccountCredentials

gauth = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secrets.json", scope)
drive = GoogleDrive(gauth)

# Create GoogleDriveFile instance with title 'Hello.txt'.
file1 = drive.CreateFile({'title': 'backup.tar.gz'})
file1.Upload() # Upload the file.
print('title: %s, id: %s' % (file1['title'], file1['id']))
# title: Hello.txt, id: {{FILE_ID}}
