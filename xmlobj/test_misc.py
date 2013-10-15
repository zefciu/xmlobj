"""Miscelanous tests."""

import unittest

from xmlobj import XmlObj
from xmlobj.attribute import Attribute

INITIAL_DATA = """<person>
    <name>Galahad</name>
    <nickname>The Pure</nickname>
    <age>31</age>
</person>"""

class TestCreate(unittest.TestCase):
    """Test creation from a dictionary."""

    def test_create(self):
        obj = XmlObj('person', {
            'name': 'Galahad',
            'nickname': 'The Pure',
            'age': '31',
        })
        self.assertEqual(obj['nickname'], 'The Pure')

class TestContext(unittest.TestCase):
    """Test the context management feature."""
    
    def setUp(self):
        """Create an object with test data."""
        self.obj = XmlObj.fromstring(INITIAL_DATA)

    def test_correct(self):
        """Test if changes are committed if *no* exception is raised"""

        with self.obj:
            self.obj['name'] = 'Bedevere'
            self.obj['nickname'] = 'The Wise'
            self.obj['age'] = '40'

        self.assertEqual(self.obj['name'], 'Bedevere')

    def test_incorrect(self):
        """Test if changes are rolled back if *an* exception is raised"""
        with self.assertRaises(ZeroDivisionError):
            with self.obj:
                self.obj['name'] = 'Bedevere'
                self.obj['nickname'] = 'The Wise'
                self.obj['age'] = str(1 / 0)

        self.assertEqual(self.obj['name'], 'Galahad')

class TestOrder(unittest.TestCase):
    """Test the ordering of attributes."""

    def setUp(self):
        """Create a test class with some attributes."""
        class Knight(XmlObj):
            name = Attribute()
            nickname = Attribute()
            age = Attribute()
            wisdom = Attribute()
            favourite_swallow = Attribute()
            squire = Attribute()
        self.Knight = Knight

    def test_order(self):
        """Test if attributes are ordered."""
        self.assertListEqual(self.Knight.attributes, [
            'name', 'nickname', 'age', 'wisdom', 'favourite_swallow', 'squire'
        ])

