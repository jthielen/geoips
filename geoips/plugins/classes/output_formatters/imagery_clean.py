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

"""Matplotlib-based clean image output."""

from geoips.interfaces.class_based.output_formatters import BaseOutputFormatterPlugin

import logging

LOG = logging.getLogger(__name__)


class ImageryCleanOutputFormatterPlugin(BaseOutputFormatterPlugin):
    """Imagery Clean Output formatter plugin class."""

    interface = "output_formatters"
    family = "image"
    name = "imagery_clean"

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
    ):
        """Plot clean image on matplotlib figure."""
        success_outputs = []
        plot_data = xarray_obj[product_name].to_masked_array()
        plot_kwargs = {}
        if hasattr(xarray_obj, "fuse_order"):
            plot_kwargs = {"zorder": int(xarray_obj.fuse_order)}
        from geoips.image_utils.mpl_utils import create_figure_and_main_ax_and_mapobj
        from geoips.image_utils.colormap_utils import set_matplotlib_colors_standard
        from geoips.image_utils.mpl_utils import plot_image, save_image

        if not mpl_colors_info:
            # Create the matplotlib color info dict - the fields in this dictionary
            # (cmap, norm, features, etc) will be used in plot_image to ensure the image
            # matches the colorbar.
            mpl_colors_info = set_matplotlib_colors_standard(
                data_range=[plot_data.min(), plot_data.max()],
                cmap_name=None,
                cbar_label=None,
            )

        if fig is None and main_ax is None and mapobj is None:
            # Create matplotlib figure and main axis, where the main image will be
            # plotted
            fig, main_ax, mapobj = create_figure_and_main_ax_and_mapobj(
                area_def.width, area_def.height, area_def, noborder=True
            )

        # Plot the actual data on a map
        plot_image(
            main_ax, plot_data, mapobj, mpl_colors_info=mpl_colors_info, **plot_kwargs
        )

        if output_fnames is not None:
            for clean_fname in output_fnames:
                LOG.info("Saving the clean image %s", clean_fname)
                # Save the clean image with no gridlines or coastlines
                success_outputs += save_image(
                    fig,
                    clean_fname,
                    is_final=False,
                    image_datetime=xarray_obj.start_datetime,
                    remove_duplicate_minrange=remove_duplicate_minrange,
                )

        return success_outputs


PLUGIN_CLASS = ImageryCleanOutputFormatterPlugin
