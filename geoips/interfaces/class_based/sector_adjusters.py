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

"""Sector adjusters interface class."""

from geoips.interfaces.class_based_plugin import BaseClassPlugin
from geoips.interfaces.base import BaseClassInterface


class BaseSectorAdjusterPlugin(BaseClassPlugin, abstract=True):
    """Base class for GeoIPS sector_adjuster plugins."""

    data_tree = False

    pass


class SectorAdjustersInterface(BaseClassInterface):
    """Interface for adjusting a sector based on additional information.

    Ie, pass in data and the area definition, and modify the area_definition based
    on the data itself.
    """

    name = "sector_adjusters"
    plugin_class = BaseSectorAdjusterPlugin

    required_args = {
        "list_xarray_list_variables_to_area_def_out_fnames": [
            "xobjs",
            "area_def",
            "variables",
        ]
    }
    required_kwargs = {
        "list_xarray_list_variables_to_area_def_out_fnames": ["recenter_variables"]
    }


sector_adjusters = SectorAdjustersInterface()
