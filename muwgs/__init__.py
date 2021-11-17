'''muwgs: abbreviation for Microsoft Ultimate Word Games Script'''

__version__ = 'v1.0.0'

from .application import *
from enchant import Dict

global global_limit, global_x, global_y, global_time, english_dict

global_limit = 7
global_x = [-1, 0, 1, -1, 1, -1, 0, 1]
global_y = [-1, -1, -1, 0, 0, 1, 1, 1]
global_time = 0.05
english_dict = Dict('en-US')

# todo: add english dict serialization and new dictionary(ocr imported)
# from utils.file_utils import load_from_file
# english_dict = load_from_file('./dict.txt')

__all__ = [
    'wordament',
    'word_twister',
    'crosswords',
    'global_limit',
    'global_x',
    'global_y',
    'global_time',
    'english_dict'
]
