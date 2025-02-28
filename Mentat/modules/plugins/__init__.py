from .default import Plugin
from .eq import AceEQ

plugin_map = {
    'ACE%20EQ': SC4
}

def osc_plugin(plugin):

    if plugin.name in plugin_map:
        return plugin_map[plugin.name](plugin)
    else:
        return Plugin(plugin)
