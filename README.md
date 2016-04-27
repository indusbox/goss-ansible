
# ansible-goss

Launch Goss (https://github.com/aelsabbahy/goss) test file with Ansible.

## Installation

Copy the **goss.py** file into your Ansible **library** directory. That's it !

## Quick start

### Simple example

Validate a Goss test file (the test file must be on the remote machine) :

```yaml
- name: test goss file
  goss:
    path: "/path/to/file.yml"
```

If a test fail, the module return an error. if you want to ignore this error, add **ignore_errors: yes** on the task.

### output format and output file

You can change the output format in a format supported by goss with the option **format** :

```yaml
- name: test goss file
  goss:
    path: "/path/to/file.yml"
    format: json
```

You can save the output of the goss command in a file with the option **output_file**:

```yaml
- name: test goss file
  goss:
    path: "/path/to/file.yml"
    format: json
    output_file : /my/output/file.json
```

### changed = False

We use this module for testing/validation purposes. Actually, this module always return **changed = False**, even with the **output_file** option.

## Module documentation

```yaml

description:
    - Launch goss test. Always changed = False if success.
options:
    path:
        required: true
        description:
            - Test file to validate. Must be on the remote machine.
    format:
        required: false
        description:
            - change the output goss format.
            - Goss format list : goss v --format => [documentation json junit nagios rspecish tap].
            - Default: None
    output_file:
        required: false
        description:
            - save the result of the goss command in a file whose path is output_file
examples:
    - name: test goss file
      goss:
        path: "/path/to/file.yml"

    - name: test goss files
      goss:
        path: "{{ item }}"
        format: json
        output_file : /my/output/file-{{ item }}
        with_items: "{{ goss_files }}"

```
