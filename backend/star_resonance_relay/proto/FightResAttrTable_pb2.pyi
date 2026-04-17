from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FightResAttrTableBase(_message.Message):
    __slots__ = ("id", "name", "can_cost")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_COST_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    can_cost: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., can_cost: bool = ...) -> None: ...

class FightResAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FightResAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FightResAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FightResAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FightResAttrTableBase]] = ...) -> None: ...
