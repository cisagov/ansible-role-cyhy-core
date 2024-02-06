"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "pkg",
    [
        "python-crypto",
        "python-dateutil",
        "python-docopt",
        "python-geoip2",
        "python-maxminddb",
        "python-netaddr",
        "python-pandas",
        "python-progressbar",
        "python-six",
        "python-unidecode",
        "python-yaml",
    ],
)
def test_apt_packages(host, pkg):
    """Test that the apt packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["cyhy-core"])
def test_pip_packages(host, pkg):
    """Test that the pip packages were installed."""
    assert pkg in host.pip.get_packages(pip_path="/usr/bin/pip2")
