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

"""GeoIPS configuration package.

Provides a layered, YAML-based configuration system with environment
variable overrides.

Usage::

    from geoips.config import config

    print(config.outdirs)
    print(config.features.no_color)
    print(config["GEOIPS_OUTDIRS"])  # backward-compatible dict access
"""

from geoips.config.config import GeoIPSConfig, get_config, make_dirs
from geoips.config.plugins import ConfigPlugin
from geoips.config.schema import GeoSettings

config = get_config()

__all__ = [
    "ConfigPlugin",
    "GeoIPSConfig",
    "GeoSettings",
    "config",
    "get_config",
    "make_dirs",
]
