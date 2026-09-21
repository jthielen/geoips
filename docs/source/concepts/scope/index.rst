:orphan:

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

Scope of GeoIPS
===============

The GeoIPS "core" package covers data processing from **reading and reformatting** source
data into the common internal GeoIPS representation, through **algorithm and product
application**, to **writing** user-configurable output formats (imagery, NetCDF, GeoTIFF,
text, and more). This processing is orchestrated by :ref:`Order-Based Processing
<order-based-processing>`.

The following are intentionally **outside** the scope of the GeoIPS core and are treated as
site-specific implementations:

* Data collection and ingest scheduling.
* Data transfer between systems.
* Product dissemination and archival.
* Operational job scheduling (though GeoIPS can integrate with tools such as ``cylc``).

See :ref:`what is GeoIPS <getting-started>` for the high-level overview and
:ref:`order-based-processing` for the processing model.
