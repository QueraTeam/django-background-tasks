#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner
from argparse import ArgumentParser


def main(argv):
    parser = ArgumentParser()
    parser.add_argument(
        "--async",
        "-a",
        action="store_true",
        default=False,
        dest="run_async",
        help="process background tasks in multiple threads",
    )
    args = parser.parse_args(argv)

    os.environ["DJANGO_SETTINGS_MODULE"] = "background_task.tests.test_settings"

    if args.run_async:
        os.environ["DJANGO_SETTINGS_MODULE"] = "background_task.tests.test_settings_async"

    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["background_task.tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    main(argv=sys.argv[1:])
