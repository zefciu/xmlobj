"""Definition for XmlObj."""
from collections.abc import Mapping

class XmlObj(Mapping):
    """A dictionary-like object that stores it's values as XML."""

    def __getitem__(self, key):
        txt = self._element.xpath('{0}/text()'.format(key))
        if txt:
            return txt[0]
        raise KeyError('No such key')

    def __iter__(self):
        return (el.tag for el in self._element)

    def __len__(self):
        return len(self._element)
