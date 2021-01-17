import sys
from os import path
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.settings import LoadSettingsFile
from pydrive2.auth import ServiceAccountCredentials

scriptpath=path.dirname(path.realpath(__file__))
scope = ['https://www.googleapis.com/auth/drive']

gauth = GoogleAuth()
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(path.join(scriptpath,"client_secrets.json"), scope)
drive = GoogleDrive(gauth)

# If provided arguments incorrect, print usage instructions and exit.
if len(sys.argv) < 2:
    print("usage: backup.py <Google Drive folder ID> <local file path>")
    exit(1)  # Exit program as incorrect parameters provided.

parentId = sys.argv[1]
myFilePath = sys.argv[2]
myFileName = path.basename(sys.argv[2])

# Check if file name already exists in folder.
file_list = drive.ListFile(
    {
        "q": '"{}" in parents and title="{}" and trashed=false'.format(
            parentId, myFileName
        )
    }
).GetList()

# If file is found, update it, otherwise create new file.
if len(file_list) == 1:
    myFile = file_list[0]
else:
    myFile = drive.CreateFile(
        {"parents": [{"kind": "drive#fileLink", "id": parentId}]}
    )

# Upload new file content.
myFile.SetContentFile(myFilePath)
myFile["title"] = myFileName
# The `convert` flag indicates to Google Drive whether to convert the
# uploaded file into a Google Drive native format, i.e. Google Sheet for
# CSV or Google Document for DOCX.
myFile.Upload({"convert": True})
