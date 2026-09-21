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

"""Module containing matplotlib information for RGB or RGBA imagery."""

from geoips.interfaces.class_based.colormappers import BaseColormapperPlugin

import logging

LOG = logging.getLogger(__name__)


class CmapRgbColormapperPlugin(BaseColormapperPlugin):
    """Cmap RGB colormapper plugin class."""

    interface = "colormappers"
    family = "matplotlib"
    name = "cmap_rgb"

    def call(self):
        """For rgb imagery, we require no color information.

        colormap is entirely specified by the RGB(A) arrays, so no specific
        matplotlib color information required.

        Parameters
        ----------
            No arguments

        Returns
        -------
        mpl_colors_info : dict
            * Specifies matplotlib Colors parameters for use in both plotting
              and colorbar generation
            * For RGBA arrays, all fields are "None"
        """
        mpl_colors_info = {
            "cmap": None,
            "norm": None,
            "cbar_ticks": None,
            "cbar_tick_labels": None,
            "cbar_label": None,
            "boundaries": None,
            "cbar_spacing": "proportional",
            "colorbar": False,
        }
        return mpl_colors_info


PLUGIN_CLASS = CmapRgbColormapperPlugin
