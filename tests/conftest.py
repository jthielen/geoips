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

"""Pytest configuration for test data validation.

Provides command-line options and fixtures to control test behavior
when required test data files are missing.
"""

import pytest


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Collect and print all failed-test log file paths in one section.

    Parameters
    ----------
    terminalreporter : _pytest.terminal.TerminalReporter
        Pytest terminal reporter for writing output.
    exitstatus : int
        Overall test session exit status.
    config : pytest.Config
        Pytest configuration object.
    """
    failed_logs = set()
    for report in terminalreporter.getreports("failed"):
        longrepr = str(getattr(report, "longreprtext", ""))
        for line in longrepr.split("\n"):
            if "Log file:" in line:
                failed_logs.add(line.strip())
    if failed_logs:
        terminalreporter.section("Failed Test Log Files")
        for log in sorted(failed_logs):
            terminalreporter.write_line(f"  {log}")


def pytest_addoption(parser):
    """Add custom command-line options to pytest.

    Parameters
    ----------
    parser : pytest.Parser
        Pytest command-line argument parser.

    Notes
    -----
    Adds --no-fail-on-missing-data flag to skip tests instead of
    failing when test data is unavailable.
    """
    try:
        parser.addoption(
            "--no-fail-on-missing-data",
            action="store_true",
            default=False,
            help="Fail tests if test data is missing",
        )
    except ValueError as resp:
        if "option names {'--no-fail-on-missing-data'} already added" in str(resp):
            pass


@pytest.fixture
def fail_on_missing_data(request):
    """Determine whether to fail tests on missing data.

    Parameters
    ----------
    request : pytest.FixtureRequest
        Pytest fixture request object.

    Returns
    -------
    bool
        True if tests should fail on missing data, False to skip instead.
    """
    return not request.config.getoption("--no-fail-on-missing-data")
