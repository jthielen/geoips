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

"""Coverage check routine for RGBA arrays."""

from geoips.interfaces.class_based.coverage_checkers import BaseCoverageCheckerPlugin

# Python Standard Libraries
import logging

# GeoIPS imports
from geoips.image_utils.mpl_utils import percent_unmasked_rgba

LOG = logging.getLogger(__name__)


class RgbaCoverageCheckerPlugin(BaseCoverageCheckerPlugin):
    """Rgba Coverage checker plugin class."""

    interface = "coverage_checkers"
    family = "standard"
    name = "rgba"

    def call(
        self,
        xarray_obj,
        variable_name,
        area_def=None,
    ):
        """Coverage check routine for xarray objects with projected RGBA arrays.

        Parameters
        ----------
        xarray_obj : xarray.Dataset
            xarray object containing variable "variable_name"
        variable_name : str
            variable name to check percent unmasked

        Returns
        -------
        float
            Percent coverage of variable_name
        """
        if variable_name not in xarray_obj:
            raise KeyError(
                f"Variable {variable_name} did not exist. Can not calculate coverage."
            )
        return percent_unmasked_rgba(xarray_obj[variable_name].to_masked_array())


PLUGIN_CLASS = RgbaCoverageCheckerPlugin
