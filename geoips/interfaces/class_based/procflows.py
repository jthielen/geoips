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

"""Procflows interface class."""

from geoips.interfaces.class_based_plugin import BaseClassPlugin
from geoips.interfaces.base import BaseClassInterface


class BaseProcflowPlugin(BaseClassPlugin, abstract=True):
    """Base class for GeoIPS procflow plugins."""

    data_tree = True

    pass


class ProcflowsInterface(BaseClassInterface):
    """Class-based interface for processing workflows (procflows).

    Procflows drive a specific collection of steps for a particular type of
    processing.  Currently available are:

    * order_based: the class-based, YAML-driven Order-Based Procflow (OBP) that
      executes a validated workflow spec as a DAG of steps. This is the
      forward-looking procflow intended to replace the module-based ones below.
    * single_source: (legacy, module-based) single input type and single output
      type.
    * config_based: (legacy, module-based) efficient method for producing all
      possible outputs for a given set of data files.
    """

    name = "procflows"
    plugin_class = BaseProcflowPlugin

    required_args = {
        "standard": ["fnames"],
        "order_based": ["workflow_spec", "filenames"],
    }
    required_kwargs = {"standard": ["command_line_args"], "order_based": []}


procflows = ProcflowsInterface()
