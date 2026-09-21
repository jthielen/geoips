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

import logging
from xarray import DataTree

LOG = logging.getLogger(__name__)


def xarray_to_datatree(xarray_dict):
    """Convert a flat (non nested) dictionary of xarrays to DataTree format."""
    tmp_meta = xarray_dict.pop("METADATA")
    xarray_datatree = DataTree(
        name="METADATA", data=tmp_meta, children=DataTree.from_dict(xarray_dict)
    )

    return xarray_datatree
