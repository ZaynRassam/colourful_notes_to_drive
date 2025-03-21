This application takes images of notes and categorises them into their corresponding Google Drive folder.
Loading images and the classification is achieved using the OpenCV library, and the Google Drive connection using the PyDrive2 library.

To run the script:  
```python identify_and_organise_notes.py <image_name>.<extension> <boolean>```

The first CLI arguement dictates the image name and extension (file should be located in the notes folder.  
The second arguement is set to ```True``` if the user wishes to upload the note to Google Drive, and set to ```False``` if not.

Folders for each coloured note should be created in Google Drive before running the application. A folder for "no_colour" must also be created in the event that an image has been processed without a coloured sticky note.   
Currently, these folders must be located in the root directory of Google Drive.

The folder ```colour_refs``` should include PNG files of the sticky notes that are used to identify the images. The names of these files should match the names of the Google Drive folders that the images will be organised into.   

Cache is used to retieve Google Drive folder IDs. For this to work create a ```folder_id_cache.json``` file in the root directory and insert an empty dictionary, i.e. ```{}```. Cacheing folder IDs took the time to retrieve the IDs from ~2-10 seconds to be instanateous when ID is already known. If a folder is created in Google Drive with the same name as the previous folder, if previous folder ID has already been cached, new images will be sent to this folder, otherwise, they will be sent to the newest created folder.

A ```client_secrets.json``` file must be present in the root directory of the project. This is acquired by following the instructions of this webpage: https://docs.iterative.ai/PyDrive2/quickstart/#authentication
