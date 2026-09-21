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

"""Tests for the class-based OrderBased procflow."""

from geoips.plugins.modules.procflows.order_based import OrderBased


class TestOrderBased:
    """Tests for the OrderBased procflow class."""

    def test_class_has_correct_attrs(self):
        """Expected class-level interface, family, name, and data_tree attrs."""
        ob = OrderBased()
        assert ob.interface == "procflows"
        assert ob.family == "order_based"
        assert ob.name == "order_based"
        assert ob.data_tree is True
