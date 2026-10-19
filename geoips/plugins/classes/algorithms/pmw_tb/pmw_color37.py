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

"""Passive Microwave 37 GHz Colorized Brightness Temperature.

Data manipulation steps for the "color37" product.
This algorithm expects Brightness Temperatures in units of degrees Kelvin
"""

from geoips.interfaces.class_based.algorithms import BaseAlgorithmPlugin

import logging

LOG = logging.getLogger(__name__)


class PmwColor37AlgorithmPlugin(BaseAlgorithmPlugin):
    """PMW Color37 algorithm plugin class."""

    interface = "algorithms"
    family = "list_numpy_to_numpy"
    name = "pmw_color37"

    def call(self, arrays):
        """color37 product algorithm data manipulation steps.

        This algorithm expects Brightness Temperatures in units of degrees Kelvin,
        and returns red green and blue gun arrays.

        Parameters
        ----------
        data : list of numpy.ndarray
            * list of numpy.ndarray or numpy.MaskedArray of channel data,
                in order of channels list above
            * Degrees Kelvin

        Returns
        -------
        numpy.ndarray
            numpy.ndarray or numpy.MaskedArray of qualitative RGBA image output
        """
        h37 = arrays[0]
        v37 = arrays[1]

        from geoips.data_manipulations.corrections import apply_data_range, apply_gamma

        red = 2.181 * v37 - 1.181 * h37
        red = apply_data_range(
            red,
            260.0,
            280.0,
            min_outbounds="crop",
            max_outbounds="crop",
            norm=True,
            inverse=True,
        )
        red = apply_gamma(red, 1.0)

        grn = (v37 - 180.0) / (300.0 - 180.0)
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

        blu = (h37 - 160.0) / (300.0 - 160.0)
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


PLUGIN_CLASS = PmwColor37AlgorithmPlugin
