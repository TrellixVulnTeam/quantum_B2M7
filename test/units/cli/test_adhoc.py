# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
import re

from quantum import context
from quantum.cli.adhoc import AdHocCLI, display
from quantum.errors import QuantumOptionsError


def test_parse():
    """ Test adhoc parse"""
    with pytest.raises(ValueError, match='A non-empty list for args is required'):
        adhoc_cli = AdHocCLI([])

    adhoc_cli = AdHocCLI(['quantumtest'])
    with pytest.raises(SystemExit):
        adhoc_cli.parse()


def test_with_command():
    """ Test simple adhoc command"""
    module_name = 'command'
    adhoc_cli = AdHocCLI(args=['quantum', '-m', module_name, '-vv', 'localhost'])
    adhoc_cli.parse()
    assert context.CLIARGS['module_name'] == module_name
    assert display.verbosity == 2


def test_simple_command():
    """ Test valid command and its run"""
    adhoc_cli = AdHocCLI(['/bin/quantum', '-m', 'command', 'localhost', '-a', 'echo "hi"'])
    adhoc_cli.parse()
    ret = adhoc_cli.run()
    assert ret == 0


def test_no_argument():
    """ Test no argument command"""
    adhoc_cli = AdHocCLI(['/bin/quantum', '-m', 'command', 'localhost'])
    adhoc_cli.parse()
    with pytest.raises(QuantumOptionsError) as exec_info:
        adhoc_cli.run()
    assert 'No argument passed to command module' == str(exec_info.value)


def test_did_you_mean_coupling():
    """ Test adhoc with yml file as argument parameter"""
    adhoc_cli = AdHocCLI(['/bin/quantum', '-m', 'command', 'localhost.yml'])
    adhoc_cli.parse()
    with pytest.raises(QuantumOptionsError) as exec_info:
        adhoc_cli.run()
    assert 'No argument passed to command module (did you mean to run quantum-coupling?)' == str(exec_info.value)


def test_play_ds_positive():
    """ Test _play_ds"""
    adhoc_cli = AdHocCLI(args=['/bin/quantum', 'localhost', '-m', 'command'])
    adhoc_cli.parse()
    ret = adhoc_cli._play_ds('command', 10, 2)
    assert ret['name'] == 'Quantum Ad-Hoc'
    assert ret['tasks'] == [{'action': {'module': 'command', 'args': {}}, 'async_val': 10, 'poll': 2}]


def test_play_ds_with_include_role():
    """ Test include_role command with poll"""
    adhoc_cli = AdHocCLI(args=['/bin/quantum', 'localhost', '-m', 'include_role'])
    adhoc_cli.parse()
    ret = adhoc_cli._play_ds('include_role', None, 2)
    assert ret['name'] == 'Quantum Ad-Hoc'
    assert ret['gather_facts'] == 'no'


def test_run_import_coupling():
    """ Test import_coupling which is not allowed with ad-hoc command"""
    import_coupling = 'import_coupling'
    adhoc_cli = AdHocCLI(args=['/bin/quantum', '-m', import_coupling, 'localhost'])
    adhoc_cli.parse()
    with pytest.raises(QuantumOptionsError) as exec_info:
        adhoc_cli.run()
    assert context.CLIARGS['module_name'] == import_coupling
    assert "'%s' is not a valid action for ad-hoc commands" % import_coupling == str(exec_info.value)


def test_run_no_extra_vars():
    adhoc_cli = AdHocCLI(args=['/bin/quantum', 'localhost', '-e'])
    with pytest.raises(SystemExit) as exec_info:
        adhoc_cli.parse()
    assert exec_info.value.code == 2


def test_quantum_version(capsys, mocker):
    adhoc_cli = AdHocCLI(args=['/bin/quantum', '--version'])
    with pytest.raises(SystemExit):
        adhoc_cli.run()
    version = capsys.readouterr()
    try:
        version_lines = version.out.splitlines()
    except AttributeError:
        # Python 2.6 does return a named tuple, so get the first item
        version_lines = version[0].splitlines()

    assert len(version_lines) == 6, 'Incorrect number of lines in "quantum --version" output'
    assert re.match('quantum [0-9.a-z]+$', version_lines[0]), 'Incorrect quantum version line in "quantum --version" output'
    assert re.match('  config file = .*$', version_lines[1]), 'Incorrect config file line in "quantum --version" output'
    assert re.match('  configured module search path = .*$', version_lines[2]), 'Incorrect module search path in "quantum --version" output'
    assert re.match('  quantum python module location = .*$', version_lines[3]), 'Incorrect python module location in "quantum --version" output'
    assert re.match('  executable location = .*$', version_lines[4]), 'Incorrect executable locaction in "quantum --version" output'
    assert re.match('  python version = .*$', version_lines[5]), 'Incorrect python version in "quantum --version" output'
