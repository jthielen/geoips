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

"""Matplotlib-based windbarb annotated image output clean."""

from geoips.interfaces.class_based.output_formatters import (
    WindbarbOutputFormatterPlugin,
)

import logging

LOG = logging.getLogger(__name__)


class ImageryWindbarbsMultiLevelCleanOutputFormatterPlugin(
    WindbarbOutputFormatterPlugin
):
    """Imagery Windbarbs Multi Level Clean Output formatter plugin class."""

    interface = "output_formatters"
    family = "image"
    name = "imagery_windbarbs_multi_level_clean"

    def call(
        self,
        area_def,
        xarray_obj,
        product_name,
        output_fnames,
        product_name_title=None,
        mpl_colors_info=None,
        existing_image=None,
        remove_duplicate_minrange=None,
        fig=None,
        main_ax=None,
        mapobj=None,
        pressure_range_dict=None,
    ):
        """Plot clean windbarb imagery on matplotlib figure."""
        formatted_data_dict = self.format_windbarb_data(xarray_obj, product_name)

        if not pressure_range_dict:
            pressure_range_dict = {
                "Low": [701, 1013.25],
                "Mid": [401, 700],
                "High": [0, 400],
            }
        height_numbers, level_labels = self.assign_height_levels(
            formatted_data_dict, pressure_range_dict
        )
        formatted_data_dict["height_numbers"] = height_numbers

        success_outputs = self.output_clean_windbarbs(
            area_def,
            output_fnames,
            mpl_colors_info,
            xarray_obj.start_datetime,
            formatted_data_dict,
            fig,
            main_ax,
            mapobj,
            barb_color_variable="height_numbers",
        )

        return success_outputs


PLUGIN_CLASS = ImageryWindbarbsMultiLevelCleanOutputFormatterPlugin
