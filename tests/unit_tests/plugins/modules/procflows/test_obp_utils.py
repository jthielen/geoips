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

"""Unit tests for Order-Based Procflow specific utility functions."""

# GeoIPS imports
from geoips.plugins.modules.procflows.obp_utils import (
    remove_keys_with_default_value_plugin_provided,
)


def test_remove_plugin_provided_root_level_key(workflow_with_plugin_provided):
    """Ensure keys wtih value PLUGIN_PROVIDED are removed."""
    actual = remove_keys_with_default_value_plugin_provided(
        workflow_with_plugin_provided
    )

    reader_arguments = actual["spec"]["steps"]["reader"]["arguments"]

    assert "test" not in reader_arguments
    assert reader_arguments["variables"] == ["B14BT"]
