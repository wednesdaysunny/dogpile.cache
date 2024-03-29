import sys


py2k = sys.version_info < (3, 0)
py3k = sys.version_info >= (3, 0)
py32 = sys.version_info >= (3, 2)
jython = sys.platform.startswith('java')


try:
    import threading
except ImportError:
    import dummy_threading as threading


if py3k: # pragma: no cover
    string_types = str,
    text_type = str
    string_type = str

    if py32:
        callable = callable
    else:
        def callable(fn):
            return hasattr(fn, '__call__')

    def u(s):
        return s

    def ue(s):
        return s

    import configparser
    import io
    import _thread as thread
else:
    string_types = basestring,
    text_type = unicode
    string_type = str

    def u(s):
        return unicode(s, "utf-8")

    def ue(s):
        return unicode(s, "unicode_escape")

    import ConfigParser as configparser
    import StringIO as io


    callable = callable
    import thread


if py3k or jython:
    import pickle
else:
    import cPickle as pickle