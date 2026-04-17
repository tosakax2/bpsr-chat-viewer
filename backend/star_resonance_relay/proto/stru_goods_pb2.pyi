from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Goods(_message.Message):
    __slots__ = ("goods_id", "goods_num")
    GOODS_ID_FIELD_NUMBER: _ClassVar[int]
    GOODS_NUM_FIELD_NUMBER: _ClassVar[int]
    goods_id: int
    goods_num: int
    def __init__(self, goods_id: _Optional[int] = ..., goods_num: _Optional[int] = ...) -> None: ...
