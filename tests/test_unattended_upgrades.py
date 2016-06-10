def test_unattended_upgrades(Service, Package, File):
    assert Package('unattended-upgrades').is_installed
    assert Service('unattended-upgrades').is_enabled
    assert File('/etc/apt/apt.conf.d/20auto-upgrades').is_file
