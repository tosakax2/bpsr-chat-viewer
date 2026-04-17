import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DialogueCameraTableBase(_message.Message):
    __slots__ = ("id", "comment", "template_ids", "aim_target_character", "aim_point")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    AIM_TARGET_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    AIM_POINT_FIELD_NUMBER: _ClassVar[int]
    id: int
    comment: str
    template_ids: _table_basic_pb2.int_array
    aim_target_character: int
    aim_point: str
    def __init__(self, id: _Optional[int] = ..., comment: _Optional[str] = ..., template_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., aim_target_character: _Optional[int] = ..., aim_point: _Optional[str] = ...) -> None: ...

class DialogueCameraTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DialogueCameraTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DialogueCameraTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, DialogueCameraTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, DialogueCameraTableBase]] = ...) -> None: ...
