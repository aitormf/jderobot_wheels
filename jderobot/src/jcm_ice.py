# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.2
#
# <auto-generated>
#
# Generated from file `jcm.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module jderobot
_M_jderobot = Ice.openModule('jderobot')
__name__ = 'jderobot'

if 'FQExecutableName' not in _M_jderobot.__dict__:
    _M_jderobot.FQExecutableName = Ice.createTempClass()
    class FQExecutableName(object):
        def __init__(self, executable='', host=''):
            self.executable = executable
            self.host = host

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.executable)
            _h = 5 * _h + Ice.getHash(self.host)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.FQExecutableName):
                return NotImplemented
            else:
                if self.executable is None or other.executable is None:
                    if self.executable != other.executable:
                        return (-1 if self.executable is None else 1)
                else:
                    if self.executable < other.executable:
                        return -1
                    elif self.executable > other.executable:
                        return 1
                if self.host is None or other.host is None:
                    if self.host != other.host:
                        return (-1 if self.host is None else 1)
                else:
                    if self.host < other.host:
                        return -1
                    elif self.host > other.host:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_FQExecutableName)

        __repr__ = __str__

    _M_jderobot._t_FQExecutableName = IcePy.defineStruct('::jderobot::FQExecutableName', FQExecutableName, (), (
        ('executable', (), IcePy._t_string),
        ('host', (), IcePy._t_string)
    ))

    _M_jderobot.FQExecutableName = FQExecutableName
    del FQExecutableName

if 'FQComponentName' not in _M_jderobot.__dict__:
    _M_jderobot.FQComponentName = Ice.createTempClass()
    class FQComponentName(object):
        def __init__(self, platform='', component=''):
            self.platform = platform
            self.component = component

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.platform)
            _h = 5 * _h + Ice.getHash(self.component)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.FQComponentName):
                return NotImplemented
            else:
                if self.platform is None or other.platform is None:
                    if self.platform != other.platform:
                        return (-1 if self.platform is None else 1)
                else:
                    if self.platform < other.platform:
                        return -1
                    elif self.platform > other.platform:
                        return 1
                if self.component is None or other.component is None:
                    if self.component != other.component:
                        return (-1 if self.component is None else 1)
                else:
                    if self.component < other.component:
                        return -1
                    elif self.component > other.component:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_FQComponentName)

        __repr__ = __str__

    _M_jderobot._t_FQComponentName = IcePy.defineStruct('::jderobot::FQComponentName', FQComponentName, (), (
        ('platform', (), IcePy._t_string),
        ('component', (), IcePy._t_string)
    ))

    _M_jderobot.FQComponentName = FQComponentName
    del FQComponentName

if 'FQInterfaceName' not in _M_jderobot.__dict__:
    _M_jderobot.FQInterfaceName = Ice.createTempClass()
    class FQInterfaceName(object):
        def __init__(self, platform='', component='', iface=''):
            self.platform = platform
            self.component = component
            self.iface = iface

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.platform)
            _h = 5 * _h + Ice.getHash(self.component)
            _h = 5 * _h + Ice.getHash(self.iface)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.FQInterfaceName):
                return NotImplemented
            else:
                if self.platform is None or other.platform is None:
                    if self.platform != other.platform:
                        return (-1 if self.platform is None else 1)
                else:
                    if self.platform < other.platform:
                        return -1
                    elif self.platform > other.platform:
                        return 1
                if self.component is None or other.component is None:
                    if self.component != other.component:
                        return (-1 if self.component is None else 1)
                else:
                    if self.component < other.component:
                        return -1
                    elif self.component > other.component:
                        return 1
                if self.iface is None or other.iface is None:
                    if self.iface != other.iface:
                        return (-1 if self.iface is None else 1)
                else:
                    if self.iface < other.iface:
                        return -1
                    elif self.iface > other.iface:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_FQInterfaceName)

        __repr__ = __str__

    _M_jderobot._t_FQInterfaceName = IcePy.defineStruct('::jderobot::FQInterfaceName', FQInterfaceName, (), (
        ('platform', (), IcePy._t_string),
        ('component', (), IcePy._t_string),
        ('iface', (), IcePy._t_string)
    ))

    _M_jderobot.FQInterfaceName = FQInterfaceName
    del FQInterfaceName

