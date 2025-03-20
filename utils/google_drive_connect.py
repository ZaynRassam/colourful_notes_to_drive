import pydrive2.auth
from pydrive2.drive import GoogleDrive
import time
import json


def set_up_connection():
    gauth = pydrive2.auth.GoogleAuth()
    drive = GoogleDrive(gauth)
    return drive


def get_folder_id(google_drive_connection, colour):
    start = time.time()
    folder_name = colour
    with open("folder_id_cache.json") as json_file:
        folders_id_dict = json.load(json_file)

    if colour in folders_id_dict.keys():
        end = time.time()
        print("Time taken to find folder ID using cache: ", end-start)

        return folders_id_dict[colour]
    else:
        folders = google_drive_connection.ListFile(
            {'q': "title='" + folder_name + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        for folder in folders:
            if folder['title'] == folder_name:
                print("folder title: ", folder['title'])
                print(f"folder id: {folder['id'][:7]}...")
                end = time.time()
                print("Time taken to find folder ID without cache: ", end-start)

                dict_to_add_to_cache = {colour: folder['id']}
                folders_id_dict.update(dict_to_add_to_cache)
                with open("folder_id_cache.json", "w+") as f:
                    json.dump(folders_id_dict, f)

                return folder['id']


def upload_file_to_folder(image_name, google_drive_connection, folder_id):
    file = google_drive_connection.CreateFile({'title': image_name, 'parents': [{'id': folder_id}]})
    file.SetContentFile(image_name)
    file.Upload()
    print('Created file %s with mimeType %s' % (file['title'],
                                                file['mimeType']))
