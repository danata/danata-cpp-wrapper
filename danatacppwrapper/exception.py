# -*- coding: utf-8 -*-
"""
**********
Exceptions
**********

Base exceptions and errors for danata-cpp-wrapper.

"""
__author__ = """Youngsung Kim (grnydawn@gmail.com)"""
#    Copyright (C) 2016 by
#    Youngsung Kim <grnydawn@gmail.com>
#    All rights reserved.
#

# Exception handling

# the root of all Exceptions
class DNTCppWrapperException(Exception):
    """Base class for exceptions in danata-cpp-wrapper."""

class DNTCppWrapperError(DNTCppWrapperException):
    """Exception for a serious error in danata-cpp-wrapper"""
