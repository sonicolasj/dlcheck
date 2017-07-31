#! /usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Callable
from os.path import join as join_path

from dlcheck.io import download_file
from dlcheck.check import hash_file


def dlcheck(url: str, 
            output_directory_path: str='.',
            check_method: str=None,
            hash_digest: str=None,
            observer: Callable[[str, str], None]=None
            ) -> bool:
    """
        Downloads a resource, and checks it against a checksum, in a specific
        hash method.
        Returns True, or raises a ValueError if the file doesn't match the sum.

        -----

        args:

        url: str
            The url of the resource to download.

        output_directory_path: str
            The folder to put the downloaded file in.

        check_method: str
            The hash method to use for the check.
            Raises a ValueError if the method is not supported on the system.

        hash_digest: str
            The checksum to check the file against.

        observer: Callable[[str, str], None]
            An observer function for the download of the file, 

        returns: bool
        Returns True
    """

    file_name = url.split('/')[-1]
    file_path = join_path(output_directory_path, file_name)
    download_file(url, file_path, observer)

    if check_method is not None and \
       hash_digest is not None and \
       hash_file(file_path, check_method) != hash_digest:
        raise ValueError(
            "File {file} doesn't match the hash {hash}({method})".format(
                file=file_path,
                hash=hash_digest,
                method=check_method
            )
        )

    return True
