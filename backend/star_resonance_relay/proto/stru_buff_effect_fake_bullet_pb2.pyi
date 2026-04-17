import stru_vec3_pb2 as _stru_vec3_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectFakeBullet(_message.Message):
    __slots__ = ("buff_uuid", "event_id", "bullet_id", "buff_id", "bullet_offset")
    BUFF_UUID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    BULLET_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    BULLET_OFFSET_FIELD_NUMBER: _ClassVar[int]
    buff_uuid: int
    event_id: int
    bullet_id: int
    buff_id: int
    bullet_offset: _stru_vec3_pb2.Vec3
    def __init__(self, buff_uuid: _Optional[int] = ..., event_id: _Optional[int] = ..., bullet_id: _Optional[int] = ..., buff_id: _Optional[int] = ..., bullet_offset: _Optional[_Union[_stru_vec3_pb2.Vec3, _Mapping]] = ...) -> None: ...
