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

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_gfs/data/gfswave.t06z.wcoast.0p16.f000.grib2 \
    --procflow single_source \
    --reader_name gfs_grib \
    --output_formatter imagery_clean \
    --filename_formatter geoips_fname \
    --sector_list conus \
    --minimum_coverage 0 \
    --product_name Model-WaveHeight \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/gfs.static.waveheight.imagery_clean" 

ss_retval=$?

exit $((ss_retval))
