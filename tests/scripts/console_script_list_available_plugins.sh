#!/bin/sh

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

# If package_name and repo_path are passed in, pass to list_available_plugins
if [[ "$1" != "" && "$2" != "" ]]; then
    list_available_plugins readers --package_name $1 --repo_path $2
    retval_readers=$?
    list_available_plugins --package_name $1 --repo_path $2
    retval_all=$?
# Otherwise, run all
else
    list_available_plugins readers
    retval_readers=$?

    list_available_plugins
    retval_all=$?
fi
echo "Readers retval: $retval_readers"
echo "All retval: $retval_all"
exit $((retval_readers+retval_all))
