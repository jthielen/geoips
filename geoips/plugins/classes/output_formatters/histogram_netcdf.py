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

"""Produce histogram from the given dataset with specified bin size."""

from geoips.interfaces.class_based.output_formatters import NetcdfOutputFormatterPlugin

import logging
import numpy

LOG = logging.getLogger(__name__)


class HistogramJsonOutputFormatterPlugin(NetcdfOutputFormatterPlugin):
    """Histogram Json Output formatter plugin class."""

    interface = "output_formatters"
    family = "xarray_data"
    name = "histogram_json"

    def call(
        self,
        xarray_obj,
        product_names,
        output_fnames,
        min_val=None,
        max_val=None,
        num_bins=501,
    ):
        """Produce histogram.

        Parameters
        ----------
        xarray_obj: xarray Dataset

        Returns
        -------
        xarray.Dataset
            Resulting histogram
        """
        import xarray

        prod_xarray = xarray.Dataset()

        from geoips.geoips_utils import copy_standard_metadata

        copy_standard_metadata(xarray_obj, prod_xarray)
        for product_name in product_names:
            prod_xarray[product_name] = xarray_obj[product_name]

            if product_name == "latitude" or product_name == "longitude":
                continue
            xda = xarray_obj[product_name]
            hist = numpy.histogram(xda, numpy.linspace(min_val, max_val, num_bins + 1))
            prod_xarray[f"{product_name}_histogram"] = xarray.DataArray(
                hist[0], dims=("dim_2")
            )
            prod_xarray["bins"] = xarray.DataArray(hist[1], dims=("dim_3"))

        for ncdf_fname in output_fnames:
            self.write_xarray_netcdf(prod_xarray, ncdf_fname)
        return output_fnames


PLUGIN_CLASS = HistogramJsonOutputFormatterPlugin
