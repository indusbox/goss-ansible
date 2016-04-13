#!/usr/bin/env python

DOCUMENTATION = '''
---
module: goss
author: Mathieu Corbin
short_description: Launch goss (https://github.com/aelsabbahy/goss) test
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
'''

# launch goss validate command on the file
def check(module, file_path, output_format):
    cmd = ""
    if output_format != None:
        cmd = "goss -g {0} v --format {1}".format(file_path, output_format)
    else:
        cmd = "goss -g {0} v".format(file_path)
    return module.run_command(cmd)

#write goss result to output_file_path
def output_file(output_file_path, out):
    if output_file_path != None:
        with open(output_file_path, 'w') as output_file:
            output_file.write(out)

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, type='str'),
            format = dict(required=False, type='str'),
            output_file = dict(required=False, type='str'),
        ),
        supports_check_mode=False
    )

    file_path = module.params['path']
    output_format = module.params['format']
    output_file_path = module.params['output_file']

    (rc, out, err) = check(module, file_path, output_format)

    output_file(output_file_path, out)

    if rc is not None and rc != 0:
        error_msg = "err : {0} ; out : {1}".format(err, out)
        module.fail_json(msg=error_msg)

    result = {}
    result['stdout'] = out
    result['changed'] = False

    module.exit_json(**result)

# import module snippets
from ansible.module_utils.basic import *
main()
