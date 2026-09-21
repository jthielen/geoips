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

.. _architecture:

Architecture
============

The architecture section describes the design and structure of GeoIPS
in-depth. This section is intended for users who want to understand how GeoIPS
works, plugin developers who need a deeper understanding of how plugins
operate, and developers of the core GeoIPS package. The architecture section
details the plugin system, the various plugin kinds and how they behave,
interfaces and how they manage plugins, the plugin registry, unit and
integration test structure, documentation standards, code standards, and more.

.. toctree::
    :maxdepth: 1

    extend-with-plugins
    plugin-registry
    interfaces/module_based/output-checkers/index.rst
    structure-of-geoips/index
    data-structures
    geoips-specification
    cached-files
    test-infrastructure/index
    ci-infrastructure
    documentation/index
    command_line_interface
    custom-types/index
