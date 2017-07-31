#! /usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib


def hash_file(file_path: str, check_method: str) -> str:
    """
        Generates and returns the hash of a file in a hash method.

        -----

        args:

        file_path: str
            The system path of the file to hash.

        check_method: str
            The chosen hash method. Raises a ValueError if it isn't supported.

        return: str
        The hash of the file given the method.
    """
    BLOCK_SIZE = 8192
    hash_object = hashlib.new(check_method)

    with open(file_path, "rb") as file_stream:
        for block in iter(lambda: file_stream.read(BLOCK_SIZE), b""):
            hash_object.update(block)

    return hash_object.hexdigest()
