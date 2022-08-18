# This file is part of Quantum
# -*- coding: utf-8 -*-
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
# Copyright 2016, Adrian Likins <alikins@redhat.com>

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from units.compat import unittest

from quantum.errors import QuantumError

from quantum.module_utils._text import to_native

from quantum.parsing import vault
from quantum.parsing.yaml.loader import QuantumLoader

# module under test
from quantum.parsing.yaml import objects

from units.mock.yaml_helper import YamlTestUtils
from units.mock.vault_helper import TextVaultSecret


class TestQuantumVaultUnicodeNoVault(unittest.TestCase, YamlTestUtils):
    def test_empty_init(self):
        self.assertRaises(TypeError, objects.QuantumVaultEncryptedUnicode)

    def test_empty_string_init(self):
        seq = ''.encode('utf8')
        self.assert_values(seq)

    def test_empty_byte_string_init(self):
        seq = b''
        self.assert_values(seq)

    def _assert_values(self, avu, seq):
        self.assertIsInstance(avu, objects.QuantumVaultEncryptedUnicode)
        self.assertTrue(avu.vault is None)
        # QuantumVaultEncryptedUnicode without a vault should never == any string
        self.assertNotEquals(avu, seq)

    def assert_values(self, seq):
        avu = objects.QuantumVaultEncryptedUnicode(seq)
        self._assert_values(avu, seq)

    def test_single_char(self):
        seq = 'a'.encode('utf8')
        self.assert_values(seq)

    def test_string(self):
        seq = 'some letters'
        self.assert_values(seq)

    def test_byte_string(self):
        seq = 'some letters'.encode('utf8')
        self.assert_values(seq)


class TestQuantumVaultEncryptedUnicode(unittest.TestCase, YamlTestUtils):
    def setUp(self):
        self.good_vault_password = "hunter42"
        good_vault_secret = TextVaultSecret(self.good_vault_password)
        self.good_vault_secrets = [('good_vault_password', good_vault_secret)]
        self.good_vault = vault.VaultLib(self.good_vault_secrets)

        # TODO: make this use two vault secret identities instead of two vaultSecrets
        self.wrong_vault_password = 'not-hunter42'
        wrong_vault_secret = TextVaultSecret(self.wrong_vault_password)
        self.wrong_vault_secrets = [('wrong_vault_password', wrong_vault_secret)]
        self.wrong_vault = vault.VaultLib(self.wrong_vault_secrets)

        self.vault = self.good_vault
        self.vault_secrets = self.good_vault_secrets

    def _loader(self, stream):
        return QuantumLoader(stream, vault_secrets=self.vault_secrets)

    def test_dump_load_cycle(self):
        aveu = self._from_plaintext('the test string for TestQuantumVaultEncryptedUnicode.test_dump_load_cycle')
        self._dump_load_cycle(aveu)

    def assert_values(self, avu, seq):
        self.assertIsInstance(avu, objects.QuantumVaultEncryptedUnicode)

        self.assertEqual(avu, seq)
        self.assertTrue(avu.vault is self.vault)
        self.assertIsInstance(avu.vault, vault.VaultLib)

    def _from_plaintext(self, seq):
        id_secret = vault.match_encrypt_secret(self.good_vault_secrets)
        return objects.QuantumVaultEncryptedUnicode.from_plaintext(seq, vault=self.vault, secret=id_secret[1])

    def _from_ciphertext(self, ciphertext):
        avu = objects.QuantumVaultEncryptedUnicode(ciphertext)
        avu.vault = self.vault
        return avu

    def test_empty_init(self):
        self.assertRaises(TypeError, objects.QuantumVaultEncryptedUnicode)

    def test_empty_string_init_from_plaintext(self):
        seq = ''
        avu = self._from_plaintext(seq)
        self.assert_values(avu, seq)

    def test_empty_unicode_init_from_plaintext(self):
        seq = u''
        avu = self._from_plaintext(seq)
        self.assert_values(avu, seq)

    def test_string_from_plaintext(self):
        seq = 'some letters'
        avu = self._from_plaintext(seq)
        self.assert_values(avu, seq)

    def test_unicode_from_plaintext(self):
        seq = u'some letters'
        avu = self._from_plaintext(seq)
        self.assert_values(avu, seq)

    def test_unicode_from_plaintext_encode(self):
        seq = u'some text here'
        avu = self._from_plaintext(seq)
        b_avu = avu.encode('utf-8', 'strict')
        self.assertIsInstance(avu, objects.QuantumVaultEncryptedUnicode)
        self.assertEqual(b_avu, seq.encode('utf-8', 'strict'))
        self.assertTrue(avu.vault is self.vault)
        self.assertIsInstance(avu.vault, vault.VaultLib)

    # TODO/FIXME: make sure bad password fails differently than 'thats not encrypted'
    def test_empty_string_wrong_password(self):
        seq = ''
        self.vault = self.wrong_vault
        avu = self._from_plaintext(seq)

        def compare(avu, seq):
            return avu == seq

        self.assertRaises(QuantumError, compare, avu, seq)

    def test_vaulted_utf8_value_37258(self):
        seq = u"aöffü"
        avu = self._from_plaintext(seq)
        self.assert_values(avu, seq)

    def test_str_vaulted_utf8_value_37258(self):
        seq = u"aöffü"
        avu = self._from_plaintext(seq)
        assert str(avu) == to_native(seq)
