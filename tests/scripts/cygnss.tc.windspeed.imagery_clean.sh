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

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_cygnss/data/cyg.ddmi.s20240125-000001-e20240125-235959.l2.wind_trackgridsize25km_NOAAv1.2_L1a21.d21.nc \
    --reader_name cygnss_netcdf \
    --product_name windspeed \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --window_start_time "20240125T0600Z" \
    --window_end_time "20240125T0615Z" \
    --minimum_coverage 0 \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh062024.dat \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/cygnss.tc.windspeed.imagery_clean" \

ss_retval=$?

exit $((ss_retval))