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
# https://www.nrlmry.navy.mil/tcdat/tc2021/WP/WP022021/txt/SCT_winds_knmi_metop-c_WP02_202104210141
geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_scat/data/20220911_metopb_byu_uhr_tc2022wp14muifa/MUIFA_20220911_51797_B_A-product.nc \
          --reader_name ascat_uhr_netcdf \
          --product_name nrcs \
          --filename_formatter tc_fname \
          --output_formatter imagery_clean \
          --tc_spec_template tc_web \
          --trackfile_parser bdeck_parser \
          --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp142022.dat \
          --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/ascat_uhr.tc.nrcs.imagery_clean" \
          --product_spec_override '{}' \
          --output_formatter_kwargs '{}' \
          --filename_formatter_kwargs '{}' \
          --metadata_output_formatter_kwargs '{}' \
          --metadata_filename_formatter_kwargs '{}'
ss_retval=$?

exit $((ss_retval))
