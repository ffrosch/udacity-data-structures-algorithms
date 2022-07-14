#!/usr/bin/env python3.10

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
        valid forms are e.g. '.doc' and 'doc'
      path(str): path of the file system

    Returns:
       a list of paths
    """
    matched_files = []

    match suffix:
        case "":
            return "ValueError: suffix can't be an empty string!"
        case None:
            return "ValueError: suffix can't be None!"
        case ".":
            return "ValueError: '.' is not a valid suffix!"
        case str(p) if p.find(".") > 0:
            return f"ValueError: '{suffix}' is not a valid suffix!"

    match path:
        case "":
            return "ValueError: path can't be an empty string!"
        case None:
            return "ValueError: path can't be  None!"
        case str(p) if not os.path.isdir(p):
            return "ValueError: path must be a directory!"

    # remove '.' at the beginning
    suffix = suffix[1:] if suffix[0] == "." else suffix

    for child in os.listdir(path):
        child_path = os.path.join(path, child)

        if os.path.isfile(child_path):

            if child_path.split(".")[-1] == suffix:
                matched_files.append(child_path)

        if os.path.isdir(child_path):
            matched_files.extend(find_files(suffix, child_path))

    return matched_files


if __name__ == "__main__":
    print(find_files(".c", "./"))
    # ['./testdir/subdir1/a.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c']
    print(find_files(".", "./"))
    # ValueError: '.' is not a valid suffix!
    print(find_files(".c", "./dir-does-not-exist"))
    # ValueError: path must be a directory!
    print(find_files(".gitkeep", "./"))
    # ['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep']
    print(find_files("keep", "./"))
    # []
    print(find_files("a.c", "./"))
    # ValueError: 'a.c' is not a valid suffix!
