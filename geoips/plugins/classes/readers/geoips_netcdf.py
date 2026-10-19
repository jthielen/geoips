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

"""Read pre-processed GeoIPS-formatted NetCDF data."""

from geoips.interfaces.class_based.readers import BaseReaderPlugin

# Python Standard Libraries
from datetime import datetime
from os.path import basename
import logging

# Third-Party Libraries
import xarray

LOG = logging.getLogger(__name__)


class GeoipsNetcdfReaderPlugin(BaseReaderPlugin):
    """Geoips Netcdf reader plugin class."""

    interface = "readers"
    family = "standard"
    name = "geoips_netcdf"

    source_names = ["any"]

    def call(
        self,
        fnames,
        metadata_only=False,
        chans=None,
        area_def=None,
        self_register=False,
    ):
        """Read preprocessed geoips netcdf output.

        Parameters
        ----------
        fnames : list
            * List of strings, full paths to files
        metadata_only : bool, default=False
            * NOT YET IMPLEMENTED
            * Return before actually reading data if True
        chans : list of str, default=None
            * NOT YET IMPLEMENTED
            * List of desired channels (skip unneeded variables as needed).
            * Include all channels if None.
        area_def : pyresample.AreaDefinition, default=None
            * NOT YET IMPLEMENTED
            * Specify region to read
            * Read all data if None.
        self_register : str or bool, default=False
            * NOT YET IMPLEMENTED
            * register all data to the specified dataset id (as specified in the
              return dictionary keys).
            * Read multiple resolutions of data if False.

        Returns
        -------
        dict of xarray.Datasets
            * dictionary of xarray.Dataset objects with required Variables and
              Attributes.
            * Dictionary keys can be any descriptive dataset ids.

        See Also
        --------
        :ref:`xarray_standards`
            Additional information regarding required attributes and variables
            for GeoIPS-formatted xarray Datasets.
        """
        LOG.info("Reading files %s", fnames)

        xarray_objs = {}
        for fname in fnames:
            xarray_objs[basename(fname)] = self.read_xarray_netcdf(fname)

        xarray_objs["METADATA"] = list(xarray_objs.values())[0][[]]

        return xarray_objs

    # This is a static method as geoips.xarray_utils.data:get_vis_ir_bg references this
    # fu
    @staticmethod
    def read_xarray_netcdf(ncdf_fname):
        """Read NetCDF file written out using the xarray python package."""
        try:
            xarray_obj = xarray.open_dataset(ncdf_fname)
        except IOError:
            raise IOError
        for attr in xarray_obj.attrs.keys():
            if "datetime" in attr:
                xarray_obj.attrs[attr] = datetime.strptime(xarray_obj.attrs[attr], "%c")
            if attr == "None":
                xarray_obj.attrs[attr] = None
            if attr == "True":
                xarray_obj.attrs[attr] = True
            if attr == "False":
                xarray_obj.attrs[attr] = False
        return xarray_obj


PLUGIN_CLASS = GeoipsNetcdfReaderPlugin
