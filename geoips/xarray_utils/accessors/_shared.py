# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Shared utilities for GeoIPS's xarray accessors, including reused base classs."""

import xarray as xr


class GeoipsAccessor:
    def __init__(self, xarray_obj):
        self._data = xarray_obj
        self.validate = BooleanValidator(self)


class BooleanValidator:
    """Turn bool attributes into Pydantic-style validation checks."""

    def __init__(self, accessor: GeoipsAccessor) -> None:
        self._accessor = accessor

    def __getattr__(self, name: str) -> xr.DataTree | xr.Dataset | xr.DataArray:
        bool_result = getattr(self._accessor, name, None)
        if bool_result is None:
            raise AttributeError(f"Attribute {name} not found on accessor.")
        if callable(bool_result):
            # Workaround for methods rather than properties
            bool_result = bool_result()
        if bool_result:
            return self._accessor._data
        else:
            raise ValueError(f"{name} is not True.")
