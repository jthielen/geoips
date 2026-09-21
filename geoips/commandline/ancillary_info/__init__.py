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

"""geoips.commandline.ancillary_info init file."""

import os
from geoips.utils.cache_files import get_cached_json

# This will collect ancillary information contained in YAML files, but will convert them
# to a cached JSON file first. This is done because reading YAML files is slow.
alias_mapping = get_cached_json(f"{os.path.dirname(__file__)}/alias_mapping.yaml")
cmd_instructions = get_cached_json(f"{os.path.dirname(__file__)}/cmd_instructions.yaml")
