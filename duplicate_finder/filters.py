"""
Stage 2 of the pipeline: Filter.

Decide which scanned files are even considered. This is where the
ideas from the old search.py live (name, extension, size range...).
"""

# TODO: One small predicate per criterion (extension, size range, name pattern, ...).
#   - What should each predicate take in, and what should it return?

# TODO: A function that combines the predicates from ScanOptions and
#       applies them to a stream of FileEntry objects.
#   - Can you apply the filters without loading all entries into memory?

# NOTE: Content search ("files containing the word X") is expensive.
#       Does it belong in the same place as the cheap metadata filters?
