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

"""Pydantic models used to validate GeoIPS OBP v1 coverage-checker plugins."""

# Python Standard Libraries
from typing import Optional

# Third-Party Libraries
from pydantic import Field

# GeoIPS imports
from geoips.pydantic_models.v1.bases import PermissiveFrozenModel


class CoverageCheckerArgumentsModel(PermissiveFrozenModel):
    """Coverage-Checker step argument definition.

    Pydantic model defining and validating Coverage Checker step arguments.
    """

    variable_name: str = Field(
        None, description="Variable name to check percent unmasked."
    )
    area_def: str = Field(None, description="Area definition identifier.")
    radius_km: Optional[float] = Field(
        300, description="Radius of center disk to check for coverage. "
    )
