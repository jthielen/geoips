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

"""Passive Microwave 37 GHz Polarization Corrected Temperature.

Data manipulation steps for the "37pct" product.
This algorithm expects Brightness Temperatures in units of degrees Kelvin.
"""

from geoips.interfaces.class_based.algorithms import BaseAlgorithmPlugin

import logging

LOG = logging.getLogger(__name__)


class Pmw37PctAlgorithmPlugin(BaseAlgorithmPlugin):
    """Pmw37 PCT algorithm plugin class."""

    interface = "algorithms"
    family = "list_numpy_to_numpy"
    name = "pmw_37pct"

    def call(
        self,
        arrays,
        output_data_range=None,
        min_outbounds="crop",
        max_outbounds="mask",
        norm=False,
        inverse=False,
    ):
        """37pct product algorithm data manipulation steps.

        This algorithm expects Brightness Temperatures in units of degrees Kelvin,
        and returns degrees Kelvin

        Parameters
        ----------
        arrays : list of numpy.ndarray
            * numpy.ndarray or numpy.MaskedArray of channel data, in order of sensor
                "channels" list
            * Degrees Kelvin

        Returns
        -------
        numpy.ndarray
            numpy.ndarray or numpy.MaskedArray of appropriately scaled channel data,
            in degrees Kelvin.
        """
        h37 = arrays[0]
        v37 = arrays[1]

        out = (2.15 * v37) - (1.15 * h37)

        if output_data_range is None:
            output_data_range = [230.0, 280.0]

        from geoips.data_manipulations.corrections import apply_data_range

        data = apply_data_range(
            out,
            min_val=output_data_range[0],
            max_val=output_data_range[1],
            min_outbounds=min_outbounds,
            max_outbounds=max_outbounds,
            norm=norm,
            inverse=inverse,
        )
        return data


PLUGIN_CLASS = Pmw37PctAlgorithmPlugin
