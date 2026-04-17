from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StageBehaveCallEventTableBase(_message.Message):
    __slots__ = ("id", "event_type", "lua_event_name", "c_sharp_event_id", "desc")
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LUA_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    C_SHARP_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    id: int
    event_type: int
    lua_event_name: str
    c_sharp_event_id: int
    desc: str
    def __init__(self, id: _Optional[int] = ..., event_type: _Optional[int] = ..., lua_event_name: _Optional[str] = ..., c_sharp_event_id: _Optional[int] = ..., desc: _Optional[str] = ...) -> None: ...

class StageBehaveCallEventTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StageBehaveCallEventTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StageBehaveCallEventTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, StageBehaveCallEventTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, StageBehaveCallEventTableBase]] = ...) -> None: ...
