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

"""Command line script for updating the TC database."""


def main():
    """Update TC tracks database via command line."""
    import sys
    from geoips.commandline.log_setup import setup_logging

    LOG = setup_logging()
    from geoips.sector_utils.tc_tracks_database import check_db

    if len(sys.argv) >= 2:
        LOG.info("Calling with arg %s", sys.argv[1:])
        check_db(sys.argv[1:])
    else:
        check_db()


if __name__ == "__main__":
    main()
