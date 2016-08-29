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
# Generated from file `pose3d.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module jderobot
_M_jderobot = Ice.openModule('jderobot')
__name__ = 'jderobot'

if 'Time' not in _M_jderobot.__dict__:
    _M_jderobot.Time = Ice.createTempClass()
    class Time(object):
        def __init__(self, seconds=0, useconds=0):
            self.seconds = seconds
            self.useconds = useconds

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.seconds)
            _h = 5 * _h + Ice.getHash(self.useconds)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_jderobot.Time):
                return NotImplemented
            else:
                if self.seconds is None or other.seconds is None:
                    if self.seconds != other.seconds:
                        return (-1 if self.seconds is None else 1)
                else:
                    if self.seconds < other.seconds:
                        return -1
                    elif self.seconds > other.seconds:
                        return 1
                if self.useconds is None or other.useconds is None:
                    if self.useconds != other.useconds:
                        return (-1 if self.useconds is None else 1)
                else:
                    if self.useconds < other.useconds:
                        return -1
                    elif self.useconds > other.useconds:
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
            return IcePy.stringify(self, _M_jderobot._t_Time)

        __repr__ = __str__

    _M_jderobot._t_Time = IcePy.defineStruct('::jderobot::Time', Time, (), (
        ('seconds', (), IcePy._t_long),
        ('useconds', (), IcePy._t_long)
    ))

    _M_jderobot.Time = Time
    del Time

# End of module jderobot

# Start of module jderobot
__name__ = 'jderobot'

if 'JderobotException' not in _M_jderobot.__dict__:
    _M_jderobot.JderobotException = Ice.createTempClass()
    class JderobotException(Ice.UserException):
        def __init__(self, what=''):
            self.what = what

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::JderobotException'

    _M_jderobot._t_JderobotException = IcePy.defineException('::jderobot::JderobotException', JderobotException, (), False, None, (('what', (), IcePy._t_string, False, 0),))
    JderobotException._ice_type = _M_jderobot._t_JderobotException

    _M_jderobot.JderobotException = JderobotException
    del JderobotException

if 'ConfigurationNotExistException' not in _M_jderobot.__dict__:
    _M_jderobot.ConfigurationNotExistException = Ice.createTempClass()
    class ConfigurationNotExistException(_M_jderobot.JderobotException):
        def __init__(self, what=''):
            _M_jderobot.JderobotException.__init__(self, what)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::ConfigurationNotExistException'

    _M_jderobot._t_ConfigurationNotExistException = IcePy.defineException('::jderobot::ConfigurationNotExistException', ConfigurationNotExistException, (), False, _M_jderobot._t_JderobotException, ())
    ConfigurationNotExistException._ice_type = _M_jderobot._t_ConfigurationNotExistException

    _M_jderobot.ConfigurationNotExistException = ConfigurationNotExistException
    del ConfigurationNotExistException

if 'DataNotExistException' not in _M_jderobot.__dict__:
    _M_jderobot.DataNotExistException = Ice.createTempClass()
    class DataNotExistException(_M_jderobot.JderobotException):
        def __init__(self, what=''):
            _M_jderobot.JderobotException.__init__(self, what)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::DataNotExistException'

    _M_jderobot._t_DataNotExistException = IcePy.defineException('::jderobot::DataNotExistException', DataNotExistException, (), False, _M_jderobot._t_JderobotException, ())
    DataNotExistException._ice_type = _M_jderobot._t_DataNotExistException

    _M_jderobot.DataNotExistException = DataNotExistException
    del DataNotExistException

if 'HardwareFailedException' not in _M_jderobot.__dict__:
    _M_jderobot.HardwareFailedException = Ice.createTempClass()
    class HardwareFailedException(_M_jderobot.JderobotException):
        def __init__(self, what=''):
            _M_jderobot.JderobotException.__init__(self, what)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::HardwareFailedException'

    _M_jderobot._t_HardwareFailedException = IcePy.defineException('::jderobot::HardwareFailedException', HardwareFailedException, (), False, _M_jderobot._t_JderobotException, ())
    HardwareFailedException._ice_type = _M_jderobot._t_HardwareFailedException

    _M_jderobot.HardwareFailedException = HardwareFailedException
    del HardwareFailedException

