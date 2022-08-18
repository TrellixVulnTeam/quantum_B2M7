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
module: gcp_mlengine_version
description:
- Each version is a trained model deployed in the cloud, ready to handle prediction
  requests. A model can have multiple versions .
short_description: Creates a GCP Version
version_added: 2.9
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
    - The name specified for the version when it was created.
    - The version name must be unique within the model it is created in.
    required: true
    type: str
  description:
    description:
    - The description specified for the version when it was created.
    required: false
    type: str
  deployment_uri:
    description:
    - The Cloud Storage location of the trained model used to create the version.
    required: true
    type: str
  runtime_version:
    description:
    - The AI Platform runtime version to use for this deployment.
    required: false
    type: str
  machine_type:
    description:
    - The type of machine on which to serve the model. Currently only applies to online
      prediction service.
    - 'Some valid choices include: "mls1-c1-m2", "mls1-c4-m2"'
    required: false
    type: str
  labels:
    description:
    - One or more labels that you can add, to organize your model versions.
    required: false
    type: dict
  framework:
    description:
    - The machine learning framework AI Platform uses to train this version of the
      model.
    - 'Some valid choices include: "FRAMEWORK_UNSPECIFIED", "TENSORFLOW", "SCIKIT_LEARN",
      "XGBOOST"'
    required: false
    type: str
  python_version:
    description:
    - The version of Python used in prediction. If not set, the default version is
      '2.7'. Python '3.5' is available when runtimeVersion is set to '1.4' and above.
      Python '2.7' works with all supported runtime versions.
    - 'Some valid choices include: "2.7", "3.5"'
    required: false
    type: str
  service_account:
    description:
    - Specifies the service account for resource access control.
    required: false
    type: str
  auto_scaling:
    description:
    - Automatically scale the number of nodes used to serve the model in response
      to increases and decreases in traffic. Care should be taken to ramp up traffic
      according to the model's ability to scale or you will start seeing increases
      in latency and 429 response codes.
    required: false
    type: dict
    suboptions:
      min_nodes:
        description:
        - The minimum number of nodes to allocate for this mode.
        required: false
        type: int
  manual_scaling:
    description:
    - Manually select the number of nodes to use for serving the model. You should
      generally use autoScaling with an appropriate minNodes instead, but this option
      is available if you want more predictable billing. Beware that latency and error
      rates will increase if the traffic exceeds that capability of the system to
      serve it based on the selected number of nodes.
    required: false
    type: dict
    suboptions:
      nodes:
        description:
        - The number of nodes to allocate for this model. These nodes are always up,
          starting from the time the model is deployed.
        required: false
        type: int
  prediction_class:
    description:
    - The fully qualified name (module_name.class_name) of a class that implements
      the Predictor interface described in this reference field. The module containing
      this class should be included in a package provided to the packageUris field.
    required: false
    type: str
  model:
    description:
    - The model that this version belongs to.
    - 'This field represents a link to a Model resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_mlengine_model task and then set this model field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  is_default:
    description:
    - If true, this version will be used to handle prediction requests that do not
      specify a version.
    required: false
    type: bool
    aliases:
    - default
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a model
  gcp_mlengine_model:
    name: model_version
    description: My model
    regions:
    - us-central1
    online_prediction_logging: 'true'
    online_prediction_console_logging: 'true'
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: model

- name: create a version
  gcp_mlengine_version:
    name: "{{ resource_name | replace('-', '_') }}"
    model: "{{ model }}"
    runtime_version: 1.13
    python_version: 3.5
    is_default: 'true'
    deployment_uri: gs://quantum-cloudml-bucket/
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The name specified for the version when it was created.
  - The version name must be unique within the model it is created in.
  returned: success
  type: str
description:
  description:
  - The description specified for the version when it was created.
  returned: success
  type: str
deploymentUri:
  description:
  - The Cloud Storage location of the trained model used to create the version.
  returned: success
  type: str
createTime:
  description:
  - The time the version was created.
  returned: success
  type: str
lastUseTime:
  description:
  - The time the version was last used for prediction.
  returned: success
  type: str
runtimeVersion:
  description:
  - The AI Platform runtime version to use for this deployment.
  returned: success
  type: str
machineType:
  description:
  - The type of machine on which to serve the model. Currently only applies to online
    prediction service.
  returned: success
  type: str
state:
  description:
  - The state of a version.
  returned: success
  type: str
errorMessage:
  description:
  - The details of a failure or cancellation.
  returned: success
  type: str
