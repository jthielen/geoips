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

"""Pydantic models used to validate GeoIPS OBP v1 title-formatter plugins."""

# Third-Party Libraries
from pydantic import Field

# GeoIPS imports
from geoips.pydantic_models.v1.bases import PermissiveFrozenModel


class TitleFormatterArgumentsModel(PermissiveFrozenModel):
    """Title-Formatter step argument definition.

    Pydantic model defining and validating Title Formatter step arguments.
    """

    area_def: str = Field(None, description="Area definition identifier.")
    product_name_title: str = Field(None, description="Product name title.")
    product_datatype_title: str = Field(
        None, description="Product data type label to include in the title."
    )
    bg_product_name_title: str = Field(
        None,
        description="Background product name title when background layer is provided.",
    )
    bg_datatype_title: str = Field(
        None, description="Background data type label for the background product title."
    )
    title_copyright: str = Field(
        None, description="Copyright string to append to the generated title"
    )
