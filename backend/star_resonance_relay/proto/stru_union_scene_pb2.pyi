import enum_union_enter_scene_pb2 as _enum_union_enter_scene_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionScene(_message.Message):
    __slots__ = ("union_id", "enter_type")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    enter_type: _enum_union_enter_scene_pb2.UnionEnterScene
    def __init__(self, union_id: _Optional[int] = ..., enter_type: _Optional[_Union[_enum_union_enter_scene_pb2.UnionEnterScene, str]] = ...) -> None: ...
