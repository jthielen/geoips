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

.. _output_checkers_functionality:

Output Checkers in GeoIPS
*************************

An output checker is a class-based GeoIPS plugin that compares a generated output file
against a reference file (a "compare path") to validate correctness. Output checkers are
used heavily in testing to confirm that a change did not alter a product unexpectedly.

GeoIPS selects the appropriate output checker based on the output file type — for example,
``image`` for imagery (with a configurable difference ``threshold``), ``netcdf`` for
NetCDF data, ``text`` for text products, and ``geotiff`` for GeoTIFFs. The checker can be
derived automatically from the ``compare_path`` or specified explicitly.

For the built-in output checkers, see the `output_checkers directory
<https://github.com/NRLMMD-GEOIPS/geoips/tree/main/geoips/plugins/classes/output_checkers>`_.

In :ref:`Order-Based Processing <order-based-processing>`, output checkers run either as an
explicit ``output_checker`` step or via the ``outputs`` block of a workflow's ``test``
section, which sets the ``compare_path`` and inserts the checker automatically. See
:ref:`running-obp` for how to configure output checks and overrides.

Plugin arguments
================

The arguments accepted by an output checker step are defined by the model below. These
fields are generated directly from the code, so they always reflect the current validation
rules.

.. autopydantic_model:: geoips.pydantic_models.v1.output_checkers.OutputCheckerArgumentsModel
   :noindex:
