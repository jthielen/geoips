..
    !#######################################################################
    THIS SOURCE CODE IS PROPERTY OF THE GOVERNMENT OF THE UNITED STATES OF
    AMERICA. BY USING, MODIFYING, OR DISSEMINATING THIS SOURCE CODE, YOU ACCEPT
    THE TERMS AND CONDITIONS IN THE NRL OPEN LICENSE AGREEMENT. USE, MODIFICATION,
    AND DISSEMINATION ARE PERMITTED ONLY IN ACCORDANCE WITH THE TERMS AND
    CONDITIONS OF THE NRL OPEN LICENSE AGREEMENT. NO OTHER RIGHTS OR LICENSES
    ARE GRANTED. UNAUTHORIZED USE, SALE, CONVEYANCE, DISPOSITION, OR MODIFICATION
    OF THIS SOURCE CODE MAY RESULT IN CIVIL PENALTIES AND/OR CRIMINAL PENALTIES
    UNDER 18 U.S.C. § 641.
    !########################################################################

.. _sector_adjusters_functionality:

Sector Adjusters in GeoIPS
**************************

A sector adjuster is a class-based GeoIPS plugin that modifies a sector's
:class:`~pyresample.geometry.AreaDefinition` at runtime based on the data being processed.
The most common use is recentering a tropical cyclone sector on the storm's actual center
(for example, from an archer or best-track fix) before the data is registered to it.

For the built-in sector adjusters, see the `sector_adjusters directory
<https://github.com/NRLMMD-GEOIPS/geoips/tree/main/geoips/plugins/classes/sector_adjusters>`_.
