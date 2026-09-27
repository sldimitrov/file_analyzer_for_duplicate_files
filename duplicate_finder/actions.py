"""
Stage 6 of the pipeline (optional): Act.

The only module allowed to change the file system.
Default is ALWAYS a dry run: describe what would happen, change nothing.
"""

# TODO: Keep policies - pick which file in a DuplicateGroup to keep
#       (oldest / newest / shortest path / inside a preferred folder).

# TODO: Plan actions - produce a list of "what would happen" without doing it.
#   - Why separate planning from executing?

# TODO: Execute a plan - move to quarantine / Recycle Bin, (advanced) hardlink.
#   - What should happen if a file changed or disappeared since the scan?
#   - Why avoid permanent deletion as the default?
