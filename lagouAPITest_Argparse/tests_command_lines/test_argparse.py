# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 10:30
# @Author  : pengketong
# test_argparse.py

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("name", help="This is a demo", action="store")

    args = parser.parse_args()

    if args.name:
        print(args.name)
