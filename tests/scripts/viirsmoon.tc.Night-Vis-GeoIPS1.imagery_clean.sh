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

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210525/191200/VJ102DNB.A2021145.1912.002.2021146004551.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210525/191200/VJ102IMG.A2021145.1912.002.2021146004551.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210525/191200/VJ102MOD.A2021145.1912.002.2021146004551.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210525/191200/VJ103DNB.A2021145.1912.002.2021146002749.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210525/191200/VJ103IMG.A2021145.1912.002.2021146002749.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210525/191200/VJ103MOD.A2021145.1912.002.2021146002749.nc \
             --reader_name viirs_netcdf \
             --product_name Night-Vis-GeoIPS1 \
             --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/viirsmoon.tc.<product>.imagery_clean" \
             --output_formatter imagery_clean \
             --filename_formatter tc_clean_fname \
             --trackfile_parser bdeck_parser \
             --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bio022021.dat

ss_retval=$?

exit $((ss_retval))
