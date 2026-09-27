"""
Data model - the shared vocabulary of the whole program.

Every other module takes these objects in and/or returns them.
No I/O happens here: no reading files, no printing.
"""

# TODO: FileEntry (dataclass)
#   One file found during the scan.
#   - Which fields are cheap to get while walking a directory?
#   - Which fields are expensive and should stay empty until a strategy needs them?
#   - How will you represent "not computed yet"?

# TODO: DuplicateGroup (dataclass)
#   A set of files confirmed to have identical content.
#   - How many files must a group contain to be meaningful?
#   - Wasted space: should it be a stored field or computed from the files?
#   - Where does the idea of "the original" (the file to keep) live?

# TODO: ScanOptions (dataclass)
#   Everything the user chose for this run: root paths, filters, strategy,
#   flags (follow symlinks? include hidden files?).
#   - Which options need sensible defaults?

# TODO: ScanResult (dataclass)
#   The final output of a run, consumed by report.py, export.py and actions.py.
#   - Totals: files scanned, bytes scanned, elapsed time.
#   - Errors: files that couldn't be read. Why keep them instead of ignoring them?
