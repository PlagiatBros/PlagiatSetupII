# add local package to import path
# not needed if package is installed
from sys import path
from os.path import dirname
path.insert(0, dirname(__file__) + '/../src/mentat')

# add all modules
from inspect import getmembers
from mentat import Module
from modules import engine
import modules
engine.add_module(modules.openstagecontrol)
for name, mod in getmembers(modules):
    if name[0] != '_' and isinstance(mod, Module) and name not in ['raysession', 'openstagecontrol']:
        engine.add_module(mod)
engine.add_module(modules.raysession)


# add routes
import routes
from mentat import Route
for name, mod in getmembers(routes):
    if name[0] != '_' and isinstance(mod, Route):
        engine.add_route(mod)

# set default route
engine.set_route('Snapshat')

# enable autorestart upon file modification
engine.autorestart()


_docs = ''
def print_params(mod, depth=0):
    global _docs
    _docs += '\n\n    ' * depth
    _docs += mod.name + '\n\n'

    for pname in mod.parameters:
        param = mod.parameters[pname]
        _docs += '    ' * (depth + 1)
        _docs += '%s (%s %s)' % (pname, param.address, param.types) + '\n'

    depth += 1
    for name in mod.submodules:
        print_params(mod.submodules[name], depth)
def docs():
    engine.root_module.wait(2,'s')
    print_params(engine.root_module, 0)
    f = open('docs.txt', 'w')
    f.write(_docs)
    f.close()

engine.root_module.start_scene('docs', docs)

# start main loop
engine.start()
