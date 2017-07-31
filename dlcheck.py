#! /usr/bin/python3
# -*- coding: utf-8 -*-

from dlcheck.core import dlcheck


def verbose_observer(downloaded, file_size):
    percentage = (downloaded / file_size) * 100
    print("\r{}/{}({:.2f}%)".format(downloaded, file_size, percentage), end="")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('url')
    parser.add_argument('-o', '--outdir',
                        dest='output_directory_path', default=".")
    parser.add_argument('-c', '--checkmethod', 
                        dest='check_method', default=None)
    parser.add_argument('-d', '--hash',
                        dest='hash_digest', default=None)
    parser.add_argument('-v', '--verbose',
                        dest='verbose', action='store_const',
                        const=True, default=False)

    args = parser.parse_args()

    observer = None
    if args.verbose:
        observer = verbose_observer

    print(
        dlcheck(
            args.url,
            args.output_directory_path,
            args.check_method,
            args.hash_digest,
            observer))
