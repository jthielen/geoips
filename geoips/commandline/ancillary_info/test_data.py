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

"""Ancillary module containing test dataset information.

Dictionary mapping of GeoIPS Test Datasets.

Mapping goes {"test_dataset_name": "test_dataset_url"}
"""

from pathlib import Path
from typing import Dict
import geoips_yaml_utils as yaml

# This is not a plugin module
interface = None


def load_test_dataset_urls() -> Dict[str, str]:
    """
    Load test dataset URLs from the YAML configuration file.

    Returns
    -------
    Dict[str, str]
        Dictionary mapping test dataset names to their URLs
    """
    current_file_path = Path(__file__).resolve()
    url_file_path = current_file_path.parent / "test-data-urls.yaml"

    with open(url_file_path, "r") as file:
        urls = yaml.safe_load(file)

    return urls["test_data_urls"]


# Initialize the test dataset dictionary
test_dataset_dict = load_test_dataset_urls()
