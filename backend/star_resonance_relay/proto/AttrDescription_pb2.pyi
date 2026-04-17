import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttrDescriptionBase(_message.Message):
    __slots__ = ("id", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    description: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class AttrDescriptionMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AttrDescriptionBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AttrDescriptionBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AttrDescriptionBase]
    def __init__(self, datas: _Optional[_Mapping[int, AttrDescriptionBase]] = ...) -> None: ...
