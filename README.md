# ansible-role-cyhy-core #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-core/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-core/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-cyhy-core.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-cyhy-core/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-cyhy-core.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-cyhy-core/context:python)

An Ansible role for installing
[cyhy-core](https://github.com/cisagov/cyhy-core).

## Requirements ##

* The [boto3](https://pypi.org/project/boto3/) Python package for performing
  `lookup()`s of AWS SSM Parameter Store keys.

## Role Variables ##

* `maxmind_license_key` - The MaxMind license key that provides access to a
  GeoIP2 database subscription.

## Dependencies ##

* [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - cyhy_core
```

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
