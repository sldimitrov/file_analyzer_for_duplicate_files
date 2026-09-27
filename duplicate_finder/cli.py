"""
Command-line interface - the only place (besides a future GUI) that
talks to the user.

Responsibilities:
    1. Parse arguments into ScanOptions.
    2. Run the pipeline.
    3. Print the report / write exports.
    4. Ask for confirmation before any action.
"""

# TODO: Build the argparse parser (paths, strategy, filters, --json, --csv, --dry-run...).

# TODO: main() - glue the pipeline stages together in order.
#   - If main() gets long, which part belongs in its own function
#     so the GUI can reuse it later without argparse?

