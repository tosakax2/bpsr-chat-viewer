import stru_vec3_pb2 as _stru_vec3_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneInteractionInfo(_message.Message):
    __slots__ = ("obj_id", "pos_id", "pos")
    OBJ_ID_FIELD_NUMBER: _ClassVar[int]
    POS_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    obj_id: int
    pos_id: int
    pos: _stru_vec3_pb2.Vec3
    def __init__(self, obj_id: _Optional[int] = ..., pos_id: _Optional[int] = ..., pos: _Optional[_Union[_stru_vec3_pb2.Vec3, _Mapping]] = ...) -> None: ...
