# Copyright (c) 2017-2019 Fumito Hamamura <fumito.ham@gmail.com>

# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation version 3.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see <http://www.gnu.org/licenses/>.

import sys
import re
import keyword
import importlib
import types
from inspect import getmro


class AutoNamer:
    def __init__(self, basename):

        self.__basename = basename
        self.__last_postfix = 0

    def get_next(self, existing_names, prefix=""):

        self.__last_postfix += 1
        result = prefix + self.__basename + str(self.__last_postfix)

        if result in existing_names:
            # Increment postfix until no name
            # exists with that postfix.
            return self.get_next(existing_names, prefix)
        else:
            return result

    def revert(self):
        self.__last_postfix -= self.__last_postfix and 1

    def reset(self):
        self.__last_postfix = 0


_system_defined_names = re.compile(r"^_.*")


def is_valid_name(word):

    if not isinstance(word, str):
        return False

    if word.isidentifier() and not keyword.iskeyword(word):
        check = _system_defined_names.match(word)
        if not check:  # _system_defined_names.match(word):
            return True

    return False


def get_state_attrs(obj):

    mro = list(reversed(getmro(type(obj))))
    mro.remove(object)
    attrs = {}
    for cls in mro:
        cls_attrs = {}
        for attr in cls.state_attrs:
            cls_attrs[attr] = getattr(obj, attr)

        attrs.update(cls_attrs)

    return attrs


def get_module(module):

    if isinstance(module, types.ModuleType):
        pass

    elif isinstance(module, str):
        if module not in sys.modules:
            importlib.import_module(module)

        module = sys.modules[module]

    else:
        raise TypeError("%s is not a module or string." % module)

    return module


def get_param_func(param_names):

    if param_names:
        sig = "=None, ".join(param_names) + "=None"
    else:
        sig = ""

    return "def _param_func(" + sig + "): pass"
