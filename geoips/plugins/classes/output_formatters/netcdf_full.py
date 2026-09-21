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

"""Full NetCDF output format, writing out all channels in full dataset."""

from geoips.interfaces.class_based.output_formatters import NetcdfOutputFormatterPlugin

import logging

LOG = logging.getLogger(__name__)


class NetcdfFullOutputFormatterPlugin(NetcdfOutputFormatterPlugin):
    """Netcdf Full Output formatter plugin class."""

    interface = "output_formatters"
    family = "xarray_data"
    name = "netcdf_full"

    def call(
        self,
        xarray_obj,
        product_names,
        output_fnames,
        clobber=False,
        use_compression=True,
        compression_kwargs=None,
    ):
        """Write GeoIPS style NetCDF to disk."""
        for ncdf_fname in output_fnames:
            self.write_xarray_netcdf(
                xarray_obj,
                ncdf_fname,
                clobber=clobber,
                use_compression=use_compression,
                compression_kwargs=compression_kwargs,
            )
        return output_fnames


PLUGIN_CLASS = NetcdfFullOutputFormatterPlugin
