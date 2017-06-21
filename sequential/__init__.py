from . import links
from . import layers
from . import functions
from . import util
from . import chain
from .sequential import *

def from_json(str):
	seq = Sequential()
	seq.from_json(str)
	return seq

def from_dict(dict_array):
	seq = Sequential()
	seq.from_dict(dict_array)
	return seq