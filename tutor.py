"""Multilevel interactive tutorial for using Pdb.
"""
import pdb


class Tdb(pdb.Pdb):
    """Bunch of functions to debug with hints."""

    def _inner(self, a, b):
        if a > b:
            return a - b
        if a < b:
            return b - a
        else:
            return a + b

    def debug_me(self):
        Tdb().set_trace()
        a = 1
        b = 2
        a = 2
        c = self._inner(a, b)
        c = self._inner(b, a)
        return c


if __name__ == '__main__':
    Tdb().debug_me()
