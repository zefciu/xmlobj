"""Miscelanous tests."""

import unittest
from xmlobj import XmlObj

class TestCreate(unittest.TestCase):
    """Test creation from a dictionary."""

    def test_create(self):
        obj = XmlObj('person', {
            'name': 'Galahad',
            'nickname': 'The Pure',
            'age': '31',
        })
        self.assertEqual(obj['nickname'], 'The Pure')
