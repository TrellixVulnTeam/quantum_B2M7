#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_iam_service_account
description:
- A service account in the Identity and Access Management API.
short_description: Creates a GCP ServiceAccount
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - The name of the service account.
    required: false
    type: str
  display_name:
    description:
    - User specified description of service account.
    required: false
    type: str
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a service account
  gcp_iam_service_account:
    name: sa-{{ resource_name.split("-")[-1] }}@graphite-playground.google.com.iam.gserviceaccount.com
    display_name: My Quantum test key
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The name of the service account.
  returned: success
  type: str
projectId:
  description:
  - Id of the project that owns the service account.
  returned: success
  type: str
uniqueId:
  description:
  - Unique and stable id of the service account.
  returned: success
  type: str
email:
  description:
  - Email address of the service account.
  returned: success
  type: str
displayName:
  description:
  - User specified description of service account.
  returned: success
  type: str
oauth2ClientId:
  description:
  - OAuth2 client id for the service account.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from quantum.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(state=dict(default='present', choices=['present', 'absent'], type='str'), name=dict(type='str'), display_name=dict(type='str'))
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/iam']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'iam')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    auth = GcpSession(module, 'iam')
    return return_if_object(module, auth.put(link, resource_to_request(module)))


def delete(module, link):
    auth = GcpSession(module, 'iam')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {u'name': module.params.get('name'), u'displayName': module.params.get('display_name')}
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'iam')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://iam.googleapis.com/v1/projects/{project}/serviceAccounts/{name}".format(**module.params)


def collection(module):
    return "https://iam.googleapis.com/v1/projects/{project}/serviceAccounts".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_response(request, module)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Quantum's current parameters.
def response_to_hash(module, response):
    return {
        u'name': response.get(u'name'),
        u'projectId': response.get(u'projectId'),
        u'uniqueId': response.get(u'uniqueId'),
        u'email': response.get(u'email'),
        u'displayName': response.get(u'displayName'),
        u'oauth2ClientId': response.get(u'oauth2ClientId'),
    }


def encode_request(resource_request, module):
    """Structures the request as accountId + rest of request"""
    account_id = resource_request['name'].split('@')[0]
    del resource_request['name']
    return {'accountId': account_id, 'serviceAccount': resource_request}


def decode_response(response, module):
    """Unstructures the request from accountId + rest of request"""
    if 'name' not in response:
        return response
    response['name'] = response['name'].split('/')[-1]
    return response


if __name__ == '__main__':
    main()
