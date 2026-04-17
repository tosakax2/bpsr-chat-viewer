import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BdTagTableBase(_message.Message):
    __slots__ = ("id", "tag_name", "tag_string", "tag_type", "parent_tag")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_STRING_FIELD_NUMBER: _ClassVar[int]
    TAG_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_TAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    tag_name: _table_basic_pb2.mlstring
    tag_string: _table_basic_pb2.mlstring
    tag_type: int
    parent_tag: int
    def __init__(self, id: _Optional[int] = ..., tag_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., tag_string: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., tag_type: _Optional[int] = ..., parent_tag: _Optional[int] = ...) -> None: ...

class BdTagTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BdTagTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BdTagTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BdTagTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BdTagTableBase]] = ...) -> None: ...
