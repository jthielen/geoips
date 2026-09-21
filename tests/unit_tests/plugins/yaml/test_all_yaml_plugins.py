# !#######################################################################
#
# THIS SOURCE CODE IS PROPERTY OF THE GOVERNMENT OF THE UNITED STATES OF
# AMERICA. BY USING, MODIFYING, OR DISSEMINATING THIS SOURCE CODE, YOU ACCEPT
# THE TERMS AND CONDITIONS IN THE NRL OPEN LICENSE AGREEMENT. USE, MODIFICATION,
# AND DISSEMINATION ARE PERMITTED ONLY IN ACCORDANCE WITH THE TERMS AND
# CONDITIONS OF THE NRL OPEN LICENSE AGREEMENT. NO OTHER RIGHTS OR LICENSES
# ARE GRANTED. UNAUTHORIZED USE, SALE, CONVEYANCE, DISPOSITION, OR MODIFICATION
# OF THIS SOURCE CODE MAY RESULT IN CIVIL PENALTIES AND/OR CRIMINAL PENALTIES
# UNDER 18 U.S.C. § 641.
#
# !########################################################################

"""Test all YAML plugins."""

import pytest
import yaml
from importlib import resources, metadata

from geoips import interfaces


def yield_plugins():
    """Yield plugins."""
    plugin_packages = metadata.entry_points(group="geoips.plugin_packages")
    for pkg in plugin_packages:
        fpath = resources.files(pkg.name) / "plugins/yaml"
        plugin_files = fpath.rglob("*.yaml")
        for pf in plugin_files:
            yield pf


def gen_label(val):
    """Generate the yaml name for pytest ids."""
    return val.name


@pytest.mark.parametrize("plugin", yield_plugins(), ids=gen_label)
def test_is_plugin_valid(plugin):
    """Test if plugin is valid."""
    with open(plugin, "r") as fo:
        docs = list(yaml.safe_load_all(fo))

    for rplugin in docs:
        interface = getattr(interfaces, rplugin["interface"])
        # All 'get_plugin' calls perform validation. No need to call the validator
        # directly
        if rplugin["interface"] == "products":
            # validate product plugins against their source name instead of the top
            # level product name. That is not always a source, such as the integration
            # test products we have.
            for prod_plg in rplugin["spec"]["products"]:
                for source_name in prod_plg["source_names"]:
                    interface.get_plugin(source_name, prod_plg["name"])
        else:
            # Otherwise just validate against the top level name.
            interface.get_plugin(rplugin["name"])
