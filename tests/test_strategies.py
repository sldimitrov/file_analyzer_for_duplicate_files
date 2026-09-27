"""
Tests for duplicate_finder.strategies and duplicate_finder.hashing.
"""

# TODO: Edge cases worth a test each:
#   - empty files
#   - same size, different content
#   - same beginning, different ending (partial hash must not be fooled)
#   - a single file (no duplicates at all)
#   - progressive and naive strategies must find the SAME groups
