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

"""Takes in a dictionary of xarrays and converts to xarray datatree."""

import pytest
import xarray
import numpy as np
from geoips.commandline.log_setup import setup_logging
from geoips.xarray_utils import xr_to_dtree

LOG = setup_logging()


@pytest.fixture
def load_testfiles():
    """Generate test xarrays for testing."""
    # only want a small sample for testing
    xarray_dict = {
        "test_{}".format(k): xarray.Dataset(
            data_vars=dict(temp=(["x", "y"], np.empty((2, 2)))),
            coords=dict(lon=(["x", "y"], np.empty((2, 2)))),
        )
        for k in range(0, 4)
    }
    xarray_dict["METADATA"] = xarray.Dataset(
        attrs={"units": "test", "dataset": "synthetic"}
    )
    return xarray_dict


def test_xarray_to_datatree(load_testfiles):
    """Test conversion a xarray dictionary to a datatree.

    Parameters
    ----------
    load_testfiles : dict(xarrays)
        Dictionary of xarrays

    Returns
    -------
    None
    """
    metadata_copy = load_testfiles["METADATA"].copy()
    xarray_datatree = xr_to_dtree.xarray_to_datatree(load_testfiles)
    assert xarray_datatree.attrs == metadata_copy.attrs
    assert xarray_datatree.keys() == load_testfiles.keys()
