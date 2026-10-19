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

.. _validators_functionality:

********************
Validators in GeoIPS
********************

A validator is a class-based GeoIPS plugin designed to produce 'validation' metrics
between a produced dataset and a dataset from a known source of truth for a given use
case. These metrics could be as simple as an absolute difference product between the
output and truth dataset, or it could be more complex such as producing statistics
derived between those two datasets (say, comparing them to produce a data for a
histogram), would would be used by an `output formatter <create-output-formatter>`_.

Every validator plugin at its core should expect these two variables:

1. xarray_obj (produced dataset)
2. truth_xarray_obj (source of truth dataset)

Additional arguments can be specified based on the family the validator falls under. The
actual validation performed by the plugin is up to the developer creating that plugin.

Validators can be executed in two ways:

Section 1 below has yet to be implemented. 2 works as specified.

1. **Specification at the Command Line:** Validators are specified
as arguments at the command line. For example:

   .. code-block:: bash

      --validator <validator name>

2. **Direct Invocation:** Call the validator from within a program:

   .. code-block:: python

      from xarray import Dataset

      from geoips.interfaces import validators

      validator_name = "difference"
      validator = validators.get_plugin(validator_name)

      # Replace 'Dataset()' with the actual produced and truth datasets
      ds = validator(xarray_obj=Dataset(), truth_xarray_obj=Dataset())
