"""
Stage 5 of the pipeline: Report.

Turn a ScanResult into human-readable text and statistics.
Return strings/structures - let cli.py do the printing.
"""

# TODO: Human-readable sizes (bytes -> KB / MB / GB).

# TODO: Summary statistics: files scanned, groups found, wasted space,
#       elapsed time, number of skipped/errored files.

# TODO: Detailed listing of groups, biggest wasted space first.
#   - How much detail is useful before it becomes noise? (top N? flag?)
