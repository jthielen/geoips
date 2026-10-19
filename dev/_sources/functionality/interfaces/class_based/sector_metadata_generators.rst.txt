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

.. _sector_metadata_generators_functionality:

Sector Metadata Generators in GeoIPS
************************************

A sector metadata generator is a class-based GeoIPS plugin that parses an external source —
such as a tropical-cyclone b-deck/f-deck file or a volcano track file — into the metadata
GeoIPS uses to build :ref:`dynamic sectors <create-a-dynamic_sector>`. Examples include the
``bdeck_parser``, ``fdeck_parser``, and ``volc_parser`` plugins.

For the built-in generators, see the `sector_metadata_generators directory
<https://github.com/NRLMMD-GEOIPS/geoips/tree/main/geoips/plugins/classes/sector_metadata_generators>`_.
