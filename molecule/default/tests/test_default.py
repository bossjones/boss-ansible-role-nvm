import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nvm_installs(host):
    f = host.file('/home/vagrant/.nvm')

    assert f.exists
    assert f.user == 'vagrant'
    assert f.group == 'vagrant'

    # with host.sudo("vagrant"):
    #     # npm_list = host.check_output("npm list -g --depth=0")
    #     assert "vtop" in host.check_output('bash -c "npm list -g --depth=0"')
