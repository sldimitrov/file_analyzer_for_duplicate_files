import os
import re

def search_files_by_name(directory, name_pattern):
    """
    Searches for files in a directory (and its subdirectories) whose names match a given pattern.
    :param directory: The path to the directory to search in.
    :param name_pattern: The pattern that the file names should match (can be a plain text or a regular expression).
    :return: A list of paths to all the files found.
    """
    pass

def search_files_by_extension(directory, extension):
    """
    Searches for files in a directory (and its subdirectories) with a specific extension.
    :param directory: The path to the directory to search in.
    :param extension: The extension of the files to search for (e.g., ".txt", ".png").
    :return: A list of paths to all the files found.
    """
    pass

def search_files_by_size(directory, min_size, max_size):
    """
    Searches for files in a directory (and its subdirectories) whose size is within a specific range.
    :param directory: The path to the directory to search in.
    :param min_size: The minimum size of the files (in bytes).
    :param max_size: The maximum size of the files (in bytes).
    :return: A list of paths to all the files found.
    """
    pass

def search_files_by_content(directory, content_pattern):
    """
    Searches for files in a directory (and its subdirectories) that contain a specific text or pattern.
    :param directory: The path to the directory to search in.
    :param content_pattern: The text or pattern that the files should contain (can be plain text or a regular expression).
    :return: A list of paths to all the files found.
    """
    pass

def search_files_by_metadata(directory, metadata_criteria):
    """
    Searches for files in a directory (and its subdirectories) that match specific metadata criteria.
    :param directory: The path to the directory to search in.
    :param metadata_criteria: A dictionary that specifies the metadata criteria (e.g., {"author": "John Doe", "created_after": "2022-01-01"}).
    :return: A list of paths to all the files found.
    """
    pass

def search_files(directory, criteria):
    """
    General function for searching files that combines multiple criteria.
    :param directory: The path to the directory to search in.
    :param criteria: A dictionary that specifies the various search criteria (e.g., {"name": "*.txt", "size_min": 1024, "content": "hello world"}).
    :return: A list of paths to all the files that match all the criteria.
    """
    pass