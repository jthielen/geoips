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

# simple bash script to track a pid while process is running

pid=$1

echo "Tracking usage statistics for pid ${pid}"

csv_header="Time [UTC], CPU Count, CPU Percent, Thread Count, USS [RAM bytes], RSS [bytes]"

# check that the output directory exists
outdir="${GEOIPS_OUTDIRS}/memory_logs/"

if [[ ! -d $outdir ]]; then
    echo "Making $GEOIPS_OUTDIRS/memory_logs"
    mkdir $outdir
fi

outname="geoips_memtrack_p${pid}.csv"
outpath="${outdir}/${outname}"


echo $csv_header >> ${outpath}

while ps -p $pid > /dev/null; do

    dtime=$(date +%Y%m%d_%H%M%S_%N)
    memstats=$(python $GEOIPS_PACKAGES_DIR/geoips/geoips/utils/memusg.py ${pid})

    echo "${dtime},${memstats}" >> ${outpath}

    # could be adjusted
    sleep 0.1

done

echo "Finished tracking, see csv file in ${outpath} for results"