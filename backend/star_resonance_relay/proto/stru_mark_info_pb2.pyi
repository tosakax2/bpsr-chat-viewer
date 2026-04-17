import stru_mark_position_pb2 as _stru_mark_position_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarkInfo(_message.Message):
    __slots__ = ("tag_id", "title", "content", "icon_id", "position", "map_layer_id")
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ICON_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    MAP_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    tag_id: int
    title: str
    content: str
    icon_id: int
    position: _stru_mark_position_pb2.MarkPosition
    map_layer_id: int
    def __init__(self, tag_id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., icon_id: _Optional[int] = ..., position: _Optional[_Union[_stru_mark_position_pb2.MarkPosition, _Mapping]] = ..., map_layer_id: _Optional[int] = ...) -> None: ...