if 'NoTopicException' not in _M_jderobot.__dict__:
    _M_jderobot.NoTopicException = Ice.createTempClass()
    class NoTopicException(_M_jderobot.JderobotException):
        def __init__(self, what=''):
            _M_jderobot.JderobotException.__init__(self, what)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::NoTopicException'

    _M_jderobot._t_NoTopicException = IcePy.defineException('::jderobot::NoTopicException', NoTopicException, (), False, _M_jderobot._t_JderobotException, ())
    NoTopicException._ice_type = _M_jderobot._t_NoTopicException

    _M_jderobot.NoTopicException = NoTopicException
    del NoTopicException

if 'SubscriptionFailedException' not in _M_jderobot.__dict__:
    _M_jderobot.SubscriptionFailedException = Ice.createTempClass()
    class SubscriptionFailedException(_M_jderobot.JderobotException):
        def __init__(self, what=''):
            _M_jderobot.JderobotException.__init__(self, what)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::SubscriptionFailedException'

    _M_jderobot._t_SubscriptionFailedException = IcePy.defineException('::jderobot::SubscriptionFailedException', SubscriptionFailedException, (), False, _M_jderobot._t_JderobotException, ())
    SubscriptionFailedException._ice_type = _M_jderobot._t_SubscriptionFailedException

    _M_jderobot.SubscriptionFailedException = SubscriptionFailedException
    del SubscriptionFailedException

if 'SubscriptionPushFailedException' not in _M_jderobot.__dict__:
    _M_jderobot.SubscriptionPushFailedException = Ice.createTempClass()
    class SubscriptionPushFailedException(_M_jderobot.JderobotException):
        def __init__(self, what=''):
            _M_jderobot.JderobotException.__init__(self, what)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'jderobot::SubscriptionPushFailedException'

    _M_jderobot._t_SubscriptionPushFailedException = IcePy.defineException('::jderobot::SubscriptionPushFailedException', SubscriptionPushFailedException, (), False, _M_jderobot._t_JderobotException, ())
    SubscriptionPushFailedException._ice_type = _M_jderobot._t_SubscriptionPushFailedException

    _M_jderobot.SubscriptionPushFailedException = SubscriptionPushFailedException
    del SubscriptionPushFailedException

# End of module jderobot

# Start of module jderobot
__name__ = 'jderobot'

if '_t_ByteSeq' not in _M_jderobot.__dict__:
    _M_jderobot._t_ByteSeq = IcePy.defineSequence('::jderobot::ByteSeq', (), IcePy._t_byte)

if '_t_IntSeq' not in _M_jderobot.__dict__:
    _M_jderobot._t_IntSeq = IcePy.defineSequence('::jderobot::IntSeq', (), IcePy._t_int)

if '_t_seqFloat' not in _M_jderobot.__dict__:
    _M_jderobot._t_seqFloat = IcePy.defineSequence('::jderobot::seqFloat', (), IcePy._t_float)

# End of module jderobot

# Start of module jderobot
__name__ = 'jderobot'

# End of module jderobot

# Start of module jderobot
__name__ = 'jderobot'

