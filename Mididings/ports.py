# add local package to import path
# not needed if package is installed
from sys import path
from os.path import dirname
path.insert(0, dirname(__file__) + '/../src/mentat')
path.insert(0, dirname(__file__) + '/../Mentat')
import modules
from mentat import Module, Engine
from inspect import getmembers

def get_port(modname):
    for name, mod in getmembers(modules):
        if name[0] != '_' and (isinstance(mod, Module) or isinstance(mod, Engine)):
            if mod.name == modname:
                return mod.port
    raise Exception('module %s not found' % modname)
