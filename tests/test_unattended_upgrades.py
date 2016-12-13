from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_unattended_upgrades(Service, Package, File, Command):
    assert Package('unattended-upgrades').is_installed
    assert Service('unattended-upgrades').is_enabled
    assert File('/etc/apt/apt.conf.d/50unattended-upgrades').is_file
    assert Command('/usr/bin/unattended-upgrade --dry-run').rc == 0
