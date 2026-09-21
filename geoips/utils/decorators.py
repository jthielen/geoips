# !#######################################################################
#
# THIS SOURCE CODE IS PROPERTY OF THE GOVERNMENT OF THE UNITED STATES OF
# AMERICA. BY USING, MODIFYING, OR DISSEMINATING THIS SOURCE CODE, YOU ACCEPT
# THE TERMS AND CONDITIONS IN THE NRL OPEN LICENSE AGREEMENT. USE, MODIFICATION,
# AND DISSEMINATION ARE PERMITTED ONLY IN ACCORDANCE WITH THE TERMS AND
# CONDITIONS OF THE NRL OPEN LICENSE AGREEMENT. NO OTHER RIGHTS OR LICENSES
# ARE GRANTED. UNAUTHORIZED USE, SALE, CONVEYANCE, DISPOSITION, OR MODIFICATION
# OF THIS SOURCE CODE MAY RESULT IN CIVIL PENALTIES AND/OR CRIMINAL PENALTIES
# UNDER 18 U.S.C. § 641.
#
# !########################################################################

"""GeoIPS decorators module."""

from warnings import warn
from functools import wraps
import inspect


class deprecated:
    """
    A decorator that deprecates a function.

    When applied to a function, will cause that function to raise a
    DeprecationWarning when called.
    """

    def __init__(self, replacement=None):
        self.replacement = replacement

    def __call__(self, func):
        """Call method."""
        func_mod = inspect.getmodule(func).__name__
        func_name = f"{func_mod}.{func.__name__}"
        msg = f"Function '{func_name}' is deprecated and "
        msg += "will be removed in a future version."
        if self.replacement:
            repl_mod = inspect.getmodule(self.replacement).__name__
            repl_name = f"{repl_mod}.{self.replacement.__name__}"
            msg += f' Use "{repl_name}" for the same functionality.'

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            warn(msg, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        wrapped_func.__doc__ = f"DECPRECATED: {msg}\n\n"
        wrapped_func.__doc__ += self.replacement.__doc__
        return wrapped_func


def developmental(func):
    """Mark an interfaces as developmental.

    When applied to a function, will prepend a "developmental" message to the
    beginning of that function's docstring.
    """
    func_mod = inspect.getmodule(func).__name__
    func_name = f"{func_mod}.{func.__name__}"
    msg = f"'{func_name}' is currently under development "
    msg += "and should be expected to change in the future.\n"
    msg += "Please provide feedback at "
    msg += "https://github.com/NRLMMD-GEOIPS/geoips or geoips@nrlmry.navy.mil."

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs)

    wrapped_func.__doc__ = f"DEVELOPMENTAL: {msg}\n\n"
    wrapped_func.__doc__ += func.__doc__

    return wrapped_func
