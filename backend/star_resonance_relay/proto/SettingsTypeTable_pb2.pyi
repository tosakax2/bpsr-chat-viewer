from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettingsTypeTableBase(_message.Message):
    __slots__ = ("types_id", "system_id", "name", "sort")
    TYPES_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    types_id: int
    system_id: int
    name: str
    sort: int
    def __init__(self, types_id: _Optional[int] = ..., system_id: _Optional[int] = ..., name: _Optional[str] = ..., sort: _Optional[int] = ...) -> None: ...

class SettingsTypeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SettingsTypeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SettingsTypeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SettingsTypeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SettingsTypeTableBase]] = ...) -> None: ...
