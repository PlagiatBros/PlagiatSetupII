from .default import Plugin
# from .sc4 import SC4

plugin_map = {
    # 'SC4%20mono': SC4
}

def osc_plugin(plugin):

    if plugin.name in plugin_map:
        return plugin_map[plugin.name](plugin)
    else:
        return Plugin(plugin)
