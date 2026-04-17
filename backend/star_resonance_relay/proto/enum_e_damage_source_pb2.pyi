from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDamageSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDamageSourceSkill: _ClassVar[EDamageSource]
    EDamageSourceBullet: _ClassVar[EDamageSource]
    EDamageSourceBuff: _ClassVar[EDamageSource]
    EDamageSourceFall: _ClassVar[EDamageSource]
    EDamageSourceFakeBullet: _ClassVar[EDamageSource]
    EDamageSourceOther: _ClassVar[EDamageSource]
EDamageSourceSkill: EDamageSource
EDamageSourceBullet: EDamageSource
EDamageSourceBuff: EDamageSource
EDamageSourceFall: EDamageSource
EDamageSourceFakeBullet: EDamageSource
EDamageSourceOther: EDamageSource
