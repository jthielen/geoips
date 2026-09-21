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

"""Test Order-based procflow ReaderArgumentsModel."""

import copy

# GeoIPS Libraries
from geoips.pydantic_models.v1.readers import ReaderArgumentsModel


def test_reader_arguments_model_chans_deprecation(
    caplog, valid_reader_arguments_model_data
):
    """Tests ReaderArgumentsModel with valid inputs."""
    invalid_test_data = copy.deepcopy(valid_reader_arguments_model_data)
    invalid_test_data["chans"] = invalid_test_data.pop("variables")

    with caplog.at_level("WARNING"):
        model = ReaderArgumentsModel(**invalid_test_data)

    # Assert model still created
    assert model

    # Check that a warning was logged
    assert any(
        "'chans' is deprecated and will be removed in GeoIPS 2.0." in msg
        for msg in caplog.messages
    )
