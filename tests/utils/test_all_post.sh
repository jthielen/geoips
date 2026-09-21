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

echo ""
echo `date` " Running post, final results in $LOGFILE"


echo "" >> $LOGFILE 2>&1
echo "******Overall results from all test runs******" >> $LOGFILE 2>&1
echo "" >> $LOGFILE 2>&1

for curr_num in "${!overall_procflow_retvals[@]}"; do >> $LOGFILE 2>&1
    curr_return=${overall_procflow_retvals[$curr_num]} >> $LOGFILE 2>&1
    if [[ $curr_return > 1 ]]; then
        curr_return=1
    fi
    overall_procflow_retval=$((overall_procflow_retval+curr_return)) >> $LOGFILE 2>&1
    echo "" >> $LOGFILE 2>&1
    echo "${overall_calls[$curr_num]}" >> $LOGFILE 2>&1
    echo "Runtime: ${overall_runtimes[$curr_num]}" >> $LOGFILE 2>&1
    echo "return: $curr_return" >> $LOGFILE 2>&1
done >> $LOGFILE 2>&1

echo "" >> $LOGFILE 2>&1

overall_end=`date +%s` >> $LOGFILE 2>&1
overall_runtime=$((overall_end-overall_start)) >> $LOGFILE 2>&1

echo "" >> $LOGFILE 2>&1
echo "Package: $package_name" >> $LOGFILE 2>&1
echo "Total run time: $overall_runtime seconds" >> $LOGFILE 2>&1
echo "Number data types run: ${#overall_procflow_retvals[@]}" >> $LOGFILE 2>&1
echo "Number data types failed: $overall_procflow_retval" >> $LOGFILE 2>&1

echo ""
echo "Package: $package_name"
echo "Total run time: $overall_runtime seconds"
echo "Number data types run: ${#overall_procflow_retvals[@]}"
echo "Number data types failed: $overall_procflow_retval"
date -u

exit $overall_procflow_retval
