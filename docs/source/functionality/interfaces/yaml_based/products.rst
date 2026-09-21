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

.. _products_functionality:

Products in GeoIPS
******************

A product is a YAML-based GeoIPS plugin that defines the information needed to
produce a particular output from a particular data source. This information
includes the source of the data that will be processed, which plugins are
needed to produce the output, what order they go in (via the `family`
attribute), and values to be passed to the arguments for those plugins.

Products are a key plugin for GeoIPS, as they define much of the information
GeoIPS needs to determine how to produce an output.

.. note::

   In :ref:`Order-Based Processing <order-based-processing>`, a product is referenced from
   a workflow as a ``kind: product`` step (``name: [source_name, product_name]``). GeoIPS
   expands that step into the ordered plugin steps its ``family`` implies (for example,
   interpolator → algorithm → colormapper). See :ref:`workflows`.

See the
:ref:`products tutorial <create-a-product>`
for instruction on setting up a new product.

Products are defined in a YAML file, as shown in the tutorial above. They are
then included as arguments at the command line:

   .. code-block:: bash

        --product_name My-Cloud-Top-Height