if 'Pose3DData' not in _M_jderobot.__dict__:
    _M_jderobot.Pose3DData = Ice.createTempClass()
    class Pose3DData(Ice.Object):
        """Pose3D data information"""
        def __init__(self, x=0.0, y=0.0, z=0.0, h=0.0, q0=0.0, q1=0.0, q2=0.0, q3=0.0):
            self.x = x
            self.y = y
            self.z = z
            self.h = h
            self.q0 = q0
            self.q1 = q1
            self.q2 = q2
            self.q3 = q3

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::Pose3DData')

        def ice_id(self, current=None):
            return '::jderobot::Pose3DData'

        def ice_staticId():
            return '::jderobot::Pose3DData'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_Pose3DData)

        __repr__ = __str__

    _M_jderobot.Pose3DDataPrx = Ice.createTempClass()
    class Pose3DDataPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.Pose3DDataPrx.ice_checkedCast(proxy, '::jderobot::Pose3DData', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.Pose3DDataPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::Pose3DData'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_Pose3DDataPrx = IcePy.defineProxy('::jderobot::Pose3DData', Pose3DDataPrx)

    _M_jderobot._t_Pose3DData = IcePy.defineClass('::jderobot::Pose3DData', Pose3DData, -1, (), False, False, None, (), (
        ('x', (), IcePy._t_float, False, 0),
        ('y', (), IcePy._t_float, False, 0),
        ('z', (), IcePy._t_float, False, 0),
        ('h', (), IcePy._t_float, False, 0),
        ('q0', (), IcePy._t_float, False, 0),
        ('q1', (), IcePy._t_float, False, 0),
        ('q2', (), IcePy._t_float, False, 0),
        ('q3', (), IcePy._t_float, False, 0)
    ))
    Pose3DData._ice_type = _M_jderobot._t_Pose3DData

    _M_jderobot.Pose3DData = Pose3DData
    del Pose3DData

    _M_jderobot.Pose3DDataPrx = Pose3DDataPrx
    del Pose3DDataPrx

if 'Pose3D' not in _M_jderobot.__dict__:
    _M_jderobot.Pose3D = Ice.createTempClass()
    class Pose3D(Ice.Object):
        """Interface to the Pose3D."""
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.Pose3D:
                raise RuntimeError('jderobot.Pose3D is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::Pose3D')

        def ice_id(self, current=None):
            return '::jderobot::Pose3D'

        def ice_staticId():
            return '::jderobot::Pose3D'
        ice_staticId = staticmethod(ice_staticId)

        def getPose3DData(self, current=None):
            pass

        def setPose3DData(self, data, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_Pose3D)

        __repr__ = __str__

    _M_jderobot.Pose3DPrx = Ice.createTempClass()
    class Pose3DPrx(Ice.ObjectPrx):

        def getPose3DData(self, _ctx=None):
            return _M_jderobot.Pose3D._op_getPose3DData.invoke(self, ((), _ctx))

        def begin_getPose3DData(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Pose3D._op_getPose3DData.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getPose3DData(self, _r):
            return _M_jderobot.Pose3D._op_getPose3DData.end(self, _r)

        def setPose3DData(self, data, _ctx=None):
            return _M_jderobot.Pose3D._op_setPose3DData.invoke(self, ((data, ), _ctx))

        def begin_setPose3DData(self, data, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Pose3D._op_setPose3DData.begin(self, ((data, ), _response, _ex, _sent, _ctx))

        def end_setPose3DData(self, _r):
            return _M_jderobot.Pose3D._op_setPose3DData.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.Pose3DPrx.ice_checkedCast(proxy, '::jderobot::Pose3D', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.Pose3DPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::Pose3D'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_Pose3DPrx = IcePy.defineProxy('::jderobot::Pose3D', Pose3DPrx)

    _M_jderobot._t_Pose3D = IcePy.defineClass('::jderobot::Pose3D', Pose3D, -1, (), True, False, None, (), ())
    Pose3D._ice_type = _M_jderobot._t_Pose3D

    Pose3D._op_getPose3DData = IcePy.Operation('getPose3DData', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_jderobot._t_Pose3DData, False, 0), ())
    Pose3D._op_setPose3DData = IcePy.Operation('setPose3DData', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_jderobot._t_Pose3DData, False, 0),), (), ((), IcePy._t_int, False, 0), ())

    _M_jderobot.Pose3D = Pose3D
    del Pose3D

    _M_jderobot.Pose3DPrx = Pose3DPrx
    del Pose3DPrx

# End of module jderobot
