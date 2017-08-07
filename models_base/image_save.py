from io import BytesIO
from PIL import Image
from os.path import join
from os import mkdir
from config import UPLOAD_PHOTO
from slugify import slugify

MAX_SIZE_X = 600
MAX_SIZE_Y = 800

def save_image(first_name, last_name, photo_form):
    name_folder = slugify('%s-%s' % (first_name, last_name))
    mkdir(join(UPLOAD_PHOTO, name_folder))
    photo = Image.open(BytesIO(photo_form.read()))
    name_file = '%s-%s.%s' % (name_folder, 'base', photo.format)
    photo.thumbnail((MAX_SIZE_X, MAX_SIZE_Y), Image.ANTIALIAS)
    photo.save(join(UPLOAD_PHOTO, name_folder, name_file), dpi=(72., 72.), quality=90)
    return [join(name_folder, name_file), name_folder]