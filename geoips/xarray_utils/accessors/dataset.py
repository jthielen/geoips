# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""GeoIPS's xarray Dataset accessor."""

import numpy as np
import xarray as xr
from xarray.core.types import T_DuckArray

from geoips.xarray_utils.accessors._shared import GeoipsAccessor


@xr.register_dataset_accessor("geoips")
class GeoipsDatasetAccessor(GeoipsAccessor):
    def __init__(self, ds):
        super().__init__(ds)

    @property
    def as_array_list(self) -> list[T_DuckArray | np.typing.ArrayLike]:
        return list(self._data.to_dict().values())
