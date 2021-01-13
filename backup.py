from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from pydrive.auth import ServiceAccountCredentials

gauth = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secrets.json", scope)
drive = GoogleDrive(gauth)

folder_id = '123123123123'
file_metadata = {
    'name': 'backup.tar.gz',
    'parents':  [{"kind": "drive#fileLink", "id": folder_id}]
}
# Create GoogleDriveFile instance with title 'Hello.txt'.
file1 = drive.CreateFile(file_metadata)
file1.Upload() # Upload the file.
permission = file1.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})
print('title: %s, id: %s' % (file1['title'], file1['id']))
# title: Hello.txt, id: {{FILE_ID}}
