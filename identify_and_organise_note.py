from utils.utils import *
from utils.google_drive_connect import *
import sys

if __name__ == "__main__":
    project_root = os.path.abspath(os.curdir)
    image_name = "blank_note.jpg"
    if len(sys.argv) > 1:
        image_name = str(sys.argv[1])
    print(f"Assessing file {image_name}")

    upload_to_drive = True
    if len(sys.argv) > 2:
        upload_to_drive = sys.argv[2].lower() == "true" if len(sys.argv) > 2 else False
    print(f"Uploading to Google Drive: {str(upload_to_drive)}")

    image_path = get_images_folder_path(image_name, project_root)
    image = load_and_scale_image(image_path, scale_factor=0.2)

    colour_refs = get_colour_ref_names(project_root)
    values_dict = {}
    range_constant = 40
    for colour in colour_refs:
        colour = colour.rsplit(".", 1)[0]
        mean_r, mean_g, mean_b = mean_pixel_values(colour)
        values_dict[colour] = ((max(mean_r-range_constant, 0), max(mean_g-range_constant, 0), max(mean_b - range_constant, 0)),
                               (min(mean_r+range_constant, 255), min(mean_g+range_constant, 255), min(mean_b + range_constant, 255)))

    count_threshold = 2000
    masks = {}
    for colour, value_range in values_dict.items():
        mask = create_mask(image, value_range)
        masks[colour] = mask

    note_colours = []
    for colour, mask in masks.items():
        count = count_mask(mask)
        note_colour = check_count(count_threshold, count, colour)
        if note_colour != None:
            note_colours.append(note_colour)

    if upload_to_drive:
        google_drive_connection = set_up_connection()
    # parent_folder_id = get_folder_id(google_drive_connection, "colourful_notes")
    if len(note_colours) != 0:
        print(f"This note belongs to the: {' and '.join(note_colours)} folder(s).")
        for colour in note_colours:
            if upload_to_drive:
                folder_id = get_folder_id(google_drive_connection, colour)
                upload_file_to_folder(image_path, google_drive_connection, folder_id)
    else:
        print("This note does not have sticky note attached.")
        if upload_to_drive:
            folder_id = get_folder_id(google_drive_connection, "no_colour")
            upload_file_to_folder(image_path, google_drive_connection, folder_id)

    # show_mask(image, masks, "pink")
