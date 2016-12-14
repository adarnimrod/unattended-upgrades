from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_unattended_upgrades_service(Service):
    assert Service('unattended-upgrades').is_enabled
    assert Service('unattended-upgrades').is_running


def test_unattended_upgrades_package(Package):
    assert Package('unattended-upgrades').is_installed


def test_unattended_upgrades_config(File):
    assert File('/etc/apt/apt.conf.d/50unattended-upgrades').is_file
    assert File('/etc/apt/apt.conf.d/02periodic').is_file


def test_unattended_upgrades_dry_run(Command, Sudo):
    with Sudo():
        assert Command('/usr/bin/unattended-upgrade --dry-run').rc == 0