packageUris:
  description:
  - Cloud Storage paths (gs://…) of packages for custom prediction routines or scikit-learn
    pipelines with custom code.
  returned: success
  type: list
labels:
  description:
  - One or more labels that you can add, to organize your model versions.
  returned: success
  type: dict
framework:
  description:
  - The machine learning framework AI Platform uses to train this version of the model.
  returned: success
  type: str
pythonVersion:
  description:
  - The version of Python used in prediction. If not set, the default version is '2.7'.
    Python '3.5' is available when runtimeVersion is set to '1.4' and above. Python
    '2.7' works with all supported runtime versions.
  returned: success
  type: str
serviceAccount:
  description:
  - Specifies the service account for resource access control.
  returned: success
  type: str
autoScaling:
  description:
  - Automatically scale the number of nodes used to serve the model in response to
    increases and decreases in traffic. Care should be taken to ramp up traffic according
    to the model's ability to scale or you will start seeing increases in latency
    and 429 response codes.
  returned: success
  type: complex
  contains:
    minNodes:
      description:
      - The minimum number of nodes to allocate for this mode.
      returned: success
      type: int
manualScaling:
  description:
  - Manually select the number of nodes to use for serving the model. You should generally
    use autoScaling with an appropriate minNodes instead, but this option is available
    if you want more predictable billing. Beware that latency and error rates will
    increase if the traffic exceeds that capability of the system to serve it based
    on the selected number of nodes.
  returned: success
  type: complex
  contains:
    nodes:
      description:
      - The number of nodes to allocate for this model. These nodes are always up,
        starting from the time the model is deployed.
      returned: success
      type: int
predictionClass:
  description:
  - The fully qualified name (module_name.class_name) of a class that implements the
    Predictor interface described in this reference field. The module containing this
    class should be included in a package provided to the packageUris field.
  returned: success
  type: str
model:
  description:
  - The model that this version belongs to.
  returned: success
  type: dict
isDefault:
  description:
  - If true, this version will be used to handle prediction requests that do not specify
    a version.
  returned: success
  type: bool
'''

################################################################################
# Imports
################################################################################

from quantum.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            deployment_uri=dict(required=True, type='str'),
            runtime_version=dict(type='str'),
            machine_type=dict(type='str'),
            labels=dict(type='dict'),
            framework=dict(type='str'),
            python_version=dict(type='str'),
            service_account=dict(type='str'),
            auto_scaling=dict(type='dict', options=dict(min_nodes=dict(type='int'))),
            manual_scaling=dict(type='dict', options=dict(nodes=dict(type='int'))),
            prediction_class=dict(type='str'),
            model=dict(required=True, type='dict'),
            is_default=dict(type='bool', aliases=['default']),
        ),
        mutually_exclusive=[['auto_scaling', 'manual_scaling']],
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

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
            if module.params.get('is_default') is True:
                set_default(module)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'mlengine')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    if module.params.get('is_default') is True:
        set_default(module)


def delete(module, link):
    auth = GcpSession(module, 'mlengine')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'deploymentUri': module.params.get('deployment_uri'),
        u'runtimeVersion': module.params.get('runtime_version'),
        u'machineType': module.params.get('machine_type'),
        u'labels': module.params.get('labels'),
        u'framework': module.params.get('framework'),
        u'pythonVersion': module.params.get('python_version'),
        u'serviceAccount': module.params.get('service_account'),
        u'autoScaling': VersionAutoscaling(module.params.get('auto_scaling', {}), module).to_request(),
        u'manualScaling': VersionManualscaling(module.params.get('manual_scaling', {}), module).to_request(),
        u'predictionClass': module.params.get('prediction_class'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'mlengine')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    res = {'project': module.params['project'], 'model': replace_resource_dict(module.params['model'], 'name'), 'name': module.params['name']}
    return "https://ml.googleapis.com/v1/projects/{project}/models/{model}/versions/{name}".format(**res)


def collection(module):
    res = {'project': module.params['project'], 'model': replace_resource_dict(module.params['model'], 'name')}
    return "https://ml.googleapis.com/v1/projects/{project}/models/{model}/versions".format(**res)


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
        u'description': response.get(u'description'),
        u'deploymentUri': response.get(u'deploymentUri'),
        u'createTime': response.get(u'createTime'),
        u'lastUseTime': response.get(u'lastUseTime'),
        u'runtimeVersion': response.get(u'runtimeVersion'),
        u'machineType': response.get(u'machineType'),
        u'state': response.get(u'state'),
        u'errorMessage': response.get(u'errorMessage'),
        u'packageUris': response.get(u'packageUris'),
        u'labels': response.get(u'labels'),
        u'framework': response.get(u'framework'),
        u'pythonVersion': response.get(u'pythonVersion'),
        u'serviceAccount': response.get(u'serviceAccount'),
        u'autoScaling': VersionAutoscaling(response.get(u'autoScaling', {}), module).from_response(),
        u'manualScaling': VersionManualscaling(response.get(u'manualScaling', {}), module).from_response(),
        u'predictionClass': response.get(u'predictionClass'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://ml.googleapis.com/v1/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['done'])
    wait_done = wait_for_completion(status, op_result, module)
    raise_if_errors(wait_done, ['error'], module)
    return navigate_hash(wait_done, ['response'])


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while not status:
        raise_if_errors(op_result, ['error'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ['done'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


# Short names are given (and expected) by the API
# but are returned as full names.
def decode_response(response, module):
    if 'name' in response and 'metadata' not in response:
        response['name'] = response['name'].split('/')[-1]
    return response


# Sets this version as default.
def set_default(module):
    res = {'project': module.params['project'], 'model': replace_resource_dict(module.params['model'], 'name'), 'name': module.params['name']}
    link = "https://ml.googleapis.com/v1/projects/{project}/models/{model}/versions/{name}:setDefault".format(**res)

    auth = GcpSession(module, 'mlengine')
    return_if_object(module, auth.post(link))


class VersionAutoscaling(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'minNodes': self.request.get('min_nodes')})

    def from_response(self):
        return remove_nones_from_dict({u'minNodes': self.request.get(u'minNodes')})


class VersionManualscaling(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'nodes': self.request.get('nodes')})

    def from_response(self):
        return remove_nones_from_dict({u'nodes': self.request.get(u'nodes')})


if __name__ == '__main__':
    main()
