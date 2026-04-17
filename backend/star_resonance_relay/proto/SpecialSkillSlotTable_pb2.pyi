import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpecialSkillSlotTableBase(_message.Message):
    __slots__ = ("id", "tag_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    tag_ids: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., tag_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class SpecialSkillSlotTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SpecialSkillSlotTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SpecialSkillSlotTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SpecialSkillSlotTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SpecialSkillSlotTableBase]] = ...) -> None: ...
