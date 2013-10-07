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
        self.obj = XmlObj()
        self.obj._element = etree.fromstring(INITIAL_DATA)

    def test_getitem(self):
        """Test if an item is correctly retrieved."""
        self.assertEqual(self.obj['name'], 'Galahad')
