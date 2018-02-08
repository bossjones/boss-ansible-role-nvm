import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# Good example: https://github.com/nephelaiio/ansible-role-rbenv/blob/4771cdc2ee559b78d29929ab0700e8fca15019ab/molecule/compile/tests/test_compile.py

nvm_version = 'v0.33.1'

def test_nvm_folders(host):
    f = host.file('/home/vagrant/.nvm')

    assert f.exists
    assert f.user == 'vagrant'
    assert f.group == 'vagrant'

    f = host.file('/home/vagrant/.nvm/alias/default')
    assert f.exists
    assert f.user == 'vagrant'
    assert f.group == 'vagrant'

    f = host.file('/etc/profile.d/nvm.sh')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nvm_installs(host):
    with host.sudo():
        assert host.user().name == "root"
        with host.sudo("vagrant"):
            assert host.user().name == "vagrant"
            # npm_list = host.check_output("npm list -g --depth=0")
            # cmd = '/bin/bash -l -c "nvm use stable && npm list -g --depth=0"'
            # assert host.check_output(cmd) == 0
            # assert "vtop" in host.check_output('bash -c -l "npm list -g --depth=0"')


