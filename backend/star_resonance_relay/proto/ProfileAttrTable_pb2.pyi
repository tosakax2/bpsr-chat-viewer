import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileAttrTableBase(_message.Message):
    __slots__ = ("id", "attr_id", "name", "type", "type_display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    attr_id: int
    name: _table_basic_pb2.mlstring
    type: int
    type_display_name: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., attr_id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., type: _Optional[int] = ..., type_display_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class ProfileAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfileAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfileAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfileAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfileAttrTableBase]] = ...) -> None: ...
