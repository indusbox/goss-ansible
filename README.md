
# ansible-goss

Launch [Goss](https://github.com/aelsabbahy/goss) test file with Ansible.

## Installation

Copy the `goss.py` file into your Ansible `library` directory. That's it!

## Quick start

### Simple example

Validate a Goss test file (the test file must be on the remote machine):

```yaml
- name: test goss file
  goss:
    path: "/path/to/file.yml"
```

If a test fails, the module returns an error.
If you want to ignore this error, add `ignore_errors: yes` on the task.

### Output format and output file

You can change the output format with the `format` option:

```yaml
- name: test goss file
  goss:
    path: "/path/to/file.yml"
    format: json
```

See all the supported output format: https://github.com/aelsabbahy/goss#supported-output-formats

You can also save the output of the `goss` command in a file with the `output_file` option:

```yaml
- name: test goss file
  goss:
    path: "/path/to/file.yml"
    format: json
    output_file : /my/output/file.json
```

### Changed = False

We use this module for testing/validation purposes.
Therefore, this module always returns `changed = false`, even with the `output_file` option.

## Ansible versions

Tested with :

- Ansible 1.8.2
- Ansible 2.0.2
- Ansible 2.2.2

## Module documentation

```yaml
module: goss
author: Mathieu Corbin
short_description: Launch goss (https://github.com/aelsabbahy/goss) tests
description:
  - Launch goss tests.
    This module always returns `changed = false` for idempotence.
options:
  path:
    required: true
    description:
      - Test file to validate.
        The test file must be on the remote machine.
  goss_path:
    required: false
    description:
      - Path location for the goss executable.
        Default is "goss" (ie.`no absolute path,  goss executable must be available in $PATH).
  format:
    required: false
    description:
      - Output goss format.
        Goss format list : goss v --format => [documentation json junit nagios nagios_verbose rspecish tap silent].
        Default is "rspecish".
  output_file:
    required: false
    description:
      - Save the result of the goss command in a file whose path is output_file

examples:
  - name: run goss against the gossfile /path/to/file.yml
    goss:
      path: "/path/to/file.yml"

  - name: run goss against the gossfile /path/to/file.yml with nagios output
    goss:
      path: "/path/to/file.yml"
      format: "nagios"

  - name: run /usr/local/bin/goss against the gossfile /path/to/file.yml
    goss:
      path: "/path/to/file.yml"
      goss_path: "/usr/local/bin/goss"

  - name: run goss against multiple gossfiles and write the result in JSON format to /my/output/ for each file
    goss:
      path: "{{ item }}"
      format: json
      output_file : /my/output/{{ item }}
    with_items: "{{ goss_files }}"
```
