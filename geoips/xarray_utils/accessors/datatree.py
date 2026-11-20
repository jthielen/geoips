# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""GeoIPS's xarray DataTree accessor."""

import functools
from typing import Annotated, Callable

from pydantic import AfterValidator
import xarray as xr

from geoips.xarray_utils.accessors._shared import GeoipsAccessor

REQUIRED_ATTRS = {
    "workflow": ("workflow_name", "geoips_version", "api_version"),
    "step": ("step_id", "plugin_name", "plugin_version"),
}


@xr.register_datatree_accessor("geoips")
class GeoipsDataTreeAccessor(GeoipsAccessor):
    def __init__(self, dt):
        super().__init__(dt)

    @property
    def is_workflow_tree(self):
        return all(key in self._data.attrs for key in REQUIRED_ATTRS["workflow"])

    @property
    def is_step_tree(self):
        return all(key in self._data.attrs for key in REQUIRED_ATTRS["step"])

    @staticmethod
    def workflow_tree_method(method: Callable) -> Callable:
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if not self.is_workflow_tree:
                raise TypeError(
                    f"{method.__name__} is a workflow_tree_method and this is not a GeoIPS workflow DataTree."
                )
            return method(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def step_tree_method(method: Callable) -> Callable:
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if not self.is_step_tree:
                raise TypeError(
                    f"{method.__name__} is a step_tree_method and this is not a GeoIPS step DataTree."
                )
            return method(self, *args, **kwargs)

        return wrapper


WorkflowDataTree = Annotated[
    xr.DataTree, AfterValidator(lambda dt: dt.geoips.validate.is_workflow_tree)
]
StepDataTree = Annotated[
    xr.DataTree, AfterValidator(lambda dt: dt.geoips.validate.is_step_tree)
]
