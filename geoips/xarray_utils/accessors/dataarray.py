# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""GeoIPS's xarray DataArray accessor."""

import numpy as np
import xarray as xr
from xarray.core.types import T_DuckArray

from geoips.xarray_utils.accessors._shared import GeoipsAccessor


@xr.register_dataarray_accessor("geoips")
class GeoipsDataArrayAccessor(GeoipsAccessor):
    def __init__(self, da):
        super().__init__(da)

    @property
    def as_array(self) -> T_DuckArray | np.typing.ArrayLike:
        return self._data.data
