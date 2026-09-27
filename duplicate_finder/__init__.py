"""
duplicate_finder - find duplicate files and help remove them safely.

Pipeline every run follows:

    Scan -> Filter -> Group candidates -> Verify -> Report -> (Act)

Guiding rule: nothing inside this package calls print() or input(),
except cli.py (and later gui). Every other module returns plain data.
"""

# TODO: Decide what the public API of the package is.
#       Which names should someone be able to import directly from
#       `duplicate_finder` without knowing the internal modules?
