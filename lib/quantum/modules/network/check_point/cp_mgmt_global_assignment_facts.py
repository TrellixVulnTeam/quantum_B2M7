#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Quantum module to manage Check Point Firewall (c) 2019
#
# Quantum is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Quantum is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Quantum.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: cp_mgmt_global_assignment_facts
short_description: Get global-assignment objects facts on Check Point over Web Services API
description:
  - Get global-assignment objects facts on Check Point devices.
  - All operations are performed over Web Services API.
  - This module handles both operations, get a specific object and get several objects,
    For getting a specific object use the parameter 'name'.
version_added: "2.9"
author: "Or Soffer (@chkp-orso)"
options:
  dependent_domain:
    description:
      - N/A
    type: str
  global_domain:
    description:
      - N/A
    type: str
  details_level:
    description:
      - The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed
        representation of the object.
    type: str
    choices: ['uid', 'standard', 'full']
  limit:
    description:
      - No more than that many results will be returned.
        This parameter is relevant only for getting few objects.
    type: int
  offset:
    description:
      - Skip that many results before beginning to return them.
        This parameter is relevant only for getting few objects.
    type: int
  order:
    description:
      - Sorts results by the given field. By default the results are sorted in the ascending order by name.
        This parameter is relevant only for getting few objects.
    type: list
    suboptions:
      ASC:
        description:
          - Sorts results by the given field in ascending order.
        type: str
        choices: ['name']
      DESC:
        description:
          - Sorts results by the given field in descending order.
        type: str
        choices: ['name']
extends_documentation_fragment: checkpoint_facts
"""

EXAMPLES = """
- name: show-global-assignment
  cp_mgmt_global_assignment_facts:
    dependent_domain: domain1
    global_domain: Global2

- name: show-global-assignments
  cp_mgmt_global_assignment_facts:
    details_level: standard
    limit: 50
    offset: 0
"""

RETURN = """
quantum_facts:
  description: The checkpoint object facts.
  returned: always.
  type: dict
"""

from quantum.module_utils.basic import QuantumModule
from quantum.module_utils.network.checkpoint.checkpoint import checkpoint_argument_spec_for_facts, api_call_facts


def main():
    argument_spec = dict(
        dependent_domain=dict(type='str'),
        global_domain=dict(type='str'),
        details_level=dict(type='str', choices=['uid', 'standard', 'full']),
        limit=dict(type='int'),
        offset=dict(type='int'),
        order=dict(type='list', options=dict(
            ASC=dict(type='str', choices=['name']),
            DESC=dict(type='str', choices=['name'])
        ))
    )
    argument_spec.update(checkpoint_argument_spec_for_facts)

    module = QuantumModule(argument_spec=argument_spec)

    api_call_object = "global-assignment"
    api_call_object_plural_version = "global-assignments"

    result = api_call_facts(module, api_call_object, api_call_object_plural_version)
    module.exit_json(quantum_facts=result)


if __name__ == '__main__':
    main()