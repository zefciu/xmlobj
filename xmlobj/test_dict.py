"""Tests for dict-like behaviour of XmlObj."""

import unittest
from lxml import etree

from xmlobj import XmlObj

INITIAL_DATA = """<person>
    <name>Galahad</name>
    <nickname>The Pure</nickname>
    <age>31</age>
</person>"""

class TestDict(unittest.TestCase):
    """Test suite for dict-like behaviour."""

    def setUp(self):
        """Create an object with test data."""
        self.obj = XmlObj.fromstring(INITIAL_DATA)

    def test_getitem(self):
        """Test if an item is correctly retrieved."""
        self.assertEqual(self.obj['name'], 'Galahad')

    def test_len(self):
        """Test if the length of object is correct."""
        self.assertEqual(len(self.obj), 3)

    def test_iter(self):
        """Test if the length of object is correct."""
        self.assertListEqual(list(self.obj), ['name', 'nickname', 'age'])

    def test_setitem(self):
        """Test if the setting of an item works correctly."""
        self.obj['city'] = 'Poznań'
        self.assertEqual(len(self.obj), 4)
        self.assertEqual(self.obj['city'], 'Poznań')
        self.assertListEqual(
            list(self.obj), ['name', 'nickname', 'age', 'city'])
