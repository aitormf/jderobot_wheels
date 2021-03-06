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
# Generated from file `varcolor.ice'
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

if 'ImageDescription' not in _M_jderobot.__dict__:
    _M_jderobot.ImageDescription = Ice.createTempClass()
    class ImageDescription(Ice.Object):
        """
        Static description of the image source.
        Members:
        width -- < %Image width [pixels]
        height -- < %Image height [pixels]
        size -- < %Image size [bytes]
        format -- < %Image format string
        md5sum -- 
        """
        def __init__(self, width=0, height=0, size=0, format='', md5sum=''):
            self.width = width
            self.height = height
            self.size = size
            self.format = format
            self.md5sum = md5sum

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::ImageDescription')

        def ice_id(self, current=None):
            return '::jderobot::ImageDescription'

        def ice_staticId():
            return '::jderobot::ImageDescription'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_ImageDescription)

        __repr__ = __str__

    _M_jderobot.ImageDescriptionPrx = Ice.createTempClass()
    class ImageDescriptionPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.ImageDescriptionPrx.ice_checkedCast(proxy, '::jderobot::ImageDescription', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.ImageDescriptionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::ImageDescription'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_ImageDescriptionPrx = IcePy.defineProxy('::jderobot::ImageDescription', ImageDescriptionPrx)

    _M_jderobot._t_ImageDescription = IcePy.defineClass('::jderobot::ImageDescription', ImageDescription, -1, (), False, False, None, (), (
        ('width', (), IcePy._t_int, False, 0),
        ('height', (), IcePy._t_int, False, 0),
        ('size', (), IcePy._t_int, False, 0),
        ('format', (), IcePy._t_string, False, 0),
        ('md5sum', (), IcePy._t_string, False, 0)
    ))
    ImageDescription._ice_type = _M_jderobot._t_ImageDescription

    _M_jderobot.ImageDescription = ImageDescription
    del ImageDescription

    _M_jderobot.ImageDescriptionPrx = ImageDescriptionPrx
    del ImageDescriptionPrx

if 'ImageData' not in _M_jderobot.__dict__:
    _M_jderobot.ImageData = Ice.createTempClass()
    class ImageData(Ice.Object):
        """
        A single image served as a sequence of bytes
        Members:
        timeStamp -- < TimeStamp of Data
        description -- < ImageDescription of Data, for convienence purposes
        pixelData -- < The image data itself. The structure of this byte sequence depends on the image format and compression.
        """
        def __init__(self, timeStamp=Ice._struct_marker, description=None, pixelData=None):
            if timeStamp is Ice._struct_marker:
                self.timeStamp = _M_jderobot.Time()
            else:
                self.timeStamp = timeStamp
            self.description = description
            self.pixelData = pixelData

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::ImageData')

        def ice_id(self, current=None):
            return '::jderobot::ImageData'

        def ice_staticId():
            return '::jderobot::ImageData'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_ImageData)

        __repr__ = __str__

    _M_jderobot.ImageDataPrx = Ice.createTempClass()
    class ImageDataPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.ImageDataPrx.ice_checkedCast(proxy, '::jderobot::ImageData', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.ImageDataPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::ImageData'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_ImageDataPrx = IcePy.defineProxy('::jderobot::ImageData', ImageDataPrx)

    _M_jderobot._t_ImageData = IcePy.declareClass('::jderobot::ImageData')

    _M_jderobot._t_ImageData = IcePy.defineClass('::jderobot::ImageData', ImageData, -1, (), False, False, None, (), (
        ('timeStamp', (), _M_jderobot._t_Time, False, 0),
        ('description', (), _M_jderobot._t_ImageDescription, False, 0),
        ('pixelData', (), _M_jderobot._t_ByteSeq, False, 0)
    ))
    ImageData._ice_type = _M_jderobot._t_ImageData

    _M_jderobot.ImageData = ImageData
    del ImageData

    _M_jderobot.ImageDataPrx = ImageDataPrx
    del ImageDataPrx

if 'ImageConsumer' not in _M_jderobot.__dict__:
    _M_jderobot.ImageConsumer = Ice.createTempClass()
    class ImageConsumer(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.ImageConsumer:
                raise RuntimeError('jderobot.ImageConsumer is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::ImageConsumer')

        def ice_id(self, current=None):
            return '::jderobot::ImageConsumer'

        def ice_staticId():
            return '::jderobot::ImageConsumer'
        ice_staticId = staticmethod(ice_staticId)

        def report(self, obj, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_ImageConsumer)

        __repr__ = __str__

    _M_jderobot.ImageConsumerPrx = Ice.createTempClass()
    class ImageConsumerPrx(Ice.ObjectPrx):

        def report(self, obj, _ctx=None):
            return _M_jderobot.ImageConsumer._op_report.invoke(self, ((obj, ), _ctx))

        def begin_report(self, obj, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.ImageConsumer._op_report.begin(self, ((obj, ), _response, _ex, _sent, _ctx))

        def end_report(self, _r):
            return _M_jderobot.ImageConsumer._op_report.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.ImageConsumerPrx.ice_checkedCast(proxy, '::jderobot::ImageConsumer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.ImageConsumerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::ImageConsumer'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_ImageConsumerPrx = IcePy.defineProxy('::jderobot::ImageConsumer', ImageConsumerPrx)

    _M_jderobot._t_ImageConsumer = IcePy.defineClass('::jderobot::ImageConsumer', ImageConsumer, -1, (), True, False, None, (), ())
    ImageConsumer._ice_type = _M_jderobot._t_ImageConsumer

    ImageConsumer._op_report = IcePy.Operation('report', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_jderobot._t_ImageData, False, 0),), (), None, ())

    _M_jderobot.ImageConsumer = ImageConsumer
    del ImageConsumer

    _M_jderobot.ImageConsumerPrx = ImageConsumerPrx
    del ImageConsumerPrx

if '_t_ImageFormat' not in _M_jderobot.__dict__:
    _M_jderobot._t_ImageFormat = IcePy.defineSequence('::jderobot::ImageFormat', (), IcePy._t_string)

if 'ImageProvider' not in _M_jderobot.__dict__:
    _M_jderobot.ImageProvider = Ice.createTempClass()
    class ImageProvider(Ice.Object):
        """
        Interface to the image provider.
        """
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.ImageProvider:
                raise RuntimeError('jderobot.ImageProvider is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::ImageProvider')

        def ice_id(self, current=None):
            return '::jderobot::ImageProvider'

        def ice_staticId():
            return '::jderobot::ImageProvider'
        ice_staticId = staticmethod(ice_staticId)

        def getImageDescription(self, current=None):
            """
            Returns the image source description.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def getImageFormat(self, current=None):
            pass

        def getImageData_async(self, _cb, format, current=None):
            """
            Returns the latest data.
            Arguments:
            _cb -- The asynchronous callback object.
            format -- 
            current -- The Current object for the invocation.
            """
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_ImageProvider)

        __repr__ = __str__

    _M_jderobot.ImageProviderPrx = Ice.createTempClass()
    class ImageProviderPrx(Ice.ObjectPrx):

        """
        Returns the image source description.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def getImageDescription(self, _ctx=None):
            return _M_jderobot.ImageProvider._op_getImageDescription.invoke(self, ((), _ctx))

        """
        Returns the image source description.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getImageDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.ImageProvider._op_getImageDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Returns the image source description.
        Arguments:
        """
        def end_getImageDescription(self, _r):
            return _M_jderobot.ImageProvider._op_getImageDescription.end(self, _r)

        def getImageFormat(self, _ctx=None):
            return _M_jderobot.ImageProvider._op_getImageFormat.invoke(self, ((), _ctx))

        def begin_getImageFormat(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.ImageProvider._op_getImageFormat.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getImageFormat(self, _r):
            return _M_jderobot.ImageProvider._op_getImageFormat.end(self, _r)

        """
        Returns the latest data.
        Arguments:
        format -- 
        _ctx -- The request context for the invocation.
        """
        def getImageData(self, format, _ctx=None):
            return _M_jderobot.ImageProvider._op_getImageData.invoke(self, ((format, ), _ctx))

        """
        Returns the latest data.
        Arguments:
        format -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getImageData(self, format, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.ImageProvider._op_getImageData.begin(self, ((format, ), _response, _ex, _sent, _ctx))

        """
        Returns the latest data.
        Arguments:
        format -- 
        """
        def end_getImageData(self, _r):
            return _M_jderobot.ImageProvider._op_getImageData.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.ImageProviderPrx.ice_checkedCast(proxy, '::jderobot::ImageProvider', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.ImageProviderPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::ImageProvider'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_ImageProviderPrx = IcePy.defineProxy('::jderobot::ImageProvider', ImageProviderPrx)

    _M_jderobot._t_ImageProvider = IcePy.defineClass('::jderobot::ImageProvider', ImageProvider, -1, (), True, False, None, (), ())
    ImageProvider._ice_type = _M_jderobot._t_ImageProvider

    ImageProvider._op_getImageDescription = IcePy.Operation('getImageDescription', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_jderobot._t_ImageDescription, False, 0), ())
    ImageProvider._op_getImageFormat = IcePy.Operation('getImageFormat', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_jderobot._t_ImageFormat, False, 0), ())
    ImageProvider._op_getImageData = IcePy.Operation('getImageData', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_jderobot._t_ImageData, False, 0), (_M_jderobot._t_DataNotExistException, _M_jderobot._t_HardwareFailedException))

    _M_jderobot.ImageProvider = ImageProvider
    del ImageProvider

    _M_jderobot.ImageProviderPrx = ImageProviderPrx
    del ImageProviderPrx

# End of module jderobot

# Start of module jderobot
__name__ = 'jderobot'

if 'VarColor' not in _M_jderobot.__dict__:
    _M_jderobot.VarColor = Ice.createTempClass()
    class VarColor(Ice.Object):
        """
        Interface to the image provider.
        """
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.VarColor:
                raise RuntimeError('jderobot.VarColor is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::VarColor')

        def ice_id(self, current=None):
            return '::jderobot::VarColor'

        def ice_staticId():
            return '::jderobot::VarColor'
        ice_staticId = staticmethod(ice_staticId)

        def getDescription(self, current=None):
            """
            Returns the image source description.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def getData_async(self, _cb, current=None):
            """
            Returns the latest data.
            Arguments:
            _cb -- The asynchronous callback object.
            current -- The Current object for the invocation.
            """
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_VarColor)

        __repr__ = __str__

    _M_jderobot.VarColorPrx = Ice.createTempClass()
    class VarColorPrx(Ice.ObjectPrx):

        """
        Returns the image source description.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def getDescription(self, _ctx=None):
            return _M_jderobot.VarColor._op_getDescription.invoke(self, ((), _ctx))

        """
        Returns the image source description.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.VarColor._op_getDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Returns the image source description.
        Arguments:
        """
        def end_getDescription(self, _r):
            return _M_jderobot.VarColor._op_getDescription.end(self, _r)

        """
        Returns the latest data.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def getData(self, _ctx=None):
            return _M_jderobot.VarColor._op_getData.invoke(self, ((), _ctx))

        """
        Returns the latest data.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getData(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.VarColor._op_getData.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Returns the latest data.
        Arguments:
        """
        def end_getData(self, _r):
            return _M_jderobot.VarColor._op_getData.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.VarColorPrx.ice_checkedCast(proxy, '::jderobot::VarColor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.VarColorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::VarColor'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_VarColorPrx = IcePy.defineProxy('::jderobot::VarColor', VarColorPrx)

    _M_jderobot._t_VarColor = IcePy.defineClass('::jderobot::VarColor', VarColor, -1, (), True, False, None, (), ())
    VarColor._ice_type = _M_jderobot._t_VarColor

    VarColor._op_getDescription = IcePy.Operation('getDescription', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_jderobot._t_ImageDescription, False, 0), ())
    VarColor._op_getData = IcePy.Operation('getData', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (), (), ((), _M_jderobot._t_ImageData, False, 0), (_M_jderobot._t_DataNotExistException, _M_jderobot._t_HardwareFailedException))

    _M_jderobot.VarColor = VarColor
    del VarColor

    _M_jderobot.VarColorPrx = VarColorPrx
    del VarColorPrx

# End of module jderobot
