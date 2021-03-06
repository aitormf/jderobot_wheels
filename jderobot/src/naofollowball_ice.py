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
# Ice version 3.6.3
#
# <auto-generated>
#
# Generated from file `naofollowball.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
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

if 'NaoFollowBall' not in _M_jderobot.__dict__:
    _M_jderobot.NaoFollowBall = Ice.createTempClass()
    class NaoFollowBall(Ice.Object):
        """
        Interface to the Nao follow-ball
        """
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.NaoFollowBall:
                raise RuntimeError('jderobot.NaoFollowBall is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::NaoFollowBall')

        def ice_id(self, current=None):
            return '::jderobot::NaoFollowBall'

        def ice_staticId():
            return '::jderobot::NaoFollowBall'
        ice_staticId = staticmethod(ice_staticId)

        def setParams(self, rMin, rMax, gMin, gMax, bMin, bMax, current=None):
            pass

        def setMinParams(self, rMin, gMin, bMin, current=None):
            pass

        def setMaxParams(self, rMax, gMax, bMax, current=None):
            pass

        def start(self, current=None):
            pass

        def stop(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_NaoFollowBall)

        __repr__ = __str__

    _M_jderobot.NaoFollowBallPrx = Ice.createTempClass()
    class NaoFollowBallPrx(Ice.ObjectPrx):

        def setParams(self, rMin, rMax, gMin, gMax, bMin, bMax, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_setParams.invoke(self, ((rMin, rMax, gMin, gMax, bMin, bMax), _ctx))

        def begin_setParams(self, rMin, rMax, gMin, gMax, bMin, bMax, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_setParams.begin(self, ((rMin, rMax, gMin, gMax, bMin, bMax), _response, _ex, _sent, _ctx))

        def end_setParams(self, _r):
            return _M_jderobot.NaoFollowBall._op_setParams.end(self, _r)

        def setMinParams(self, rMin, gMin, bMin, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_setMinParams.invoke(self, ((rMin, gMin, bMin), _ctx))

        def begin_setMinParams(self, rMin, gMin, bMin, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_setMinParams.begin(self, ((rMin, gMin, bMin), _response, _ex, _sent, _ctx))

        def end_setMinParams(self, _r):
            return _M_jderobot.NaoFollowBall._op_setMinParams.end(self, _r)

        def setMaxParams(self, rMax, gMax, bMax, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_setMaxParams.invoke(self, ((rMax, gMax, bMax), _ctx))

        def begin_setMaxParams(self, rMax, gMax, bMax, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_setMaxParams.begin(self, ((rMax, gMax, bMax), _response, _ex, _sent, _ctx))

        def end_setMaxParams(self, _r):
            return _M_jderobot.NaoFollowBall._op_setMaxParams.end(self, _r)

        def start(self, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_start.invoke(self, ((), _ctx))

        def begin_start(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_start.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_start(self, _r):
            return _M_jderobot.NaoFollowBall._op_start.end(self, _r)

        def stop(self, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_stop.invoke(self, ((), _ctx))

        def begin_stop(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.NaoFollowBall._op_stop.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_stop(self, _r):
            return _M_jderobot.NaoFollowBall._op_stop.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.NaoFollowBallPrx.ice_checkedCast(proxy, '::jderobot::NaoFollowBall', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.NaoFollowBallPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::NaoFollowBall'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_NaoFollowBallPrx = IcePy.defineProxy('::jderobot::NaoFollowBall', NaoFollowBallPrx)

    _M_jderobot._t_NaoFollowBall = IcePy.defineClass('::jderobot::NaoFollowBall', NaoFollowBall, -1, (), True, False, None, (), ())
    NaoFollowBall._ice_type = _M_jderobot._t_NaoFollowBall

    NaoFollowBall._op_setParams = IcePy.Operation('setParams', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())
    NaoFollowBall._op_setMinParams = IcePy.Operation('setMinParams', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())
    NaoFollowBall._op_setMaxParams = IcePy.Operation('setMaxParams', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())
    NaoFollowBall._op_start = IcePy.Operation('start', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    NaoFollowBall._op_stop = IcePy.Operation('stop', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_jderobot.NaoFollowBall = NaoFollowBall
    del NaoFollowBall

    _M_jderobot.NaoFollowBallPrx = NaoFollowBallPrx
    del NaoFollowBallPrx

# End of module jderobot
