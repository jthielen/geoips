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

.. _data_units:

Common GeoIPS Data Units
************************

GeoIPS readers intake several common data processing levels, but
sources and units can vary. Within geoips, unit conversions, scale factors,
and data manipulation can occur, however several common units are expected per
data level. If ingesting similar products with different processing for the same
sensor (i.e. VIIRS L1 products from NASA versus CSPP), verify products and units rigorously.

When referring to data processing levels,
GeoIPS is referencing `EOSDIS Processing Levels <https://ghrc.nsstc.nasa.gov/home/proc_level>`_

Level 1 Data
------------

Technically, the lowest level of data that GeoIPS can read, ingest, and mainpulate, is
geolocated, calibrated data (Level 1). Standard units are the following:

- Brightness Temperature: Kelvin or Celcius
- Reflectance: Unitless, common range of 1-100
- Radiance: SI units (W/cm^2 per steradian)

Conversion can be made in brightness temperature, and scale factor, gamma corrections
can be used within product definitions for individual sensors.

Level 2 Data
------------

Level 2 data can range in variable type and format, but common
products include resampled level 1 data, and wind products.
Common variables and respective units include:

- Windspeed: Knots or Meters per second (conversions available)
- Wind Direction: Meterological convention

Level 3/4 Data
--------------

Level 3 and 4 products generally fall under GeoIPS data_fusion products, or
require additional processing, readers, or products to describe unique
variables. Users should refer to current products as guidance or create
seperate products for the data.
