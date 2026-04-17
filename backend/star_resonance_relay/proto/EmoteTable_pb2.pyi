import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmoteTableBase(_message.Message):
    __slots__ = ("id", "face_data_id", "emote_type", "type", "is_loop", "icon", "is_show", "emote")
    ID_FIELD_NUMBER: _ClassVar[int]
    FACE_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    EMOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_FIELD_NUMBER: _ClassVar[int]
    EMOTE_FIELD_NUMBER: _ClassVar[int]
    id: int
    face_data_id: _table_basic_pb2.int_array
    emote_type: int
    type: int
    is_loop: bool
    icon: str
    is_show: str
    emote: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., face_data_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., emote_type: _Optional[int] = ..., type: _Optional[int] = ..., is_loop: bool = ..., icon: _Optional[str] = ..., is_show: _Optional[str] = ..., emote: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class EmoteTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EmoteTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EmoteTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EmoteTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EmoteTableBase]] = ...) -> None: ...
