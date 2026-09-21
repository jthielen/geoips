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

"""Gridline Annotator interface module."""

from geoips.interfaces.base import BaseYamlInterface
from geoips.filenames.base_paths import PATHS as gpaths

# from geoips.pydantic_models.v1.gridline_annotators import GridlineAnnotatorPluginModel


class GridlineAnnotatorsInterface(BaseYamlInterface):
    """Interface for gridline annotator plugins."""

    name = "gridline_annotators"
    use_pydantic = gpaths["GEOIPS_USE_PYDANTIC"]

    # Keyword arguments that can be used to adjust the style of lat/lon labels applied
    # to annotated imagery. See geoips.image_utils.maps:draw_gridlines for how this is
    # implemented
    label_kwargs = {
        "alpha": ["number"],
        "backgroundcolor": ["string"],
        "color": ["string"],
        "fontfamily": ["string"],
        "fontsize": ["number", "string"],
        "fontstretch": ["integer", "string"],
        "fontstyle": ["string"],
        "fontvariant": ["string"],
        "fontweight": ["integer", "string"],
        "linespacing": ["number"],
        "mouseover": ["boolean"],
        "position": ["array"],
        "rotation": ["number", "string"],
        "rotation_mode": ["string"],
        "snap": ["boolean"],
        "wrap": ["boolean"],
        "zorder": ["number"],
    }


gridline_annotators = GridlineAnnotatorsInterface()
