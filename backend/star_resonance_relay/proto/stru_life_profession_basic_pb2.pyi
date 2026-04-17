import stru_lift_profession_specialization_pb2 as _stru_lift_profession_specialization_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionBasic(_message.Message):
    __slots__ = ("id", "level", "exp", "specialization", "current_specialization_point")
    class SpecializationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_lift_profession_specialization_pb2.LiftProfessionSpecialization
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_lift_profession_specialization_pb2.LiftProfessionSpecialization, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    SPECIALIZATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SPECIALIZATION_POINT_FIELD_NUMBER: _ClassVar[int]
    id: int
    level: int
    exp: int
    specialization: _containers.MessageMap[int, _stru_lift_profession_specialization_pb2.LiftProfessionSpecialization]
    current_specialization_point: int
    def __init__(self, id: _Optional[int] = ..., level: _Optional[int] = ..., exp: _Optional[int] = ..., specialization: _Optional[_Mapping[int, _stru_lift_profession_specialization_pb2.LiftProfessionSpecialization]] = ..., current_specialization_point: _Optional[int] = ...) -> None: ...
