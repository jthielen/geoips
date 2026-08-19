# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Utilities for streamlining GeoIPS scripting using xarray accessors."""

import xarray as xr

from geoips.utils.types.script_datatree import (
    add_data_step,
    attach_plugin_result,
    get_current_data,
    get_output_products
)


@xr.register_datatree_accessor("geoips")
class GeoIPSDataTreeAccessor:
    """Provide a custom namespace on DataTree for GeoIPS-specific attributes and methods."""

    def __init__(self, dt):
        # Initialize with DataTree, not for use directly.
        self._dt = dt

    def pipe(self, f, *args, **kwargs):
        """Wrap DataTree.pipe for specific script tree keyword argument, for applying typical plugins."""
        return self._dt.pipe((f, "data"), *args, **kwargs)

    def attach_plugin_result(self, step_data, **kwargs):
        """Alias to geoips.scripting.attach_plugin_results, for applying yaml-based plugins.
        
        @todo update comment when "some yaml-based plugins do not yet route through..." no longer applies
        """
        return attach_plugin_result(self._dt, step_data, **kwargs)

    @property
    def current_data(self):
        """Alias to geoips.scripting.get_current_data."""
        return get_current_data(self._dt)

    def add_data_step(self, data, *, step_id, retention_policy=None):
        """Alias to geoips.scripting.add_data_step."""
        return add_data_step(self._dt, data, step_id=step_id, retention_policy=retention_policy)

    def output_products(self, step_id=None):
        """Alias to geoips.scripting.get_output_products."""
        return get_output_products(self._dt, step_id=step_id)
