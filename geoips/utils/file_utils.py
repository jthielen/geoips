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

"""Filesystem path helpers used across GeoIPS."""

# Python Standard Libraries
from pathlib import Path


def path_exists(path: str | Path) -> bool:
    """Return True if a filesystem path exists.

    Parameters
    ----------
    file_path : str
        File or Directory path to evaluate. This could be a file, directory, or other
         filesystem object.

    Returns
    -------
    bool
        True if `path` exists on the filesystem, otherwise False.
    """
    return Path(path).exists()
