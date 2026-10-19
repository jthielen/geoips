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

Interfaces
==========

GeoIPS plugins come in two forms: **class-based** plugins written in Python (readers,
algorithms, interpolators, colormappers, output formatters, and more) and **YAML-based**
plugins defined declaratively (products, sectors, annotators). The pages below describe
each interface. To learn how to author a class-based plugin, see
:ref:`writing-class-based-plugins`.

.. toctree::
    :maxdepth: 1
    :caption: Writing plugins

    writing-class-based-plugins

.. toctree::
    :maxdepth: 1
    :caption: Class-based (Python) interfaces

    class_based/readers
    class_based/algorithm
    class_based/interpolators
    class_based/colormapper
    class_based/coverage_checkers
    class_based/output_formats
    class_based/filename_formats
    class_based/title_formats
    class_based/output_checkers
    class_based/sector_adjusters
    class_based/sector_metadata_generators
    class_based/sector_spec_generators
    class_based/databases
    class_based/procflows
    class_based/validators

.. toctree::
    :maxdepth: 1
    :caption: YAML-based interfaces

    yaml_based/products
    yaml_based/product_defaults
    yaml_based/static_sectors
    yaml_based/dynamic_sectors
    yaml_based/feature_annotators
    yaml_based/gridline_annotators
