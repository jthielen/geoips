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

"""Testing module for Pydantic CoverageCheckersArgumentsModel."""

# Third-Party Libraries
import pytest

# GeoIPS Libraries
from geoips.pydantic_models.v1.coverage_checkers import CoverageCheckerArgumentsModel
from tests.unit_tests.pydantic_models.v1.utils import (
    load_test_cases,
    validate_bad_plugin,
    validate_base_plugin,
)

interface = "coverage_checkers"

test_cases_bad = load_test_cases(interface, "bad")


def test_good_title_formatter(valid_coverage_checker_arguments):
    """Validate a known-good CoverageCheckerArgumentsModel configuration.

    Parameters
    ----------
    valid_coverage_checker_arguments: dict
        - A dictionary representing a valid coverage checker plugin.
    """
    validate_base_plugin(
        valid_coverage_checker_arguments, CoverageCheckerArgumentsModel
    )


@pytest.mark.parametrize(
    "test_tup", test_cases_bad.values(), ids=list(test_cases_bad.keys())
)
def test_bad_title_formatter_plugins(valid_coverage_checker_arguments, test_tup):
    """Ensure invalid CoverageCheckerArgumentsModel configs fail with expected error.

    Parameters
    ----------
    valid_coverage_checker_arguments: dict
        - A dictionary representing a valid coverage checker plugin.
    test_tup:
        - A tuple formatted (description, key, value, class, err_str), formatted (str,
          any, str, str) used to run and validate tests.
    """
    validate_bad_plugin(
        valid_coverage_checker_arguments, test_tup, CoverageCheckerArgumentsModel
    )
