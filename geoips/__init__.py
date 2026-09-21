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

"""
The Geolocated Information Processing System (GeoIPS).

GeoIPS |unireg| Base Package
----------------------------

The GeoIPS Base Package provides a Python 3 based architecture supporting a wide
variety of satellite and weather data processing. The modular nature of the GeoIPS
base infrastructure also allows plug-and-play capability for user-specified custom
functionality.

Homepage: https://github.com/NRLMMD-GEOIPS/geoips

.. |unireg|    unicode:: U+000AE .. REGISTERED SIGN
"""

# Importing netCDF4 here so that it is always imported before
# xarray. Because if xarray is imported first, xarrays
# own netCDF4 functions conflict and cause segfaults
import netCDF4  # noqa
from matplotlib import rcParams
from geoips import errors
from geoips import filenames
from geoips import interfaces
from geoips import utils
from geoips import xarray_utils
from ._version import __version__, __version_tuple__

import logging  # noqa
from geoips.commandline.log_setup import add_logging_level

# Turn off image interpolation for matplotlib by default.
rcParams["image.interpolation"] = "none"

# Setting INTERACTIVE to 25 as this is between INFO (20) and WARNING (30). This way,
# WARNING output will still be shown if INFO or INTERACTIVE is set.
add_logging_level("INTERACTIVE", 25)

__all__ = [
    "interfaces",
    "errors",
    "filenames",
    "utils",
    "xarray_utils",
    "__version__",
    "__version_tuple__",
]
