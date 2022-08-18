# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Quantum.  If not, see <https://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import json
import pytest
from mock import ANY
from quantum.module_utils.network.fortios.fortios import FortiOSHandler

try:
    from quantum.modules.network.fortios import fortios_firewall_vip6
except ImportError:
    pytest.skip("Could not load required modules for testing", allow_module_level=True)


@pytest.fixture(autouse=True)
def connection_mock(mocker):
    connection_class_mock = mocker.patch('quantum.modules.network.fortios.fortios_firewall_vip6.Connection')
    return connection_class_mock


fos_instance = FortiOSHandler(connection_mock)


def test_firewall_vip6_creation(mocker):
    schema_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    set_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_vip6': {
            'arp_reply': 'disable',
            'color': '4',
            'comment': 'Comment.',
            'extip': 'test_value_6',
            'extport': 'test_value_7',
            'http_cookie_age': '8',
            'http_cookie_domain': 'test_value_9',
            'http_cookie_domain_from_host': 'disable',
            'http_cookie_generation': '11',
            'http_cookie_path': 'test_value_12',
            'http_cookie_share': 'disable',
            'http_ip_header': 'enable',
            'http_ip_header_name': 'test_value_15',
            'http_multiplex': 'enable',
            'https_cookie_secure': 'disable',
            'id': '18',
            'ldb_method': 'static',
            'mappedip': 'test_value_20',
            'mappedport': 'test_value_21',
            'max_embryonic_connections': '22',
            'name': 'default_name_23',
            'outlook_web_access': 'disable',
            'persistence': 'none',
            'portforward': 'disable',
            'protocol': 'tcp',
            'server_type': 'http',
            'ssl_algorithm': 'high',
            'ssl_certificate': 'test_value_30',
            'ssl_client_fallback': 'disable',
            'ssl_client_renegotiation': 'allow',
            'ssl_client_session_state_max': '33',
            'ssl_client_session_state_timeout': '34',
            'ssl_client_session_state_type': 'disable',
            'ssl_dh_bits': '768',
            'ssl_hpkp': 'disable',
            'ssl_hpkp_age': '38',
            'ssl_hpkp_backup': 'test_value_39',
            'ssl_hpkp_include_subdomains': 'disable',
            'ssl_hpkp_primary': 'test_value_41',
            'ssl_hpkp_report_uri': 'test_value_42',
            'ssl_hsts': 'disable',
            'ssl_hsts_age': '44',
            'ssl_hsts_include_subdomains': 'disable',
            'ssl_http_location_conversion': 'enable',
            'ssl_http_match_host': 'enable',
            'ssl_max_version': 'ssl-3.0',
            'ssl_min_version': 'ssl-3.0',
            'ssl_mode': 'half',
            'ssl_pfs': 'require',
            'ssl_send_empty_frags': 'enable',
            'ssl_server_algorithm': 'high',
            'ssl_server_max_version': 'ssl-3.0',
            'ssl_server_min_version': 'ssl-3.0',
            'ssl_server_session_state_max': '56',
            'ssl_server_session_state_timeout': '57',
            'ssl_server_session_state_type': 'disable',
            'type': 'static-nat',
            'uuid': 'test_value_60',
            'weblogic_server': 'disable',
            'websphere_server': 'disable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_vip6.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'arp-reply': 'disable',
        'color': '4',
        'comment': 'Comment.',
        'extip': 'test_value_6',
        'extport': 'test_value_7',
        'http-cookie-age': '8',
        'http-cookie-domain': 'test_value_9',
        'http-cookie-domain-from-host': 'disable',
        'http-cookie-generation': '11',
        'http-cookie-path': 'test_value_12',
        'http-cookie-share': 'disable',
        'http-ip-header': 'enable',
        'http-ip-header-name': 'test_value_15',
        'http-multiplex': 'enable',
        'https-cookie-secure': 'disable',
        'id': '18',
        'ldb-method': 'static',
        'mappedip': 'test_value_20',
        'mappedport': 'test_value_21',
        'max-embryonic-connections': '22',
        'name': 'default_name_23',
                'outlook-web-access': 'disable',
                'persistence': 'none',
                'portforward': 'disable',
                'protocol': 'tcp',
                'server-type': 'http',
                'ssl-algorithm': 'high',
                'ssl-certificate': 'test_value_30',
                'ssl-client-fallback': 'disable',
                'ssl-client-renegotiation': 'allow',
                'ssl-client-session-state-max': '33',
                'ssl-client-session-state-timeout': '34',
                'ssl-client-session-state-type': 'disable',
                'ssl-dh-bits': '768',
                'ssl-hpkp': 'disable',
                'ssl-hpkp-age': '38',
                'ssl-hpkp-backup': 'test_value_39',
                'ssl-hpkp-include-subdomains': 'disable',
                'ssl-hpkp-primary': 'test_value_41',
                'ssl-hpkp-report-uri': 'test_value_42',
                'ssl-hsts': 'disable',
                'ssl-hsts-age': '44',
                'ssl-hsts-include-subdomains': 'disable',
                'ssl-http-location-conversion': 'enable',
                'ssl-http-match-host': 'enable',
                'ssl-max-version': 'ssl-3.0',
                'ssl-min-version': 'ssl-3.0',
                'ssl-mode': 'half',
                'ssl-pfs': 'require',
                'ssl-send-empty-frags': 'enable',
                'ssl-server-algorithm': 'high',
                'ssl-server-max-version': 'ssl-3.0',
                'ssl-server-min-version': 'ssl-3.0',
                'ssl-server-session-state-max': '56',
                'ssl-server-session-state-timeout': '57',
                'ssl-server-session-state-type': 'disable',
                'type': 'static-nat',
                'uuid': 'test_value_60',
                'weblogic-server': 'disable',
                'websphere-server': 'disable'
    }

    set_method_mock.assert_called_with('firewall', 'vip6', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200


def test_firewall_vip6_creation_fails(mocker):
    schema_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'error', 'http_method': 'POST', 'http_status': 500}
    set_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_vip6': {
            'arp_reply': 'disable',
            'color': '4',
            'comment': 'Comment.',
            'extip': 'test_value_6',
            'extport': 'test_value_7',
            'http_cookie_age': '8',
            'http_cookie_domain': 'test_value_9',
            'http_cookie_domain_from_host': 'disable',
            'http_cookie_generation': '11',
            'http_cookie_path': 'test_value_12',
            'http_cookie_share': 'disable',
            'http_ip_header': 'enable',
            'http_ip_header_name': 'test_value_15',
            'http_multiplex': 'enable',
            'https_cookie_secure': 'disable',
            'id': '18',
            'ldb_method': 'static',
            'mappedip': 'test_value_20',
            'mappedport': 'test_value_21',
            'max_embryonic_connections': '22',
            'name': 'default_name_23',
            'outlook_web_access': 'disable',
            'persistence': 'none',
            'portforward': 'disable',
            'protocol': 'tcp',
            'server_type': 'http',
            'ssl_algorithm': 'high',
            'ssl_certificate': 'test_value_30',
            'ssl_client_fallback': 'disable',
            'ssl_client_renegotiation': 'allow',
            'ssl_client_session_state_max': '33',
            'ssl_client_session_state_timeout': '34',
            'ssl_client_session_state_type': 'disable',
            'ssl_dh_bits': '768',
            'ssl_hpkp': 'disable',
            'ssl_hpkp_age': '38',
            'ssl_hpkp_backup': 'test_value_39',
            'ssl_hpkp_include_subdomains': 'disable',
            'ssl_hpkp_primary': 'test_value_41',
            'ssl_hpkp_report_uri': 'test_value_42',
            'ssl_hsts': 'disable',
            'ssl_hsts_age': '44',
            'ssl_hsts_include_subdomains': 'disable',
            'ssl_http_location_conversion': 'enable',
            'ssl_http_match_host': 'enable',
            'ssl_max_version': 'ssl-3.0',
            'ssl_min_version': 'ssl-3.0',
            'ssl_mode': 'half',
            'ssl_pfs': 'require',
            'ssl_send_empty_frags': 'enable',
            'ssl_server_algorithm': 'high',
            'ssl_server_max_version': 'ssl-3.0',
            'ssl_server_min_version': 'ssl-3.0',
            'ssl_server_session_state_max': '56',
            'ssl_server_session_state_timeout': '57',
            'ssl_server_session_state_type': 'disable',
            'type': 'static-nat',
            'uuid': 'test_value_60',
            'weblogic_server': 'disable',
            'websphere_server': 'disable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_vip6.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'arp-reply': 'disable',
        'color': '4',
        'comment': 'Comment.',
        'extip': 'test_value_6',
        'extport': 'test_value_7',
        'http-cookie-age': '8',
        'http-cookie-domain': 'test_value_9',
        'http-cookie-domain-from-host': 'disable',
        'http-cookie-generation': '11',
        'http-cookie-path': 'test_value_12',
        'http-cookie-share': 'disable',
        'http-ip-header': 'enable',
        'http-ip-header-name': 'test_value_15',
        'http-multiplex': 'enable',
        'https-cookie-secure': 'disable',
        'id': '18',
        'ldb-method': 'static',
        'mappedip': 'test_value_20',
        'mappedport': 'test_value_21',
        'max-embryonic-connections': '22',
        'name': 'default_name_23',
                'outlook-web-access': 'disable',
                'persistence': 'none',
                'portforward': 'disable',
                'protocol': 'tcp',
                'server-type': 'http',
                'ssl-algorithm': 'high',
                'ssl-certificate': 'test_value_30',
                'ssl-client-fallback': 'disable',
                'ssl-client-renegotiation': 'allow',
                'ssl-client-session-state-max': '33',
                'ssl-client-session-state-timeout': '34',
                'ssl-client-session-state-type': 'disable',
                'ssl-dh-bits': '768',
                'ssl-hpkp': 'disable',
                'ssl-hpkp-age': '38',
                'ssl-hpkp-backup': 'test_value_39',
                'ssl-hpkp-include-subdomains': 'disable',
                'ssl-hpkp-primary': 'test_value_41',
                'ssl-hpkp-report-uri': 'test_value_42',
                'ssl-hsts': 'disable',
                'ssl-hsts-age': '44',
                'ssl-hsts-include-subdomains': 'disable',
                'ssl-http-location-conversion': 'enable',
                'ssl-http-match-host': 'enable',
                'ssl-max-version': 'ssl-3.0',
                'ssl-min-version': 'ssl-3.0',
                'ssl-mode': 'half',
                'ssl-pfs': 'require',
                'ssl-send-empty-frags': 'enable',
                'ssl-server-algorithm': 'high',
                'ssl-server-max-version': 'ssl-3.0',
                'ssl-server-min-version': 'ssl-3.0',
                'ssl-server-session-state-max': '56',
                'ssl-server-session-state-timeout': '57',
                'ssl-server-session-state-type': 'disable',
                'type': 'static-nat',
                'uuid': 'test_value_60',
                'weblogic-server': 'disable',
                'websphere-server': 'disable'
    }

    set_method_mock.assert_called_with('firewall', 'vip6', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 500


def test_firewall_vip6_removal(mocker):
    schema_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    delete_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    delete_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.delete', return_value=delete_method_result)

    input_data = {
        'username': 'admin',
        'state': 'absent',
        'firewall_vip6': {
            'arp_reply': 'disable',
            'color': '4',
            'comment': 'Comment.',
            'extip': 'test_value_6',
            'extport': 'test_value_7',
            'http_cookie_age': '8',
            'http_cookie_domain': 'test_value_9',
            'http_cookie_domain_from_host': 'disable',
            'http_cookie_generation': '11',
            'http_cookie_path': 'test_value_12',
            'http_cookie_share': 'disable',
            'http_ip_header': 'enable',
            'http_ip_header_name': 'test_value_15',
            'http_multiplex': 'enable',
            'https_cookie_secure': 'disable',
            'id': '18',
            'ldb_method': 'static',
            'mappedip': 'test_value_20',
            'mappedport': 'test_value_21',
            'max_embryonic_connections': '22',
            'name': 'default_name_23',
            'outlook_web_access': 'disable',
            'persistence': 'none',
            'portforward': 'disable',
            'protocol': 'tcp',
            'server_type': 'http',
            'ssl_algorithm': 'high',
            'ssl_certificate': 'test_value_30',
            'ssl_client_fallback': 'disable',
            'ssl_client_renegotiation': 'allow',
            'ssl_client_session_state_max': '33',
            'ssl_client_session_state_timeout': '34',
            'ssl_client_session_state_type': 'disable',
            'ssl_dh_bits': '768',
            'ssl_hpkp': 'disable',
            'ssl_hpkp_age': '38',
            'ssl_hpkp_backup': 'test_value_39',
            'ssl_hpkp_include_subdomains': 'disable',
            'ssl_hpkp_primary': 'test_value_41',
            'ssl_hpkp_report_uri': 'test_value_42',
            'ssl_hsts': 'disable',
            'ssl_hsts_age': '44',
            'ssl_hsts_include_subdomains': 'disable',
            'ssl_http_location_conversion': 'enable',
            'ssl_http_match_host': 'enable',
            'ssl_max_version': 'ssl-3.0',
            'ssl_min_version': 'ssl-3.0',
            'ssl_mode': 'half',
            'ssl_pfs': 'require',
            'ssl_send_empty_frags': 'enable',
            'ssl_server_algorithm': 'high',
            'ssl_server_max_version': 'ssl-3.0',
            'ssl_server_min_version': 'ssl-3.0',
            'ssl_server_session_state_max': '56',
            'ssl_server_session_state_timeout': '57',
            'ssl_server_session_state_type': 'disable',
            'type': 'static-nat',
            'uuid': 'test_value_60',
            'weblogic_server': 'disable',
            'websphere_server': 'disable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_vip6.fortios_firewall(input_data, fos_instance)

    delete_method_mock.assert_called_with('firewall', 'vip6', mkey=ANY, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200


def test_firewall_vip6_deletion_fails(mocker):
    schema_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    delete_method_result = {'status': 'error', 'http_method': 'POST', 'http_status': 500}
    delete_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.delete', return_value=delete_method_result)

    input_data = {
        'username': 'admin',
        'state': 'absent',
        'firewall_vip6': {
            'arp_reply': 'disable',
            'color': '4',
            'comment': 'Comment.',
            'extip': 'test_value_6',
            'extport': 'test_value_7',
            'http_cookie_age': '8',
            'http_cookie_domain': 'test_value_9',
            'http_cookie_domain_from_host': 'disable',
            'http_cookie_generation': '11',
            'http_cookie_path': 'test_value_12',
            'http_cookie_share': 'disable',
            'http_ip_header': 'enable',
            'http_ip_header_name': 'test_value_15',
            'http_multiplex': 'enable',
            'https_cookie_secure': 'disable',
            'id': '18',
            'ldb_method': 'static',
            'mappedip': 'test_value_20',
            'mappedport': 'test_value_21',
            'max_embryonic_connections': '22',
            'name': 'default_name_23',
            'outlook_web_access': 'disable',
            'persistence': 'none',
            'portforward': 'disable',
            'protocol': 'tcp',
            'server_type': 'http',
            'ssl_algorithm': 'high',
            'ssl_certificate': 'test_value_30',
            'ssl_client_fallback': 'disable',
            'ssl_client_renegotiation': 'allow',
            'ssl_client_session_state_max': '33',
            'ssl_client_session_state_timeout': '34',
            'ssl_client_session_state_type': 'disable',
            'ssl_dh_bits': '768',
            'ssl_hpkp': 'disable',
            'ssl_hpkp_age': '38',
            'ssl_hpkp_backup': 'test_value_39',
            'ssl_hpkp_include_subdomains': 'disable',
            'ssl_hpkp_primary': 'test_value_41',
            'ssl_hpkp_report_uri': 'test_value_42',
            'ssl_hsts': 'disable',
            'ssl_hsts_age': '44',
            'ssl_hsts_include_subdomains': 'disable',
            'ssl_http_location_conversion': 'enable',
            'ssl_http_match_host': 'enable',
            'ssl_max_version': 'ssl-3.0',
            'ssl_min_version': 'ssl-3.0',
            'ssl_mode': 'half',
            'ssl_pfs': 'require',
            'ssl_send_empty_frags': 'enable',
            'ssl_server_algorithm': 'high',
            'ssl_server_max_version': 'ssl-3.0',
            'ssl_server_min_version': 'ssl-3.0',
            'ssl_server_session_state_max': '56',
            'ssl_server_session_state_timeout': '57',
            'ssl_server_session_state_type': 'disable',
            'type': 'static-nat',
            'uuid': 'test_value_60',
            'weblogic_server': 'disable',
            'websphere_server': 'disable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_vip6.fortios_firewall(input_data, fos_instance)

    delete_method_mock.assert_called_with('firewall', 'vip6', mkey=ANY, vdom='root')
    schema_method_mock.assert_not_called()
    assert is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 500


def test_firewall_vip6_idempotent(mocker):
    schema_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'error', 'http_method': 'DELETE', 'http_status': 404}
    set_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_vip6': {
            'arp_reply': 'disable',
            'color': '4',
            'comment': 'Comment.',
            'extip': 'test_value_6',
            'extport': 'test_value_7',
            'http_cookie_age': '8',
            'http_cookie_domain': 'test_value_9',
            'http_cookie_domain_from_host': 'disable',
            'http_cookie_generation': '11',
            'http_cookie_path': 'test_value_12',
            'http_cookie_share': 'disable',
            'http_ip_header': 'enable',
            'http_ip_header_name': 'test_value_15',
            'http_multiplex': 'enable',
            'https_cookie_secure': 'disable',
            'id': '18',
            'ldb_method': 'static',
            'mappedip': 'test_value_20',
            'mappedport': 'test_value_21',
            'max_embryonic_connections': '22',
            'name': 'default_name_23',
            'outlook_web_access': 'disable',
            'persistence': 'none',
            'portforward': 'disable',
            'protocol': 'tcp',
            'server_type': 'http',
            'ssl_algorithm': 'high',
            'ssl_certificate': 'test_value_30',
            'ssl_client_fallback': 'disable',
            'ssl_client_renegotiation': 'allow',
            'ssl_client_session_state_max': '33',
            'ssl_client_session_state_timeout': '34',
            'ssl_client_session_state_type': 'disable',
            'ssl_dh_bits': '768',
            'ssl_hpkp': 'disable',
            'ssl_hpkp_age': '38',
            'ssl_hpkp_backup': 'test_value_39',
            'ssl_hpkp_include_subdomains': 'disable',
            'ssl_hpkp_primary': 'test_value_41',
            'ssl_hpkp_report_uri': 'test_value_42',
            'ssl_hsts': 'disable',
            'ssl_hsts_age': '44',
            'ssl_hsts_include_subdomains': 'disable',
            'ssl_http_location_conversion': 'enable',
            'ssl_http_match_host': 'enable',
            'ssl_max_version': 'ssl-3.0',
            'ssl_min_version': 'ssl-3.0',
            'ssl_mode': 'half',
            'ssl_pfs': 'require',
            'ssl_send_empty_frags': 'enable',
            'ssl_server_algorithm': 'high',
            'ssl_server_max_version': 'ssl-3.0',
            'ssl_server_min_version': 'ssl-3.0',
            'ssl_server_session_state_max': '56',
            'ssl_server_session_state_timeout': '57',
            'ssl_server_session_state_type': 'disable',
            'type': 'static-nat',
            'uuid': 'test_value_60',
            'weblogic_server': 'disable',
            'websphere_server': 'disable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_vip6.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'arp-reply': 'disable',
        'color': '4',
        'comment': 'Comment.',
        'extip': 'test_value_6',
        'extport': 'test_value_7',
        'http-cookie-age': '8',
        'http-cookie-domain': 'test_value_9',
        'http-cookie-domain-from-host': 'disable',
        'http-cookie-generation': '11',
        'http-cookie-path': 'test_value_12',
        'http-cookie-share': 'disable',
        'http-ip-header': 'enable',
        'http-ip-header-name': 'test_value_15',
        'http-multiplex': 'enable',
        'https-cookie-secure': 'disable',
        'id': '18',
        'ldb-method': 'static',
        'mappedip': 'test_value_20',
        'mappedport': 'test_value_21',
        'max-embryonic-connections': '22',
        'name': 'default_name_23',
                'outlook-web-access': 'disable',
                'persistence': 'none',
                'portforward': 'disable',
                'protocol': 'tcp',
                'server-type': 'http',
                'ssl-algorithm': 'high',
                'ssl-certificate': 'test_value_30',
                'ssl-client-fallback': 'disable',
                'ssl-client-renegotiation': 'allow',
                'ssl-client-session-state-max': '33',
                'ssl-client-session-state-timeout': '34',
                'ssl-client-session-state-type': 'disable',
                'ssl-dh-bits': '768',
                'ssl-hpkp': 'disable',
                'ssl-hpkp-age': '38',
                'ssl-hpkp-backup': 'test_value_39',
                'ssl-hpkp-include-subdomains': 'disable',
                'ssl-hpkp-primary': 'test_value_41',
                'ssl-hpkp-report-uri': 'test_value_42',
                'ssl-hsts': 'disable',
                'ssl-hsts-age': '44',
                'ssl-hsts-include-subdomains': 'disable',
                'ssl-http-location-conversion': 'enable',
                'ssl-http-match-host': 'enable',
                'ssl-max-version': 'ssl-3.0',
                'ssl-min-version': 'ssl-3.0',
                'ssl-mode': 'half',
                'ssl-pfs': 'require',
                'ssl-send-empty-frags': 'enable',
                'ssl-server-algorithm': 'high',
                'ssl-server-max-version': 'ssl-3.0',
                'ssl-server-min-version': 'ssl-3.0',
                'ssl-server-session-state-max': '56',
                'ssl-server-session-state-timeout': '57',
                'ssl-server-session-state-type': 'disable',
                'type': 'static-nat',
                'uuid': 'test_value_60',
                'weblogic-server': 'disable',
                'websphere-server': 'disable'
    }

    set_method_mock.assert_called_with('firewall', 'vip6', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 404


def test_firewall_vip6_filter_foreign_attributes(mocker):
    schema_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    set_method_mock = mocker.patch('quantum.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_vip6': {
            'random_attribute_not_valid': 'tag',
            'arp_reply': 'disable',
            'color': '4',
            'comment': 'Comment.',
            'extip': 'test_value_6',
            'extport': 'test_value_7',
            'http_cookie_age': '8',
            'http_cookie_domain': 'test_value_9',
            'http_cookie_domain_from_host': 'disable',
            'http_cookie_generation': '11',
            'http_cookie_path': 'test_value_12',
            'http_cookie_share': 'disable',
            'http_ip_header': 'enable',
            'http_ip_header_name': 'test_value_15',
            'http_multiplex': 'enable',
            'https_cookie_secure': 'disable',
            'id': '18',
            'ldb_method': 'static',
            'mappedip': 'test_value_20',
            'mappedport': 'test_value_21',
            'max_embryonic_connections': '22',
            'name': 'default_name_23',
            'outlook_web_access': 'disable',
            'persistence': 'none',
            'portforward': 'disable',
            'protocol': 'tcp',
            'server_type': 'http',
            'ssl_algorithm': 'high',
            'ssl_certificate': 'test_value_30',
            'ssl_client_fallback': 'disable',
            'ssl_client_renegotiation': 'allow',
            'ssl_client_session_state_max': '33',
            'ssl_client_session_state_timeout': '34',
            'ssl_client_session_state_type': 'disable',
            'ssl_dh_bits': '768',
            'ssl_hpkp': 'disable',
            'ssl_hpkp_age': '38',
            'ssl_hpkp_backup': 'test_value_39',
            'ssl_hpkp_include_subdomains': 'disable',
            'ssl_hpkp_primary': 'test_value_41',
            'ssl_hpkp_report_uri': 'test_value_42',
            'ssl_hsts': 'disable',
            'ssl_hsts_age': '44',
            'ssl_hsts_include_subdomains': 'disable',
            'ssl_http_location_conversion': 'enable',
            'ssl_http_match_host': 'enable',
            'ssl_max_version': 'ssl-3.0',
            'ssl_min_version': 'ssl-3.0',
            'ssl_mode': 'half',
            'ssl_pfs': 'require',
            'ssl_send_empty_frags': 'enable',
            'ssl_server_algorithm': 'high',
            'ssl_server_max_version': 'ssl-3.0',
            'ssl_server_min_version': 'ssl-3.0',
            'ssl_server_session_state_max': '56',
            'ssl_server_session_state_timeout': '57',
            'ssl_server_session_state_type': 'disable',
            'type': 'static-nat',
            'uuid': 'test_value_60',
            'weblogic_server': 'disable',
            'websphere_server': 'disable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_vip6.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'arp-reply': 'disable',
        'color': '4',
        'comment': 'Comment.',
        'extip': 'test_value_6',
        'extport': 'test_value_7',
        'http-cookie-age': '8',
        'http-cookie-domain': 'test_value_9',
        'http-cookie-domain-from-host': 'disable',
        'http-cookie-generation': '11',
        'http-cookie-path': 'test_value_12',
        'http-cookie-share': 'disable',
        'http-ip-header': 'enable',
        'http-ip-header-name': 'test_value_15',
        'http-multiplex': 'enable',
        'https-cookie-secure': 'disable',
        'id': '18',
        'ldb-method': 'static',
        'mappedip': 'test_value_20',
        'mappedport': 'test_value_21',
        'max-embryonic-connections': '22',
        'name': 'default_name_23',
                'outlook-web-access': 'disable',
                'persistence': 'none',
                'portforward': 'disable',
                'protocol': 'tcp',
                'server-type': 'http',
                'ssl-algorithm': 'high',
                'ssl-certificate': 'test_value_30',
                'ssl-client-fallback': 'disable',
                'ssl-client-renegotiation': 'allow',
                'ssl-client-session-state-max': '33',
                'ssl-client-session-state-timeout': '34',
                'ssl-client-session-state-type': 'disable',
                'ssl-dh-bits': '768',
                'ssl-hpkp': 'disable',
                'ssl-hpkp-age': '38',
                'ssl-hpkp-backup': 'test_value_39',
                'ssl-hpkp-include-subdomains': 'disable',
                'ssl-hpkp-primary': 'test_value_41',
                'ssl-hpkp-report-uri': 'test_value_42',
                'ssl-hsts': 'disable',
                'ssl-hsts-age': '44',
                'ssl-hsts-include-subdomains': 'disable',
                'ssl-http-location-conversion': 'enable',
                'ssl-http-match-host': 'enable',
                'ssl-max-version': 'ssl-3.0',
                'ssl-min-version': 'ssl-3.0',
                'ssl-mode': 'half',
                'ssl-pfs': 'require',
                'ssl-send-empty-frags': 'enable',
                'ssl-server-algorithm': 'high',
                'ssl-server-max-version': 'ssl-3.0',
                'ssl-server-min-version': 'ssl-3.0',
                'ssl-server-session-state-max': '56',
                'ssl-server-session-state-timeout': '57',
                'ssl-server-session-state-type': 'disable',
                'type': 'static-nat',
                'uuid': 'test_value_60',
                'weblogic-server': 'disable',
                'websphere-server': 'disable'
    }

    set_method_mock.assert_called_with('firewall', 'vip6', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200
