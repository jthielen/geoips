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

"""Passive Microwave 89 GHz Colorized Brightness Temperature.

Data manipulation steps for the "color89" product.
This algorithm expects Brightness Temperatures in units of degrees Kelvin
"""

from geoips.interfaces.class_based.algorithms import BaseAlgorithmPlugin

import logging

LOG = logging.getLogger(__name__)


class PmwColor89AlgorithmPlugin(BaseAlgorithmPlugin):
    """PMW Color89 algorithm plugin class."""

    interface = "algorithms"
    family = "list_numpy_to_numpy"
    name = "pmw_color89"

    def call(self, arrays):
        """color89 product algorithm data manipulation steps.

        This algorithm expects Brightness Temperatures in units of degrees Kelvin,
        and returns red green and blue gun arrays.

        Parameters
        ----------
        arrays : list of numpy.ndarray
            * list of numpy.ndarray or numpy.MaskedArray of channel data and
                other variables, in order of sensor "variables" list
            * Channel data: Degrees Kelvin

        Returns
        -------
        numpy.ndarray
            numpy.ndarray or numpy.MaskedArray of qualitative RGBA image output
        """
        h89 = arrays[0]
        v89 = arrays[1]

        from geoips.data_manipulations.corrections import apply_data_range, apply_gamma

        red = 1.818 * v89 - 0.818 * h89
        red = apply_data_range(
            red,
            220.0,
            310.0,
            min_outbounds="crop",
            max_outbounds="crop",
            norm=True,
            inverse=True,
        )
        red = apply_gamma(red, 1.0)

        grn = (h89 - 240.0) / (300.0 - 240.0)
        grn = apply_data_range(
            grn,
            0.0,
            1.0,
            min_outbounds="crop",
            max_outbounds="crop",
            norm=True,
            inverse=False,
        )
        grn = apply_gamma(grn, 1.0)

        blu = (v89 - 270.0) / (290.0 - 270.0)
        blu = apply_data_range(
            blu,
            0.0,
            1.0,
            min_outbounds="crop",
            max_outbounds="crop",
            norm=True,
            inverse=False,
        )
        blu = apply_gamma(blu, 1.0)

        from geoips.image_utils.mpl_utils import (
            alpha_from_masked_arrays,
            rgba_from_arrays,
        )

        alp = alpha_from_masked_arrays([red, grn, blu])
        rgba = rgba_from_arrays(red, grn, blu, alp)
        return rgba


PLUGIN_CLASS = PmwColor89AlgorithmPlugin
