from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatStickersTableBase(_message.Message):
    __slots__ = ("id", "type", "group_id", "res", "unlock_item")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_ITEM_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    group_id: int
    res: str
    unlock_item: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., group_id: _Optional[int] = ..., res: _Optional[str] = ..., unlock_item: _Optional[int] = ...) -> None: ...

class ChatStickersTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChatStickersTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChatStickersTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChatStickersTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChatStickersTableBase]] = ...) -> None: ...
