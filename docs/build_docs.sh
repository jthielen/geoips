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

#!/bin/sh
if [[ "$1" == "" ]]; then
    echo "Usage: $0 repopath pkgname"
    exit 1
fi
# pkgname should nearly always be the same as reponame.  template_basic_plugin repo
# whose pkgname is my_package is the notable exception.
pkgname=$2
# Fortran libraries sphinx build fails without realpath
repopath=`realpath $1`
save_temp_dir=$GEOIPS_OUTDIRS/scratch/docs/$pkgname
curr_path=`dirname $0`
# If this is an empty directory, remove it before we start.
# build_docs.py fails with empty latest folder.
if [ -d $repopath/docs/source/releases/latest ] && [ -z "$(ls -A "$repopath/docs/source/releases/latest")" ]; then
    echo "Latest folder is empty, removing" 
    rmdir -v $repopath/docs/source/releases/latest
fi
# Write pre-built docs to repopath, but must pass in pkgname to build_docs.
python3 $GEOIPS_PACKAGES_DIR/geoips/docs/build_docs.py \
  --license-url $GEOIPS_REPO_URL \
  --geoips-docs-path $GEOIPS_PACKAGES_DIR/geoips/docs/ \
  --output-dir "$repopath/docs/build/sphinx/html" \
  --save-temp-dir "$save_temp_dir" \
  --force \
  --repo-path $repopath \
  $pkgname
retval=$?

echo "Temporary files written to:"
echo $save_temp_dir

exit $retval
