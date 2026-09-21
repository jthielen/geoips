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
    ${GEOIPS_TESTDATA_DIR}/test_data_ahi/data/tonga_20220115T0430/* \
    --reader_name ahi_hsd \
    --product_name Infrared \
    --filename_formatter geoips_fname \
    --output_formatter imagery_clean \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/ahi.tonga.volcano" \
    --trackfile_parser volc_parser \
    --trackfiles $GEOIPS/tests/sectors/volc_csv/tonga_trackfile.csv \
    --tc_spec_template volc_tonga

retval=$?

exit $retval

