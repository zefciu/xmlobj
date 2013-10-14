class Attribute(object):
    """A string attribute of xmlobj."""

    def bind(self, name):
        """Set the attribute name."""
        self._name = name

    def __get__(self, inst, cls):
        try:
            return inst._element.attrib[self._name]
        except KeyError:
            raise AttributeError('No such attribute!')

    def __set__(self, inst, value):
        inst._element.attrib[self._name] = value

    def __delete__(self, inst):
        del inst._element.attrib[self._name]
