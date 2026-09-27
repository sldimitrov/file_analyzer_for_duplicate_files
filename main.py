import os
from typing import Dict, List, LiteralString
import hashlib


def walk_directory(path: str) -> list[LiteralString | str | bytes]:
    """
    Recursively walks the given directory and returns a list of all file paths.
    """
    file_paths = []

    for dirpath, _, filenames in os.walk(path,topdown=True):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_paths.append(file_path)

    return file_paths


def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def generate_file_metadata(file_paths: list[LiteralString | str | bytes]) -> Dict[LiteralString | str | bytes, Dict]:
    metadata = {}
    for path in file_paths:
        if os.path.isfile(path):  # check if path is a file
            size = os.path.getsize(path)
            sha256 = calculate_sha256(path)
            metadata[path] = {"size": size, "sha256": sha256}
    return metadata


def find_duplicates_by_name(files: list[LiteralString | str | bytes]) -> Dict[str, List[str]]:
    """
    Finds duplicate files by comparing their names.
    Returns a dictionary mapping each unique file name to a list of its duplicates.
    """
    name_to_files = {}

    # Extract only the file name without the dir
    for file in files:
        if file not in name_to_files:
            name_to_files[file] = []
        name_to_files[file].append(file)

    return name_to_files


def find_duplicates_by_size(files_metadata: Dict[str, Dict]) -> Dict[int, List[str]]:
    """
    Finds duplicate files by comparing their sizes.
    Returns a dictionary mapping each unique file size to a list of files with that size.
    """
    size_to_files = {}

    for file_path, metadata in files_metadata.items():
        size = metadata["size"]
        if size not in size_to_files:
            size_to_files[size] = []
        size_to_files[size].append(file_path)

    duplicates = {size: files for size, files in size_to_files.items() if len(files) > 1}
    return duplicates


def find_duplicates_by_hash(files_metadata: Dict[str, Dict]) -> Dict[str, List[str]]:
    """
    Finds duplicate files by comparing their hash values.
    Returns a dictionary mapping each unique hash to a list of files with that hash.
    """
    hash_to_files = {}

    for file_path, metadata in files_metadata.items():
        hash = metadata["sha256"]
        if hash not in hash_to_files:
            hash_to_files[hash] = []
        hash_to_files[hash].append(file_path)

    duplicates = {hash: files for hash, files, in hash_to_files.items() if len(files) > 1}
    return duplicates


def find_duplicates_by_content(file_paths: list[LiteralString | str | bytes]) -> Dict[str, List[str]]:
    """
    Finds duplicate files by comparing their content byte by byte.
    Returns a dictionary mapping each unique file to a list of its duplicates.
    """
    content_to_files = {}

    for file_path in file_paths:
        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                content = file.read()
                if content not in content_to_files:
                    content_to_files[content] = []
                content_to_files[content].append(file_path)

    duplicates = {content: files for content, files in content_to_files.items() if len(files) > 1}
    return duplicates


def calculate_storage_stats(duplicates: Dict[str, List[str]]) -> Dict[str, int]:
    """
    Calculates total and wasted storage space based on the found duplicates.
    Returns a dictionary with keys 'total_space', 'unique_space' and 'wasted_space'.
    """
    # Find: duplicates_total_size, unique_files_size, approximate_size_saved
    total_space = 0
    unique_space = 0

    for key, duplicates in duplicates.items():
        for duplicate in duplicates:
            total_space += os.path.getsize(duplicate)

        unique_space += os.path.getsize(duplicates[0])

    wasted_space = total_space - unique_space

    return {'total_space': total_space, 'unique_space': unique_space, 'wasted_space': wasted_space}


def print_results(results: Dict[str, int]) -> None:
    print("Disk usage statistics:")
    print(f"Total space: {results['total_space']} bytes")
    print(f"Unique files space: {results['unique_space']} bytes")
    print(f"Wasted space: {results['wasted_space']} bytes")
    print(f"Potential space savings: {results['wasted_space']} bytes")


def main():
    # directory = input("Enter directory path to analyze: ")
    directory = "test_data"
    algorithm = input("Choose algorithm (name/size/hash/content): ")

    print(f"Analyzing {directory} using {algorithm} algorithm...")

    file_paths = walk_directory(directory)
    files_metadata = generate_file_metadata(file_paths)

    duplicates = {}
    if algorithm == 'name':
        duplicates = find_duplicates_by_name(file_paths)
    elif algorithm == 'size':
        duplicates = find_duplicates_by_size(files_metadata)
    elif algorithm == 'hash':
        duplicates = find_duplicates_by_hash(files_metadata)
    else:
        duplicates = find_duplicates_by_content(file_paths)

    # Calculate stats
    results = calculate_storage_stats(duplicates)

    # Print results
    print_results(results)


if __name__ == '__main__':
    main()

# TODO: IDEAS - interface (text/GUI), automatic deletion of duplicates
# TODO: IDEAS - allowing more algorithms for comparing
# TODO: IDEAS - more detailed statistics and visualisation of results
# TODO: IDEAS - higher performance by parallel threads or using database

