from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConditionTableBase(_message.Message):
    __slots__ = ("type", "param", "is_lua", "example", "refresh_num")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    IS_LUA_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_NUM_FIELD_NUMBER: _ClassVar[int]
    type: int
    param: str
    is_lua: bool
    example: str
    refresh_num: str
    def __init__(self, type: _Optional[int] = ..., param: _Optional[str] = ..., is_lua: bool = ..., example: _Optional[str] = ..., refresh_num: _Optional[str] = ...) -> None: ...

class ConditionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ConditionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ConditionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ConditionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ConditionTableBase]] = ...) -> None: ...
