#!/usr/bin/env python3
"""
Push a pandas release to GitHub.
"""
import argparse
import subprocess
import sys

from packaging import version


def check_tag(tag):
    assert tag.startswith('v'), ("Invalid tag '{}', must "
                                 "start with 'v'".format(tag))
    ver = version.parse(tag.lstrip('v'))
    assert isinstance(ver, version.Version), "Invalid tag '{}'".format(tag)
    return tag


def get_branch(tag):
    if tag[-1] == '0':
        # off master
        base = 'master'
    else:
        base = '.'.join([tag[1:].rsplit('.', 1)[0], 'x'])

    return base


def push(tag):
    branch = get_branch(tag)
    subprocess.check_call(['git', 'push', 'upstream', branch, '--follow-tags'])


def parse_args(args=None):
    parser = argparse.ArgumentParser(__name__, usage=__doc__)
    parser.add_argument('tag', type=check_tag)

    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    push(args.tag)


if __name__ == '__main__':
    sys.exit(main())
