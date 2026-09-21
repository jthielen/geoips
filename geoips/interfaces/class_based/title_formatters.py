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

"""Title formatters interface class."""

from geoips.interfaces.class_based_plugin import BaseClassPlugin
from geoips.interfaces.base import BaseClassInterface


class BaseTitleFormatterPlugin(BaseClassPlugin, abstract=True):
    """Base class for GeoIPS title_formatter plugins."""

    data_tree = False

    pass


class TitleFormattersInterface(BaseClassInterface):
    """Interface for creating GeoIPS formatted titles."""

    name = "title_formatters"
    plugin_class = BaseTitleFormatterPlugin

    required_args = {"standard": []}
    required_kwargs = {"standard": []}


title_formatters = TitleFormattersInterface()
