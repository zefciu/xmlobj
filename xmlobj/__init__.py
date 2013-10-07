"""Definition for XmlObj."""

class XmlObj(object):
    """A dictionary-like object that stores it's values as XML."""

    def __getitem__(self, key):
        txt = self._element.xpath('{0}/text()'.format(key))
        if txt:
            return txt[0]
        raise KeyError('No such key')
