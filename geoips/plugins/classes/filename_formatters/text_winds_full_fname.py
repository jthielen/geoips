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

"""Filename formatter for text windspeed products."""

from geoips.interfaces.class_based.filename_formatters import (
    WindsFilenameFormatterPlugin,
)

import logging

from os.path import join as pathjoin

from geoips.filenames.base_paths import PATHS as gpaths

LOG = logging.getLogger(__name__)


class TextWindsFullFnameFilenameFormatterPlugin(WindsFilenameFormatterPlugin):
    """Text Winds Full Fname Filename formatter plugin class."""

    interface = "filename_formatters"
    family = "xarray_metadata_to_filename"
    name = "text_winds_full_fname"

    def call(
        self,
        xarray_obj,
        extension=".txt",
        basedir=pathjoin(gpaths["ANNOTATED_IMAGERY_PATH"], "text_winds"),
    ):
        """Create a single text winds file for all data in the current xarray.

        This text windspeed filename includes YYYYMMDD.HHMN in the filename
        in order to include only the current datafile in the file.

        See Also
        --------
        geoips.plugins.classes.filename_formatters.text_winds_full_fname.
            assemble_windspeeds_text_full_fname
            Shared utility to create filenames with similar formatting requirements.
        """
        return self.assemble_windspeeds_text_full_fname(
            basedir=basedir,
            source_name=xarray_obj.source_name,
            platform_name=xarray_obj.platform_name,
            data_provider=xarray_obj.data_provider,
            product_datetime=xarray_obj.start_datetime,
            dt_format="%Y%m%d.%H%M",
            extension=extension,
            creation_time=None,
        )


PLUGIN_CLASS = TextWindsFullFnameFilenameFormatterPlugin
