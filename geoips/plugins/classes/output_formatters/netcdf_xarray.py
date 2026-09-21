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

"""Standard xarray-based NetCDF output format."""

from geoips.interfaces.class_based.output_formatters import NetcdfOutputFormatterPlugin

import logging
from datetime import datetime
import json
import numpy as np

LOG = logging.getLogger(__name__)


class NetcdfXarrayOutputFormatterPlugin(NetcdfOutputFormatterPlugin):
    """Netcdf Xarray Output formatter plugin class."""

    interface = "output_formatters"
    family = "xarray_data"
    name = "netcdf_xarray"

    def call(
        self,
        xarray_obj,
        product_names,
        output_fnames,
        clobber=False,
        use_compression=True,
        compression_kwargs=None,
    ):
        """Write xarray-based NetCDF outputs to disk."""
        for ncdf_fname in output_fnames:
            self.write_xarray_netcdf(
                xarray_obj,
                ncdf_fname,
                clobber=clobber,
                use_compression=use_compression,
                compression_kwargs=compression_kwargs,
            )
        return output_fnames

    def make_json_friendly(self, value):
        """Return a JSON-serializable version of `value`."""
        # Handle NumPy scalars
        if isinstance(value, np.generic):
            return value.item()  # convert np.int32 -> int, np.float64 -> float, etc.

        # Handle common non-serializable types
        if isinstance(value, (dict, list, tuple)):
            # Recursively make contents JSON-friendly
            return json.loads(json.dumps(value, default=self.make_json_friendly))
        if isinstance(value, datetime):
            return value.isoformat()

        # Simple types that JSON already understands
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value

        # Fallback: string representation
        return str(value)


PLUGIN_CLASS = NetcdfXarrayOutputFormatterPlugin
