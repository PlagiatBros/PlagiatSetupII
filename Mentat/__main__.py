# add local package to import path
# not needed if package is installed
from sys import path
path.insert(0, '../src/mentat')

# configure logging
import logging
logging.basicConfig(level=logging.INFO)

# add all modules
from inspect import getmembers
from mentat.module import Module
from modules import engine
import modules
for name, mod in getmembers(modules):
    if name[0] != '_' and isinstance(mod, Module):
        engine.add_module(mod)

# add routes
from routes import *
engine.add_route(trackA)

# set default route
engine.set_route('A')

# enable autorestart upon file modification
engine.autorestart()

# start main loop
engine.start()
