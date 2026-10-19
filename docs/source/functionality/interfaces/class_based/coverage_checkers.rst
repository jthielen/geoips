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

.. _coverage_checkers_functionality:

Coverage Checkers in GeoIPS
***************************

A coverage checker is a class-based GeoIPS plugin that computes how much of a sector's
domain is covered by valid data, returning a coverage percentage. Coverage checkers let
GeoIPS decide whether an output should be produced (for example, by comparing against a
minimum-coverage threshold) and annotate products with their coverage.

Different coverage checkers suit different data. For example, ``masked_arrays`` computes
coverage from a masked array, ``center_radius`` restricts the calculation to a radius
around a center point (useful for tropical cyclones), and ``windbarbs`` handles wind-barb
products.

For the built-in coverage checkers, see the `coverage_checkers directory
<https://github.com/NRLMMD-GEOIPS/geoips/tree/main/geoips/plugins/classes/coverage_checkers>`_.

In an :ref:`Order-Based Processing workflow <order-based-processing>`, a coverage checker
is a ``coverage_checker`` step that typically depends on the algorithm output and the
sector.

Plugin arguments
================

The arguments accepted by a coverage checker step (validated in
:ref:`Order-Based Processing workflows <order-based-processing>`) are defined by the model
below. These fields are generated directly from the code, so they always reflect the
current validation rules.

.. autopydantic_model:: geoips.pydantic_models.v1.coverage_checkers.CoverageCheckerArgumentsModel
   :noindex:
