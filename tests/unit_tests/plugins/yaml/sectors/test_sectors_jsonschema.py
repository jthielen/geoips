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

"""Unit tests for sector plugins."""

import pytest
from geoips import interfaces
from geoips.interfaces.yaml_based.sectors import SectorPluginBase


def test_get_all_sectors():
    """Attempt to load all available sectors."""
    interfaces.sectors.get_plugins()


def gen_ids(sector_dict):
    """Generate ids from the name key in each sector."""
    return sector_dict["name"]


@pytest.mark.parametrize("sector", interfaces.sectors.get_plugins(), ids=gen_ids)
def test_sector(sector):
    """Ensure that a sector has the correct attributes."""
    assert isinstance(sector, SectorPluginBase)
    assert sector.interface == "sectors"
    assert sector.name
    assert sector.family
    assert sector.__doc__
    assert sector.docstring == sector.__doc__
    # Should add this back after completing #301
    # assert isinstance(sector.area_definition, pyresample.AreaDefinition)
