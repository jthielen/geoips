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

"""Standard GeoIPS static title production."""

from geoips.interfaces.class_based.title_formatters import BaseTitleFormatterPlugin

# Python Standard Libraries
import logging

# GeoIPS Libraries
from geoips.filenames.base_paths import PATHS as gpaths

LOG = logging.getLogger(__name__)


class StaticStandardTitleFormatterPlugin(BaseTitleFormatterPlugin):
    """Static Standard Title formatter plugin class."""

    interface = "title_formatters"
    family = "standard"
    name = "static_standard"

    def call(
        self,
        area_def,
        xarray_obj,
        product_name_title,
        product_datatype_title=None,
        bg_xarray=None,
        bg_product_name_title=None,
        bg_datatype_title=None,
        title_copyright=None,
    ):
        """Generate standard GeoIPS formatted title."""
        if title_copyright is None:
            title_copyright = gpaths["GEOIPS_COPYRIGHT"]
        title_line1 = "{0} {1}".format(product_datatype_title, product_name_title)
        title_line2 = "{0}".format(
            xarray_obj.start_datetime.strftime("%Y/%m/%d %H:%M:%SZ")
        )
        if bg_xarray is not None:
            title_line3 = "{0} {1} at {2}".format(
                bg_datatype_title,
                bg_product_name_title,
                bg_xarray.start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            )
            # title_string = f'{title_line1}\n{title_line2}\n{title_line3}\n
            #                                                         {title_copyright}'
            title_string = (
                f"{title_line1}\n{title_line2} {title_copyright}\n{title_line3}"
            )
        else:
            # title_string = f'{title_line1}\n{title_line2}\n{title_copyright}'
            title_string = f"{title_line1}\n{title_line2} {title_copyright}"
        LOG.info("Not dynamic, using standard title_string: %s", title_string)

        return title_string


PLUGIN_CLASS = StaticStandardTitleFormatterPlugin
