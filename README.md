# File analyzer for duplicate files

## Problem

- There are 

## Requirements

- Analyze any given directory and return how much storage can be saved by removing duplicated.
- Return detailed, human-readable data as an output in the console.
- Differ between different algorithms and compare their speed/acurracy.
- Include block schemes for the data model and the overall architecture.
- Include 

### BONUS:
- Search for a given word in the file directory can also be implemented later.
- Add a GUI for the project using tkinter/ any other UI lib of your choice.

## Roadmap

**Goal:** a disk-cleanup tool that finds duplicate files and helps remove them safely.
Search is a *filter* inside that tool, not a separate product.

**Pipeline every run follows:**

```
Scan → Filter → Group candidates → Verify → Report → (Act)
```

**Guiding rule:** the core never calls `print()` or `input()`, only the CLI/GUI layer talks to the user.

### Phase 1: Data model & package split (refactor only, same behaviour)

- [ ] Define dataclasses: `FileEntry`, `DuplicateGroup`, `ScanResult`, `ScanOptions`
- [ ] Split `main.py` into a `duplicate_finder/` package, one module per pipeline stage:
  `models`, `scanner`, `filters`, `strategies`, `hashing`, `report`, `export`, `actions`, `cli`, `gui`
- [ ] Move `search.py` into `filters`
- [ ] Draw the data model and architecture block schemes (fill in the sections below)

> Think about: which fields of `FileEntry` are cheap to get, and which should only be computed when needed?

### Phase 2: Progressive duplicate detection + known bugs

- [ ] Stage 1: group by size and drop files with a unique size
- [ ] Stage 2: partial hash (first/last few KB) within each size group
- [ ] Stage 3: full hash of the remaining candidates
- [ ] Stage 4 (optional "paranoid" mode): byte-by-byte comparison
- [ ] Treat "same name" as a *heuristic* report (possible duplicates), not a real duplicate check
- [ ] Fix: `find_duplicates_by_name` groups by full path, so nothing ever matches
- [ ] Fix: `find_duplicates_by_content` reads whole files into memory
- [ ] Fix: `generate_file_metadata` hashes every file, even for the size/name strategies
- [ ] Fix: `calculate_storage_stats` counts groups that contain only one file

> Think about: why is each stage cheaper than the next, and what fraction of files survives each one?

### Phase 3: CLI & reporting

- [ ] `argparse` CLI: path(s), strategy, filters (extension, size range, name pattern, ignored folders)
- [ ] Human-readable sizes (KB/MB/GB); biggest duplicate groups listed first
- [ ] Summary: files scanned, groups found, wasted space, elapsed time, skipped/errored files
- [ ] `--json` / `--csv` export
- [ ] Graceful handling of permission errors, locked files, broken symlinks, hardlinks

### Phase 4: Tests & experiment

- [ ] Unit tests per strategy using generated temporary folders
- [ ] Edge cases: empty files, same size but different content, same prefix but different ending, unreadable files, symlinks
- [ ] Benchmark script with synthetic datasets (vary file count, file size, duplicate ratio)
- [ ] Compare **naive full hashing** vs **progressive filtering**: time, bytes read, hashes computed
- [ ] Plot number of files (x) vs time (y) for each approach and write up the conclusions

### Phase 5: Safe actions

- [ ] Dry-run by default
- [ ] Move to a quarantine folder or the Recycle Bin instead of deleting permanently
- [ ] Keep policies: oldest / newest / shortest path / preferred folder
- [ ] Confirmation before any file is touched
- [ ] (Advanced) replace duplicates with hardlinks

### Phase 6: Bonus

- [ ] Hash cache (SQLite/JSON) keyed by path + size + modified time
- [ ] Parallel hashing with `concurrent.futures`; benchmark threads vs a single thread
- [ ] Progress indicator for large directories
- [ ] tkinter GUI as a thin layer over the same core

## Data model

## Algorithm

- A set of different algorithms

## Architecture

- Describe different stages of the program execution.

## Implementation

- We will compare different algorithms.

## Libraries

pathlib
hashlib
os
time
dataclasses
collections
argparse
json
csv
statistics
concurrent.futures

## Python engineering

### What can be practised?

modules
packages
classes
dataclasses
type hints
generators
context managers
exceptions
unit testing
mocking
CLI applications
configuration
logging
profiling
benchmarking

## Algorithms/data structures

### You can use:

dictionaries
sets
grouping
hashing
filtering
graph-like relationships between duplicate files
complexity analysis

## Tests

- Add unit tests.
- Compare different implementations/algorithms speed their affect on the execution time.

## Experiment

- Log out data from different algorithms to compare the results
- Create graphs using the numbers of file (x-axis) and time (y-axis).

## UI