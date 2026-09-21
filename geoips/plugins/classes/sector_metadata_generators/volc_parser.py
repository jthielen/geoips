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

"""Parser for dyanmic volcanoes csv files."""

from geoips.interfaces.class_based.sector_metadata_generators import (
    BaseSectorMetadataGeneratorPlugin,
)

import logging

import pandas as pd

LOG = logging.getLogger(__name__)


class VolcParserSectorMetadataGeneratorPlugin(BaseSectorMetadataGeneratorPlugin):
    """Volc Parser Sector Metadata generator plugin class."""

    interface = "sector_metadata_generators"
    family = "volc"
    name = "volc_parser"

    def call(self, trackfile_name):
        """Parse a sample volcano csv file.

        Parameters
        ----------
        trackfile_name: str, or path
            * Path to trackfile csv file with the format:
            * columns: lat lon time
            * lat/lon format: decimal
            * time format: YYYYMMDDTHHMM
        """
        csv_parser = pd.read_csv(trackfile_name)

        all_fields = []

        for i in csv_parser.iterrows():
            tmp_fields = i[1]
            fields = {}

            fields["clat"] = tmp_fields["Lat"]
            fields["clon"] = tmp_fields["Lon"]
            fields["time"] = pd.to_datetime(tmp_fields["Time"]).to_pydatetime()
            all_fields.append(fields)

        volcano_name = tmp_fields["Name"]
        if "volcano" not in volcano_name.lower():
            volcano_name = volcano_name.upper() + "_VOLCANO"
        return all_fields, volcano_name, fields["time"].strftime("%Y"), "BEST"


PLUGIN_CLASS = VolcParserSectorMetadataGeneratorPlugin
