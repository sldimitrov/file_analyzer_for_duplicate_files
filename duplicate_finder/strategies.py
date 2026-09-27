"""
Stages 3 and 4 of the pipeline: Group candidates -> Verify.

Progressive filtering - each stage is more expensive but more accurate,
and only runs on what survived the previous one:

    size  ->  partial hash  ->  full hash  ->  (byte-by-byte, optional)
"""

# TODO: Group by size - drop every group with only one file.

# TODO: Refine a group by partial hash, then by full hash.
#   - Notice the shape: "take groups in, split them by a key, drop singles".
#     Can one generic helper serve every stage?

# TODO: Optional byte-by-byte comparison ("paranoid" mode).

# TODO: A function that runs the chosen stages in order and returns DuplicateGroups.

# TODO: Same-name heuristic - files that share a NAME (not a path).
#   - This does not prove duplication. How will the report make that clear?

# TODO (Phase 4): A "naive" strategy (full-hash everything) kept for the benchmark.
