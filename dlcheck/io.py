#! /usr/bin/python3
# -*- coding: utf-8 -*-

from typing import Callable, Dict

import urllib.request


def download_file(url: str, 
                  file_path: str, 
                  observer: Callable[[str, str], None]=None
                  ) -> Dict[str, str]:
    """
        Downloads the content of an url to a system path,
        and notifies an observer on each iteration.

        -----

        args:

        url: str
            The resource to be downloaded.

        file_path: str
            The system path to write the resource on.

        observer: Callable[[str, str], None]
            An observer function, which is given the current downloaded bytes,
            and the size of the downloaded resource.


        returns: Dict[str, str]
        A dictionary containing the headers of the resource
    """
    with urllib.request.urlopen(url) as response:
        response_info = response.info()
        file_size = int(response_info.get("Content-Length"))

        with open(file_path, 'wb') as file_stream:
            BLOCK_SIZE = 8192
            downloaded = 0

            while True:
                buffer = response.read(BLOCK_SIZE)
                if not buffer:
                    break

                downloaded += len(buffer)
                file_stream.write(buffer)

                if observer is not None:
                    observer(downloaded, file_size)
        
        return {key: value for (key, value) in response_info.items()}

