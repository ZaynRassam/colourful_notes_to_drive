import cv2
import numpy as np
import os

def get_images_folder_path(image_name, project_root):
    image_path = os.path.join(project_root, "notes", image_name)
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image '{image_name}' not found at {image_path}")
    return image_path

def load_and_scale_image(image_path, scale_factor=1):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    scaled_image = cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor)
    return scaled_image

def get_colour_ref_names(project_root):
    colour_ref_path = os.path.join(project_root, "colour_refs")
    return os.listdir(colour_ref_path)


def mean_pixel_values(colour):
    reference = cv2.imread(f"colour_refs/{colour}.png")
    reference = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)
    rgb_list = cv2.mean(reference[:, :])
    mean_r = rgb_list[0]
    mean_g = rgb_list[1]
    mean_b = rgb_list[2]
    return mean_r, mean_g, mean_b

def create_mask(image, value_range):
    lower_range = np.array(value_range[0], dtype="uint8")
    upper_range = np.array(value_range[1], dtype="uint8")
    mask = cv2.inRange(image, lower_range, upper_range)
    return mask

def count_mask(mask):
    count = 0
    for i, row in enumerate(mask):
        for j, column in enumerate(row):
            if column == 255:
                count += 1
    return count

def check_count(count_threshold, count, colour):
    if count > count_threshold:
        return colour

def show_mask(image, masks, colour):
    detected_output = cv2.bitwise_and(image, image, mask=masks[colour])
    cv2.imshow(f"{colour} color detection", detected_output)
    cv2.waitKey(0)