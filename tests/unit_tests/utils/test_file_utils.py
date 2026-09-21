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

"""pytest test-suite for `geoips.utils.file_utils.py`."""

from geoips.utils.file_utils import path_exists


def test_path_exists_returns_true_for_existing_file(tmp_path):
    """Existing files return True."""
    existing_file = tmp_path / "exists.nc"
    existing_file.touch()
    assert path_exists(existing_file)


def test_path_exists_returns_false_for_missing_path(tmp_path):
    """Missing paths return False."""
    missing_file = tmp_path / "does_not_exist.nc"
    assert not path_exists(missing_file)
