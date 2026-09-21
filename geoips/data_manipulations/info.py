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

"""Introspection functions on data arrays."""

import logging
import numpy

LOG = logging.getLogger(__name__)


def percent_unmasked(data_array):
    """Determine percent of a numpy.ma.Masked array that is not masked.

    Parameters
    ----------
    data_array : numpy.ma.MaskedArray
        Final processed array from which to determine coverage

    Returns
    -------
    float
        percent of input data array that is not masked.
    """
    return 100 * (float(numpy.ma.count(data_array)) / data_array.size)


def percent_not_nan(data_array):
    """Determine percent of a numpy.ndarray that is not NaN values.

    Parameters
    ----------
    data_array : numpy.ndarray
        Final processed array from which to determine coverage, invalid values
        specified by "numpy.nan".

    Returns
    -------
    float
        percent of input data array that is not numpy.nan.
    """
    return 100.0 * (
        1.0 - (numpy.count_nonzero(numpy.isnan(data_array)) / data_array.size)
    )
