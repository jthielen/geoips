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

"""Utilities for normalizing GeoIPS xarray coordinate conventions."""

from __future__ import annotations

import xarray as xr
from typing import Final

GEOIPS_COORD_NAMES: Final = (
    "latitude",
    "longitude",
    "satellite_zenith_angle",
    "satellite_azimuth_angle",
    "solar_zenith_angle",
    "solar_azimuth_angle",
)


def normalize_geoips_dataset_coords(dataset):
    """Return *dataset* with standard GeoIPS coordinate variables set as coords.

    GeoIPS readers and legacy plugins commonly expose geolocation variables as
    regular xarray data variables. For OBP routing and type conversion, latitude
    and longitude should remain available through normal xarray access patterns
    while not being mistaken for science/product data variables.

    Parameters
    ----------
    dataset : Any
        Object to normalize. Non-Dataset objects are returned unchanged.

    Returns
    -------
    Any
        The normalized xarray Dataset, or the original object if it is not a
        Dataset or has no standard GeoIPS coordinate variables in ``data_vars``.
    """
    if not isinstance(dataset, xr.Dataset):
        return dataset

    coord_names = [name for name in GEOIPS_COORD_NAMES if name in dataset.data_vars]
    if not coord_names:
        return dataset
    return dataset.set_coords(coord_names)
