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

#!/bin/bash

# Default values - if you do not have this exact test case available, call with available data files / sectors.

# This exact test case required for valid comparisons - remove "compare_path" argument if running a different
# set of arguments.

# Include metadata default output for this test, since it is an invest storm and we
# want to verify correct invest storm ID generation. We don't need to include
# the metadata output for all of the AWS test scripts, we'll just include it
# in two test scripts - one with metadata_default (165) and one with metadata_tc (180).

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_arctic_weather_satellite/data/20250428/W_NO-KSAT-Tromso%2CSAT%2CAWS1-MWR-1B-RAD_C_OHB__20250428133939*.nc \
    --procflow single_source \
    --reader_name aws_netcdf \
    --product_name TB165 \
    --filename_formatter tc_clean_fname  \
    --output_formatter imagery_clean \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --tc_spec_template tc_web \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp992025.dat \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/aws.tc.<product>.imagery_clean" \
    --product_spec_override '{}' \
    --output_formatter_kwargs '{}' \
    --filename_formatter_kwargs '{}' \
    --metadata_output_formatter_kwargs '{}' \
    --metadata_filename_formatter_kwargs '{}'
ss_retval=$?

exit $((ss_retval))
