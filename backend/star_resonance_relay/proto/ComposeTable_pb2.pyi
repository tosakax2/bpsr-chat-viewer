from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComposeTableBase(_message.Message):
    __slots__ = ("id", "system_id", "nums", "name", "successful_probability", "obtain_id", "obtain_num", "obtain_name", "consumable_tips")
    ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    NUMS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_NUM_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_TIPS_FIELD_NUMBER: _ClassVar[int]
    id: int
    system_id: int
    nums: int
    name: str
    successful_probability: int
    obtain_id: int
    obtain_num: int
    obtain_name: str
    consumable_tips: int
    def __init__(self, id: _Optional[int] = ..., system_id: _Optional[int] = ..., nums: _Optional[int] = ..., name: _Optional[str] = ..., successful_probability: _Optional[int] = ..., obtain_id: _Optional[int] = ..., obtain_num: _Optional[int] = ..., obtain_name: _Optional[str] = ..., consumable_tips: _Optional[int] = ...) -> None: ...

class ComposeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ComposeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ComposeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ComposeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ComposeTableBase]] = ...) -> None: ...
