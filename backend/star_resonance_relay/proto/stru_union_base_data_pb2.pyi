import stru_photo_graph_show_pb2 as _stru_photo_graph_show_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionBaseData(_message.Message):
    __slots__ = ("id", "icon", "name", "level", "num", "max_num", "tags", "declaration", "president_id", "online_num", "slogan", "cover_photo_info", "cover_photo_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DECLARATION_FIELD_NUMBER: _ClassVar[int]
    PRESIDENT_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_NUM_FIELD_NUMBER: _ClassVar[int]
    SLOGAN_FIELD_NUMBER: _ClassVar[int]
    COVER_PHOTO_INFO_FIELD_NUMBER: _ClassVar[int]
    COVER_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    icon: _containers.RepeatedScalarFieldContainer[int]
    name: str
    level: int
    num: int
    max_num: int
    tags: _containers.RepeatedScalarFieldContainer[int]
    declaration: str
    president_id: int
    online_num: int
    slogan: str
    cover_photo_info: _stru_photo_graph_show_pb2.PhotoGraphShow
    cover_photo_id: int
    def __init__(self, id: _Optional[int] = ..., icon: _Optional[_Iterable[int]] = ..., name: _Optional[str] = ..., level: _Optional[int] = ..., num: _Optional[int] = ..., max_num: _Optional[int] = ..., tags: _Optional[_Iterable[int]] = ..., declaration: _Optional[str] = ..., president_id: _Optional[int] = ..., online_num: _Optional[int] = ..., slogan: _Optional[str] = ..., cover_photo_info: _Optional[_Union[_stru_photo_graph_show_pb2.PhotoGraphShow, _Mapping]] = ..., cover_photo_id: _Optional[int] = ...) -> None: ...
