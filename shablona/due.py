# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""

Stub file for a guaranteed safe import of duecredit constructs:  if duecredit is
not available.

To use it, just place it into your project codebase to be imported, e.g. copy as

    cp stub.py /path/tomodule/module/due.py

Note that it might be better to avoid naming it duecredit.py to avoid shadowing
installed duecredit.

Then use in your code as

    from .due import due, Doi, BibTeX


Examples
--------

TODO


License:
Originally a part of the duecredit, which is distributed under BSD-2 license.
"""

__version__ = '0.0.4'

class InactiveDueCreditCollector(object):
    """Just a stub at the Collector which would not do anything"""
    def _donothing(self, *args, **kwargs):
        """Perform no good and no bad"""
        pass

    def dcite(self, *args, **kwargs):
        """If I could cite I would"""
        def nondecorating_decorator(func):
             return func
        return nondecorating_decorator

    cite = load = add =  _donothing

    def __repr__(self):
        return self.__class__.__name__ + '()'

def _donothing_func(*args, **kwargs):
    """Perform no good and no bad"""
    pass

try:
    from duecredit import *
    if 'due' in locals() and not hasattr(due, 'cite'):
        raise RuntimeError("Imported due lacks .cite. DueCredit is now disabled")
except Exception as e:
    if type(e).__name__ != 'ImportError':
        import logging
        logging.getLogger("duecredit").error(
            "Failed to import duecredit due to %s" % str(e))
    # Initiate due stub
    due = InactiveDueCreditCollector()
    BibTeX = Doi = Url = _donothing_func
