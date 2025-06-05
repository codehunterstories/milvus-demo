import unittest
import os


def load_tests(loader, tests, pattern):
    start_dir = os.path.dirname(__file__)
    return loader.discover(start_dir)
