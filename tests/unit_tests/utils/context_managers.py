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

"""Unit Tests for log output for optional dependencies found throughout geoips."""

import logging
import pytest
from geoips.utils import context_managers

opt_importer = context_managers.import_optional_dependencies
importer_path = context_managers.__file__

LOG = logging.getLogger(__name__)

# err_str = f"Failed to import {err.name} at {filename}:{lineno}. "
# err_str += "If you need it, install it."


@pytest.mark.parametrize("loglevel", ["info", "debug", "warning", "error"])
def test_import_failure_using_log(loglevel, caplog):
    """Ensure that the test fails and that the log output is correct."""
    caplog.set_level(getattr(logging, loglevel.upper()))
    with opt_importer(loglevel=loglevel):
        """Attempt to import a package and print to LOG.info if the import fails."""
        import non_existent_package  # noqa

    err_str = f"Failed to import non_existent_package at {importer_path}:24. "
    err_str += "If you need it, install it."

    assert err_str in caplog.text


@pytest.mark.parametrize("loglevel", ["info", "debug", "warning", "error"])
def test_import_success_using_log(loglevel, caplog):
    """Ensure that the test succeeds and that the log output is empty."""
    caplog.set_level(getattr(logging, loglevel.upper()))
    with opt_importer(loglevel=loglevel):
        """Attempt to import a package and print to LOG.info if the import fails."""
        import numpy  # noqa

    assert caplog.text == ""
