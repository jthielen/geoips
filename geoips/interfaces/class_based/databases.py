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

"""Databases interface class."""

from geoips.interfaces.class_based_plugin import BaseClassPlugin
from geoips.interfaces.base import BaseClassInterface


class BaseDatabasePlugin(BaseClassPlugin, abstract=True):
    """Base class for GeoIPS database plugins."""

    data_tree = False

    pass


class DatabasesInterface(BaseClassInterface):
    """Interface for database table writers/quieriers."""

    name = "databases"
    plugin_class = BaseDatabasePlugin

    required_args = {
        "xarray_area_def_to_table": ["product_filename", "xarray_obj", "area_def"],
        "xarray_dict_to_table": ["product_filename", "xarray_dict"],
        "memusg_stats_to_table": [],
        "overpass_dict_to_postgres_table": [
            "schema_name",
            "table_name",
            "overpass_dict",
        ],
        "overpass_dict_to_sqlite_table": ["overpass_dict", "dbname"],
        "schema_table_sector_opasses_to_postgres_table": [
            "schema_name",
            "table_name",
            "sector_name",
            "sat_overpasses",
        ],
        "schema_table_storm_opasses_to_postgres_table": [
            "schema_name",
            "table_name",
            "storm_id",
            "storm_time",
            "satellite_overpasses",
        ],
        "storm_opasses_db_to_postgres_table": [
            "storm_id",
            "storm_time",
            "satellite_overpasses",
            "dbname",
        ],
        "query_overpass_table": ["window_start", "window_end"],
        "query_product_table": ["window_start", "window_end"],
    }
    required_kwargs = {
        "xarray_area_def_to_table": [],
        "xarray_dict_to_table": [],
        "memusg_stats_to_table": [],
        "overpass_dict_to_postgres_table": [],
        "overpass_dict_to_sqlite_table": [],
        "storm_opasses_db_to_postgres_table": [],
        "schema_table_storm_opasses_to_postgres_table": [],
        "schema_table_sector_opasses_to_postgres_table": [],
        "query_overpass_table": [],
        "query_product_table": [],
    }


databases = DatabasesInterface()