if 'FQTopicName' not in _M_jderobot.__dict__:
    _M_jderobot.FQTopicName = Ice.createTempClass()
    class FQTopicName(object):
        def __init__(self, platform='', component='', iface='', topic=''):
            self.platform = platform
            self.component = component
            self.iface = iface
            self.topic = topic

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.platform)
            _h = 5 * _h + Ice.getHash(self.component)
            _h = 5 * _h + Ice.getHash(self.iface)
            _h = 5 * _h + Ice.getHash(self.topic)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.FQTopicName):
                return NotImplemented
            else:
                if self.platform is None or other.platform is None:
                    if self.platform != other.platform:
                        return (-1 if self.platform is None else 1)
                else:
                    if self.platform < other.platform:
                        return -1
                    elif self.platform > other.platform:
                        return 1
                if self.component is None or other.component is None:
                    if self.component != other.component:
                        return (-1 if self.component is None else 1)
                else:
                    if self.component < other.component:
                        return -1
                    elif self.component > other.component:
                        return 1
                if self.iface is None or other.iface is None:
                    if self.iface != other.iface:
                        return (-1 if self.iface is None else 1)
                else:
                    if self.iface < other.iface:
                        return -1
                    elif self.iface > other.iface:
                        return 1
                if self.topic is None or other.topic is None:
                    if self.topic != other.topic:
                        return (-1 if self.topic is None else 1)
                else:
                    if self.topic < other.topic:
                        return -1
                    elif self.topic > other.topic:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_FQTopicName)

        __repr__ = __str__

    _M_jderobot._t_FQTopicName = IcePy.defineStruct('::jderobot::FQTopicName', FQTopicName, (), (
        ('platform', (), IcePy._t_string),
        ('component', (), IcePy._t_string),
        ('iface', (), IcePy._t_string),
        ('topic', (), IcePy._t_string)
    ))

    _M_jderobot.FQTopicName = FQTopicName
    del FQTopicName

if 'ProvidedInterface' not in _M_jderobot.__dict__:
    _M_jderobot.ProvidedInterface = Ice.createTempClass()
    class ProvidedInterface(object):
        def __init__(self, name='', id=''):
            self.name = name
            self.id = id

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.id)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.ProvidedInterface):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.id is None or other.id is None:
                    if self.id != other.id:
                        return (-1 if self.id is None else 1)
                else:
                    if self.id < other.id:
                        return -1
                    elif self.id > other.id:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_ProvidedInterface)

        __repr__ = __str__

    _M_jderobot._t_ProvidedInterface = IcePy.defineStruct('::jderobot::ProvidedInterface', ProvidedInterface, (), (
        ('name', (), IcePy._t_string),
        ('id', (), IcePy._t_string)
    ))

    _M_jderobot.ProvidedInterface = ProvidedInterface
    del ProvidedInterface

if 'RequiredInterface' not in _M_jderobot.__dict__:
    _M_jderobot.RequiredInterface = Ice.createTempClass()
    class RequiredInterface(object):
        def __init__(self, name=Ice._struct_marker, id=''):
            if name is Ice._struct_marker:
                self.name = _M_jderobot.FQInterfaceName()
            else:
                self.name = name
            self.id = id

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.id)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.RequiredInterface):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.id is None or other.id is None:
                    if self.id != other.id:
                        return (-1 if self.id is None else 1)
                else:
                    if self.id < other.id:
                        return -1
                    elif self.id > other.id:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_RequiredInterface)

        __repr__ = __str__

    _M_jderobot._t_RequiredInterface = IcePy.defineStruct('::jderobot::RequiredInterface', RequiredInterface, (), (
        ('name', (), _M_jderobot._t_FQInterfaceName),
        ('id', (), IcePy._t_string)
    ))

    _M_jderobot.RequiredInterface = RequiredInterface
    del RequiredInterface

if '_t_ProvidesInterfaces' not in _M_jderobot.__dict__:
    _M_jderobot._t_ProvidesInterfaces = IcePy.defineSequence('::jderobot::ProvidesInterfaces', (), _M_jderobot._t_ProvidedInterface)

if '_t_RequiresInterfaces' not in _M_jderobot.__dict__:
    _M_jderobot._t_RequiresInterfaces = IcePy.defineSequence('::jderobot::RequiresInterfaces', (), _M_jderobot._t_RequiredInterface)

if 'ComponentData' not in _M_jderobot.__dict__:
    _M_jderobot.ComponentData = Ice.createTempClass()
    class ComponentData(object):
        def __init__(self, name=Ice._struct_marker, provides=None, requires=None):
            if name is Ice._struct_marker:
                self.name = _M_jderobot.FQComponentName()
            else:
                self.name = name
            self.provides = provides
            self.requires = requires

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            if self.provides:
                for _i0 in self.provides:
                    _h = 5 * _h + Ice.getHash(_i0)
            if self.requires:
                for _i1 in self.requires:
                    _h = 5 * _h + Ice.getHash(_i1)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.ComponentData):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.provides is None or other.provides is None:
                    if self.provides != other.provides:
                        return (-1 if self.provides is None else 1)
                else:
                    if self.provides < other.provides:
                        return -1
                    elif self.provides > other.provides:
                        return 1
                if self.requires is None or other.requires is None:
                    if self.requires != other.requires:
                        return (-1 if self.requires is None else 1)
                else:
                    if self.requires < other.requires:
                        return -1
                    elif self.requires > other.requires:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_ComponentData)

        __repr__ = __str__

    _M_jderobot._t_ComponentData = IcePy.defineStruct('::jderobot::ComponentData', ComponentData, (), (
        ('name', (), _M_jderobot._t_FQComponentName),
        ('provides', (), _M_jderobot._t_ProvidesInterfaces),
        ('requires', (), _M_jderobot._t_RequiresInterfaces)
    ))

    _M_jderobot.ComponentData = ComponentData
    del ComponentData

# End of module jderobot