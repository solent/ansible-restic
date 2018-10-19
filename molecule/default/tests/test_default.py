import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_binary(host):
    binary = host.file("/usr/local/bin/restic")
    assert binary.exists
    assert binary.is_file
    assert binary.mode == 0o750


def test_cronfiles(host):
    cronfiles = [
        "/etc/cron.d/restic-local-example"
    ]
    for file in cronfiles:
        f = host.file(file)
        assert f.exists
        assert f.is_file
        assert f.mode == 0o640
        assert f.contains('export RESTIC_PASSWORD=correcthorsebatterystaple')
        assert f.contains('MAILTO=backup.molecule.default@domain.tld')
#
#
# def test_logdir(host):
#     logdir = host.file("/var/log/restic")
#     assert logdir.is_directory
#     assert logdir.exists
