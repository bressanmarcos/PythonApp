import pytest
import os

os.sys.path.insert(0, os.getcwd())
import test.secret as secret  # pylint: disable=no-name-in-module,import-error
