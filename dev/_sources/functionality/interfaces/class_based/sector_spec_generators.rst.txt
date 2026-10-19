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

.. _sector_spec_generators_functionality:

Sector Spec Generators in GeoIPS
********************************

A sector spec generator is a class-based GeoIPS plugin that turns sector metadata into a
concrete sector specification (an :class:`~pyresample.geometry.AreaDefinition`) — for
example, building an area definition from a center latitude/longitude, resolution, and
size. These are used when generating :ref:`dynamic sectors <create-a-dynamic_sector>`.

For the built-in generators, see the `sector_spec_generators directory
<https://github.com/NRLMMD-GEOIPS/geoips/tree/main/geoips/plugins/classes/sector_spec_generators>`_.
