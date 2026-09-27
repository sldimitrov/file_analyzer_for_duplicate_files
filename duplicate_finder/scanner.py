"""
Stage 1 of the pipeline: Scan.

Walk one or more directories and produce FileEntry objects with
CHEAP metadata only. Never open or hash files here.
"""

# TODO: A function that walks the root paths and yields FileEntry objects.
#   - Why might a generator be better than building a full list?
#   - What happens on a PermissionError or a broken symlink? (Record it, don't crash.)
#   - Hardlinks: two paths, one file on disk. How can you detect that?
#   - Which directories should be skipped by default (.git, .venv, node_modules)?
#     Is that the scanner's job or the filter's job?
