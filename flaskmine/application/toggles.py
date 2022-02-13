import logging

SAVE_PER_CATEGORY = True
DONT_SAVE = False

if SAVE_PER_CATEGORY and DONT_SAVE:
    logging.error("It's a inconsistent behaviour! Save and don't save toggles are TRUE")
    exit()

if SAVE_PER_CATEGORY:
    toggle_save_images_per_category = True
    toggle_save_images = False
else:
    toggle_save_images_per_category = False
    toggle_save_images = True

if DONT_SAVE:
    toggle_save_images_per_category = False
    toggle_save_images = False


def get_toggle_save_images():
    return toggle_save_images


def get_toggle_save_images_per_category():
    return toggle_save_images_per_category
