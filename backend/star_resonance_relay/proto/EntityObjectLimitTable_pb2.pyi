from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityObjectLimitTableBase(_message.Message):
    __slots__ = ("id", "base_object_limit", "summon_object_limit", "timer_limit", "save_var_limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASE_OBJECT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUMMON_OBJECT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TIMER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SAVE_VAR_LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    base_object_limit: int
    summon_object_limit: int
    timer_limit: int
    save_var_limit: int
    def __init__(self, id: _Optional[int] = ..., base_object_limit: _Optional[int] = ..., summon_object_limit: _Optional[int] = ..., timer_limit: _Optional[int] = ..., save_var_limit: _Optional[int] = ...) -> None: ...

class EntityObjectLimitTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EntityObjectLimitTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EntityObjectLimitTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EntityObjectLimitTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EntityObjectLimitTableBase]] = ...) -> None: ...
