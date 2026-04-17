from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HousingItemsTypeBase(_message.Message):
    __slots__ = ("id", "type_name", "group_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    type_name: int
    group_id: int
    def __init__(self, id: _Optional[int] = ..., type_name: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...

class HousingItemsTypeMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: HousingItemsTypeBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[HousingItemsTypeBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, HousingItemsTypeBase]
    def __init__(self, datas: _Optional[_Mapping[int, HousingItemsTypeBase]] = ...) -> None: ...
