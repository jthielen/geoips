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

"""Types subpackage init file.

The imports below trigger registration of the shared
``TypeConverterRegistry`` and all built-in / extended converters
at import time so that both ``DataTreeDitto`` and the
plugin-lifecycle hooks can discover them.

.. note::

    In a future version the import-time side-effects should be
    replaced with explicit ``register_converters()`` calls from the
    framework bootstrap entry point.
"""

from geoips.utils.types.converter_registry import (  # noqa: F401
    TypeConverterRegistry,
    converter_registry,
)
from geoips.utils.types.converters import FamilyConversionSpec  # noqa: F401
from geoips.utils.types import datatree_converters  # noqa: F401, E402
