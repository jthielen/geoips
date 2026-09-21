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

.. _databases_functionality:

Databases in GeoIPS
*******************

A database is a class-based GeoIPS plugin that reads from or writes to a product database —
for example, recording the outputs a processing run produced, or querying previously
generated products (such as when compositing). Database plugins let GeoIPS integrate with
external product-tracking systems without hard-coding a particular backend.

For the built-in database plugins, see the `databases directory
<https://github.com/NRLMMD-GEOIPS/geoips/tree/main/geoips/plugins/classes/databases>`_.
