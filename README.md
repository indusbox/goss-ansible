
# ansible-goss

Launch Goss (https://github.com/aelsabbahy/goss) test file with Ansible.

```yaml

description:
    - Launch goss test. Always changed = False if success.
options:
    path:
        required: true
        description:
            - Test file to validate. Must on the remote machine.
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
