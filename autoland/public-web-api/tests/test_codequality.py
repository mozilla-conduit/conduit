# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Code Style Tests.
"""
import subprocess


def test_check_python_style():
    files = (
        'setup.py',
        'tasks.py',
        'autolandweb',
        'tests',
    )
    cmd = ('./venv/bin/yapf', '--diff', '--recursive')
    passed = len(subprocess.check_output(cmd + files)) == 0
    assert passed, (
        'The python code does not adhear to the project style. Please '
        'run `invoke checkstyle` to display the required changes or '
        '`invoke formatstyle` to make the changes in place.'
    )


def test_check_python_flake8():
    files = (
        'setup.py',
        'tasks.py',
        'autolandweb',
        'tests',
    )
    cmd = ('./venv/bin/flake8', )
    passed = subprocess.call(cmd + files) == 0
    assert passed, (
        'Flake8 did not run cleanly, please run `invoke flake8` to display '
        'the reported errors.'
    )
