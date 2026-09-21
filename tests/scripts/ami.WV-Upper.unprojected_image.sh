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

# Default values - if you do not have this exact test case available, call with available data files / sectors.

# This exact test case required for valid comparisons - remove "compare_path" argument if running a different
# set of arguments.
geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_ami/data/20231208_0300_daytime/*.nc \
    --reader_name ami_netcdf \
    --reader_kwargs '{"self_register": "LOW"}' \
    --product_name WV-Upper \
    --compare_path "$GEOIPS_PACKAGES_DIR/geoips/tests/outputs/ami.WV-Upper.unprojected_image" \
    --output_formatter unprojected_image \
    --output_formatter_kwargs '{"x_size": "1000", "y_size": "1000"}' \
    --filename_formatter geoips_fname \
    --logging_level info \
    --self_register_dataset 'Full-Disk' \
    --self_register_source ami
retval=$?

exit $retval
