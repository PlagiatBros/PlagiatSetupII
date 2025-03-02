from .default import Plugin
from .eq import AceEQ
from .comp import AceComp

plugin_map = {
    'ACE%20EQ': AceEQ,
    'ACE%20Compressor': AceComp,
}

def osc_plugin(plugin):

    if plugin.name in plugin_map:
        return plugin_map[plugin.name](plugin)
    else:
        return Plugin(plugin)
