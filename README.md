This application takes images of notes and categorises them into their corresponding Google Drive folder.
Loading images and the classification is achieved using the OpenCV library, and the Google Drive connection using the PyDrive2 library.

To run the script:  
```python identify_and_organise_notes.py <image_name>.<extension> <boolean>```

The first CLI arguement dictates the image name and extension (file should be located in the notes folder.  
The second arguement is set to ```True``` if the user wishes to upload the note to Google Drive, and set to ```False``` if not.

Folders for each coloured note should be created in Google Drive before running the application. A folder for "no_colour" must also be created in the event that an image has been processed without a coloured sticky note.   
Currently, these folders must be located in the root directory of Google Drive.

The folder ```colour_refs``` should include PNG files of the sticky notes that are used to identify the images. The names of these files should match the names of the Google Drive folders that the images will be organised into.   

