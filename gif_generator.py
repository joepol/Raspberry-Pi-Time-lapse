import os
import imageio
from datetime import date

DEFAULT_PATH = 'images\\'
DEFAULT_DURATION = 0.2


def _get_files_list(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                files.append(os.path.join(r, file))

    # for f in files:
    #     print(f)
    return files


def generate_gif(path=DEFAULT_PATH, duration=DEFAULT_DURATION):
    frames = []
    file_names = _get_files_list(path)
    for filename in file_names:
        frames.append(imageio.imread(filename))
    # dd/mm/YY
    today = date.today().strftime("%d_%m_%Y")
    outfile_name = '{}timelapse_{}.gif'.format(path, today)
    imageio.mimsave(outfile_name, frames, format='GIF', duration=duration)

