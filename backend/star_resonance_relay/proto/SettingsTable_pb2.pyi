import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettingsTableBase(_message.Message):
    __slots__ = ("id", "name", "system_id", "types_id", "operate_type", "describe_key", "des", "value", "data_storage", "link")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    TYPES_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIBE_KEY_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_STORAGE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    system_id: int
    types_id: int
    operate_type: int
    describe_key: str
    des: str
    value: str
    data_storage: int
    link: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., system_id: _Optional[int] = ..., types_id: _Optional[int] = ..., operate_type: _Optional[int] = ..., describe_key: _Optional[str] = ..., des: _Optional[str] = ..., value: _Optional[str] = ..., data_storage: _Optional[int] = ..., link: _Optional[str] = ...) -> None: ...

class SettingsTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SettingsTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SettingsTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SettingsTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SettingsTableBase]] = ...) -> None: ...
