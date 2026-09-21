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
geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/200500/MYD021KM.A2021004.2005.061.NRT.hdf \
             $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/200500/MYD03.A2021004.2005.061.NRT.hdf \
             $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201000/MYD021KM.A2021004.2010.061.NRT.hdf \
             $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201000/MYD03.A2021004.2010.061.NRT.hdf \
             $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201500/MYD021KM.A2021004.2015.061.NRT.hdf \
             $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201500/MYD03.A2021004.2015.061.NRT.hdf \
             --reader_name modis_hdf4 \
             --product_name Infrared \
             --output_formatter unprojected_image \
             --output_formatter_kwargs '{"x_size": "250"}' \
             --filename_formatter geoips_fname \
             --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/modis.<product>.unprojected_image" \
             --self_register_dataset '1KM' \
             --self_register_source modis
retval=$?

exit $retval
