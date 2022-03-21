# add local package to import path
# not needed if package is installed
from sys import path, exit
from os.path import dirname
path.insert(0, dirname(__file__) + '/../src/mentat')

# add all modules
from inspect import getmembers, signature
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

#################################################################
#################################################################
# UGLY DOCS GENERATION
_docs = ''
_types = []
def print_params(mod, depth=0):
    global _docs

    t = type(mod).__name__
    if t in _types:
        return
    _types.append(t)

    _docs += '\n\n' + '    ' * depth
    if depth != 0:
        _docs += t + ': ' + ', '.join([mod.name] + [x.name for x in mod.parent_module.submodules.values() if type(x) == type(mod) and x != mod])
    else:
        _docs += t + ': ' + mod.name

    params = [p for p in mod.parameters.values() if type(p).__name__ == 'Parameter']
    mparams = [p for p in mod.parameters.values() if type(p).__name__ == 'MetaParameter']

    for pbank in [params, mparams]:
        if pbank:
            _docs += '\n\n' + '    ' * (depth + 1)
            _docs += type(pbank[0]).__name__ + 's:\n\n'
            for param in pbank:
                _docs += '    ' * (depth + 1)
                _docs += '%s (%s %s)' % (param.name, param.address, param.types) + '\n'

    methods = [x for n,x in getmembers(mod) if callable(x) and not hasattr(Module,n)]
    if methods:
        _docs += '\n\n' + '    ' * (depth + 1)
        _docs += 'Methods:\n\n'
        for m in methods:
            _docs += '    ' * (depth + 1)
            _docs += '%s%s' % (m.__name__, str(signature(m))) + '\n'

    for name in mod.submodules:
        print_params(mod.submodules[name], depth + 1)

def docs():
    engine.root_module.wait(2,'s')
    print_params(engine.root_module, 0)
    f = open('docs.txt', 'w')
    f.write(_docs)
    f.close()

engine.root_module.start_scene('docs', docs)
#################################################################
#################################################################

# start main loop
engine.start()
