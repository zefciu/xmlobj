"""Definition for XmlObj."""
import abc
from collections.abc import MutableMapping

from lxml import etree
from xmlobj.attribute import Attribute

class XmlObjMeta(abc.ABCMeta):
    """Metaclass for XmlObj. Performs binding o attributes."""

    def __init__(cls, clsname, bases, dict_):
        for k, v in dict_.items():
            if isinstance(v, Attribute):
                v.bind(k)
        super(XmlObjMeta, cls).__init__(clsname, bases, dict_)

class XmlObj(MutableMapping, metaclass=XmlObjMeta):
    """A dictionary-like object that stores it's values as XML."""

    def __init__(self, tagname, dict_):
        self._element = etree.Element(tagname)
        for k, v in dict_.items():
            self[k] = v
        super(XmlObj, self).__init__()

    @classmethod
    def fromstring(cls, s):
        """Create an xmlobj from a string."""
        self = cls.__new__(cls)
        self._element = etree.fromstring(s)
        return self

    def __getitem__(self, key):
        txt = self._element.xpath('{0}/text()'.format(key))
        if txt:
            return txt[0]
        raise KeyError('No such key')

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        element = etree.SubElement(self._element, key)
        element.text = value

    def __delitem__(self, key):
        element = self._element.xpath('{0}'.format(key))[0]
        self._element.remove(element)

    def __iter__(self):
        return (el.tag for el in self._element)

    def __len__(self):
        return len(self._element)
