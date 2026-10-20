# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""GeoIPS datetime helpers."""

from datetime import datetime, timezone


def utcnow_naive() -> datetime:
    """Return a timezone-naive version of the current UTC time.

    Notes
    -----
    Intended as a replacement for the prior `datetime.utcnow()`, where timezone-naive
    datetimes are still assumed and/or required.
    """
    return datetime.now(timezone.utc).replace(tzinfo=None)
