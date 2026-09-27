"""
Hashing helpers used by the strategies.

The only module that reads file contents for hashing.
"""

# TODO: Partial hash - hash only a small piece of the file (e.g. start + end).
#   - Why read the end as well as the start?
#   - What about files smaller than the piece size?

# TODO: Full hash - hash the whole file in chunks.
#   - Why chunks instead of file.read()?
#   - Which hash algorithm, and why? (speed vs collision resistance)

# TODO (Phase 6): Hash cache keyed by path + size + modified time.
#   - Why do all three need to be in the key?
