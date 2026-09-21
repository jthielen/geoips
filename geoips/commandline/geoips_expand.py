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

"""GeoIPS CLI "expand" command.

Single 'geoips expand <workflow_name>' command which will fully expand a workflow in the
case it has embedded workflows or products included in its steps.
"""

# cspell:ignore gpaths

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
import yaml

from geoips.commandline.geoips_command import GeoipsExecutableCommand
from geoips.errors import PluginError
from geoips.filenames.base_paths import PATHS as gpaths
from geoips.interfaces import workflows


class GeoipsExpand(GeoipsExecutableCommand):
    """Expand command class for fully dumping a workflow plugin to the terminal.

    This should be used to confirm the order of steps applied in a workflow plugin.
    Since embedded workflows and products can be included in workflow plugins, it's not
    always easy to see the order of operations that will be applied from a top-level
    workflow plugin. This is an easy way to mitigate that.
    """

    name = "expand"
    command_classes = []

    def add_arguments(self):
        """Add arguments to the expand-subparser for the Expand Command."""
        self.parser.add_argument(
            "workflow_name",
            type=str,
            help="Name of the workflow plugin to expand.",
        )
        self.parser.add_argument(
            "--color",
            default=False,
            action="store_true",
            help="Whether or not we want to highlight the output of this command.",
        )

    def __call__(self, args):
        """Run the `geoips expand <workflow-name>` command.

        Parameters
        ----------
        args: Namespace()
            - The argument namespace to parse through
        """
        print()
        workflow_name = args.workflow_name
        # Set rebuild registries to false if we are dealing with a command from a unit
        # test
        rbr = (
            False
            if "non_existent" in workflow_name
            else gpaths["GEOIPS_REBUILD_REGISTRIES"]
        )
        try:
            workflow = workflows.get_plugin(
                workflow_name, _expand=True, rebuild_registries=rbr
            )
        except PluginError:
            self.parser.error(
                f"Error: could not load workflow plugin under name '{workflow_name}'."
            )

        formatted_wf = yaml.dump(
            dict(workflow), indent=2, default_flow_style=False, sort_keys=False
        )

        if args.color:
            lexer = get_lexer_by_name("yaml")
            highlighted = highlight(formatted_wf, lexer, TerminalFormatter())
            print(highlighted)
        else:
            print(formatted_wf)
