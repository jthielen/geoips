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

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_sgli/data/20251018T0233/*DL*.h5 \
    --logging_level info \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/sgli.static.<product>.imagery_clean" \
    --reader_name sgli_l1b_hdf5 \
    --product_name IR-RGB \
    --filename_formatter geoips_fname \
    --output_formatter  imagery_clean \
    --minimum_coverage 0 \
    --sector_list korea 

retval=$?

exit $retval
