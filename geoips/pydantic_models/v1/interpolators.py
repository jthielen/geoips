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

"""Pydantic models for interpolator plugins validation."""

# Python Standard Libraries
from typing import List, TypeAlias, Union

# Third-Party Libraries
from pydantic import ConfigDict, Field, StrictBool
import xarray as xr

# GeoIPS imports
from geoips.pydantic_models.v1.bases import PermissiveFrozenModel

dataType: TypeAlias = Union[xr.DataArray, xr.Dataset]


class InterpGaussInterpolator(PermissiveFrozenModel):
    """Validate InterpGauss Interpolator."""

    sigmaval: int = Field(
        10000,
        description="Used for interp_type 'gauss' - multiplication factor for sigmas"
        " option: * sigmas = [sigmas]*len(list_of_arrays)",
    )
    drop_nan: StrictBool = Field(
        False, description="Whether to drop the nan values (default:False)"
    )


class InterpGridInterpolator(PermissiveFrozenModel):
    """Validate InterpGrid Interpolator."""

    method: str = Field(
        "linear", description="Method of interpolation; defaults to linear"
    )


class InterpolatorArgumentsModel(InterpGaussInterpolator, InterpGridInterpolator):
    """Validate common Interpolator arguments."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # area_def should be a required field after SSP -> OBP transition
    # It is currently set optional because some SSP workflows compute
    # area_def dynamically at runtime
    area_def: str | None = Field(None, description="Area definition identifier.")
    varlist: List[str] | None = Field(
        None, description="variables required for specific interpolation processing"
    )
