#!/bin/bash

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

# This script ensures we exit non-zero if any of the steps fail.
check="$GEOIPS_PACKAGES_DIR/geoips/setup/check_system_requirements.sh"

test_exit=""
install_script=""
skip_create_registries="false"
if [[ "$1" == "exit_on_missing" ]]; then
    test_exit="exit_on_missing"
    install_script="$0"
fi
if [[ "$2" == "skip_create_registries" ]]; then
    skip_create_registries="true"
fi

. $check geoips_base

# If you already have a .gitconfig, this won't do anything.
# Gives some reasonable defaults if you don't have one.
. $check set_gitconfig

. $check run_command "geoips config install test_data_amsr2"

if [[ "$skip_create_registries" == "true" ]]; then
    echo "Skipping geoips config create-registries"
else
    . $check run_command "geoips config create-registries"
fi
