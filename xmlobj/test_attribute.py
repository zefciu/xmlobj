"""Tests for attribute access."""

import unittest
from lxml import etree

from xmlobj import XmlObj
from xmlobj.attribute import Attribute

INITIAL_DATA = """<person type="user">
    <name>Galahad</name>
    <nickname>The Pure</nickname>
    <age>31</age>
</person>"""

class TestAttribute(unittest.TestCase):
    """Test the attribute access of xmlobj."""

    def setUp(self):
        """Create an object with test data."""

        class Person(XmlObj):
            """A person."""
            type = Attribute()
            source = Attribute()

        self.obj = Person.fromstring(INITIAL_DATA)

    def test_getattr(self):
        """Test the getattribute behaviour."""
        self.assertEqual(self.obj.type, 'user')

    def test_setattr(self):
        """Test the setattribute behaviour."""
        self.obj.source = 'LDAP'
        self.assertEqual(self.obj.source, 'LDAP')
        self.assertIn(b'source="LDAP"', etree.tostring(self.obj._element))

    def test_delattr(self):
        """Test the delattribute behaviour."""
        del self.obj.type
        with self.assertRaises(AttributeError):
            self.obj.type
