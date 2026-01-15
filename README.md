# ansible-role-cyhy-core #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-core/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-core/actions)
[![License](https://img.shields.io/github/license/cisagov/ansible-role-cyhy-core)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/ansible-role-cyhy-core/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-core/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cyhy-core](https://github.com/cisagov/cyhy-core).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| cyhy\_core\_install\_geoipupdate | Whether to install the MaxMind geoipupdate tool. | `false` | No |
| cyhy\_core\_maxmind\_account\_id | The MaxMind account ID for access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_core\_maxmind\_license\_key | The MaxMind license key that provides access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_core\_version | The version of cisagov/cyhy-core to install; must be a valid git reference. | `v1.1.13` | No |

## Dependencies ##

- [cisagov/ansible-role-geoip2](https://github.com/cisagov/ansible-role-geoip2)
- [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)
- [cisagov/ansible-role-python](https://github.com/cisagov/ansible-role-python)

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: cyhy_core
  src: https://github.com/cisagov/ansible-role-cyhy-core
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install cisagov/cyhy-core
      ansible.builtin.include_role:
        name: cyhy_core
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
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

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
