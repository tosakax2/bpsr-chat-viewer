import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NpcEntityGlobalTableBase(_message.Message):
    __slots__ = ("u_id", "id", "position", "source_type")
    U_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    u_id: int
    id: int
    position: _table_basic_pb2.number_array
    source_type: int
    def __init__(self, u_id: _Optional[int] = ..., id: _Optional[int] = ..., position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., source_type: _Optional[int] = ...) -> None: ...

class NpcEntityGlobalTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NpcEntityGlobalTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NpcEntityGlobalTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, NpcEntityGlobalTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, NpcEntityGlobalTableBase]] = ...) -> None: ...
