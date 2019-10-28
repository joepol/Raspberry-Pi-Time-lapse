import os
import imageio
import logging
from datetime import date

DEFAULT_PATH = 'temp\\'
DEFAULT_DURATION = 0.2

logger = logging.getLogger(__name__)


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
    if not frames:
        logging.debug("No frames were found in %s", path)
    # dd/mm/YY
    today = date.today().strftime("%d_%m_%Y")
    outfile_name = '{}timelapse_{}.gif'.format(path, today)
    imageio.mimsave(outfile_name, frames, format='GIF', duration=duration)
    file_size = os.stat('./'+str(outfile_name)).st_size
    logger.info("GIF generated %s, size of %s bytes", outfile_name, file_size)
    absolute_file_path = os.path.abspath('./'+str(outfile_name))
    return absolute_file_path
    # return outfile_name

generate_gif()