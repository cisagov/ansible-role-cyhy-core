"""Module containing the tests for the default scenario."""

import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["cyhy-core"])
def test_packages(host, pkg):
    """Test that the pip packages were installed."""
    assert pkg in host.pip_package.get_packages()


@pytest.mark.parametrize("f", ["/var/cyhy/core"])
def test_files(host, f):
    """Test that the expected files and directories are present."""
    assert host.file(f).exists
