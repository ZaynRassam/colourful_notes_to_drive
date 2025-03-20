import pydrive2.auth
from pydrive2.drive import GoogleDrive

def set_up_connection():
    gauth = pydrive2.auth.GoogleAuth()
    drive = GoogleDrive(gauth)
    return drive

def get_folder_id(google_drive_connection, colour):
    folder_name = colour
    folders = google_drive_connection.ListFile(
        {'q': "title='" + folder_name + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folder_name:
            print("folder title: ", folder['title'])
            print("folder id: ", folder['id'])
            return folder['id']

def upload_file_to_folder(image_name, google_drive_connection, folder_id):
    file = google_drive_connection.CreateFile({'title': image_name, 'parents': [{'id': folder_id}]})
    file.SetContentFile(image_name)
    file.Upload()
    print('Created file %s with mimeType %s' % (file['title'],
                                                file['mimeType']))
