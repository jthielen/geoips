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

"""Fixtures for testing Order-Based Procflow-specific utility functions."""

# Third-Party Libraries
import pytest

# GeoIPS imports
from geoips.constants import PLUGIN_PROVIDED


@pytest.fixture
def workflow_with_plugin_provided():
    """Return workflow containing plugin-provided values."""
    return {
        "spec": {
            "steps": {
                "reader": {
                    "kind": "reader",
                    "arguments": {
                        "test": PLUGIN_PROVIDED,
                        "variables": ["B14BT"],
                    },
                }
            }
        }
    }
