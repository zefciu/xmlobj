class Attribute(object):
    """A string attribute of xmlobj."""

    def bind(self, name):
        """Set the attribute name."""
        self._name = name

    def __get__(self, inst, cls):
        return inst._element.attrib[self._name]
