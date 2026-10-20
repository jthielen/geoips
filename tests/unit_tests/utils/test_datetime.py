# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""pytest test-suite for `geoips.utils.datetime.py`."""

from datetime import datetime, timedelta

import pytest

from geoips.utils.datetime import utcnow_naive


def test_utcnow_naive_type():
    """Ensure returns a timezone-naive datetime."""
    now = utcnow_naive()
    # Check exact type, not permitting subclass
    assert type(now) is datetime
    # As documented, these characteristics are what define a naive datetime
    assert now.tzinfo is None or getattr(now.tzinfo, "utcoffset", None) is None


def test_utcnow_old_stdlib_version_equivalence():
    """Ensure our utcnow matches the deprecated standard library version."""
    now = utcnow_naive()
    with pytest.warns(DeprecationWarning, match=r"utcnow\(\) is deprecated"):
        # Cannot assume instantaneous for comparison, so permit a generous buffer that
        # nevertheless ensures no timezone differences will slip through
        assert datetime.utcnow() - now < timedelta(seconds=10)
