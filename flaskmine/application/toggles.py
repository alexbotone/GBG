import logging

save_per_category = True
dont_save = False

if save_per_category and dont_save:
    logging.error("It's a inconsistent behaviour! Save and don't save toggles are TRUE")
    exit()


if save_per_category:
    toggle_save_images_per_category = True
    toggle_save_images = False
else:
    toggle_save_images_per_category = False
    toggle_save_images = True

if dont_save:
    toggle_save_images_per_category = False
    toggle_save_images = False



def get_toggle_save_images():
    return toggle_save_images

def get_toggle_save_images_per_category():
    return toggle_save_images_per_category
