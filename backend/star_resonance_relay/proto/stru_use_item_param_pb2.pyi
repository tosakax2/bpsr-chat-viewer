from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UseItemParam(_message.Message):
    __slots__ = ("item_uuid", "param", "select", "use_num")
    class SelectEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    USE_NUM_FIELD_NUMBER: _ClassVar[int]
    item_uuid: int
    param: str
    select: _containers.ScalarMap[int, int]
    use_num: int
    def __init__(self, item_uuid: _Optional[int] = ..., param: _Optional[str] = ..., select: _Optional[_Mapping[int, int]] = ..., use_num: _Optional[int] = ...) -> None: ...
