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

"""Sector spec generators interface class."""

from geoips.interfaces.class_based_plugin import BaseClassPlugin
from geoips.interfaces.base import BaseClassInterface


class BaseSectorSpecGeneratorPlugin(BaseClassPlugin, abstract=True):
    """Base class for GeoIPS sector_spec_generator plugins."""

    data_tree = False

    pass


class SectorSpecGeneratorsInterface(BaseClassInterface):
    """Interface for generating appropriate specifications for a sector.

    Generates a sector specification (location, resolution, etc)
    using a dynamically determined subset of information (ie, center
    lat/lon of the region determined at run time, while the resolution
    and width/height are predetermined)
    """

    name = "sector_spec_generators"
    plugin_class = BaseSectorSpecGeneratorPlugin

    required_args = {"area_definition": []}
    required_kwargs = {"area_definition": []}


sector_spec_generators = SectorSpecGeneratorsInterface()
