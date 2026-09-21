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

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131200/VNP02DNB.A2022042.1312.001.2022042183606.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131200/VNP02IMG.A2022042.1312.001.2022042183606.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131200/VNP02MOD.A2022042.1312.001.2022042183606.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131200/VNP03DNB.A2022042.1312.001.2022042182240.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131200/VNP03IMG.A2022042.1312.001.2022042182240.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131200/VNP03MOD.A2022042.1312.001.2022042182240.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131800/VNP02DNB.A2022042.1318.001.2022042183444.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131800/VNP02IMG.A2022042.1318.001.2022042183444.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131800/VNP02MOD.A2022042.1318.001.2022042183444.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131800/VNP03DNB.A2022042.1318.001.2022042182210.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131800/VNP03IMG.A2022042.1318.001.2022042182210.nc \
             $GEOIPS_TESTDATA_DIR/test_data_viirs/data/npp/20220211/131800/VNP03MOD.A2022042.1318.001.2022042182210.nc \
             --reader_name viirs_netcdf \
             --product_name Night-Vis-IR-GeoIPS1 \
             --output_formatter unprojected_image \
             --output_formatter_kwargs '{"x_size": "500"}' \
             --filename_formatter geoips_fname \
             --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/viirsclearnight.<product>.unprojected_image" \
             --self_register_dataset 'DNB' \
             --self_register_source viirs

ss_retval=$?

exit $((ss_retval))
