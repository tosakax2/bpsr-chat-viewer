from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShopCompensationInfo(_message.Message):
    __slots__ = ("entor_store_num", "buy_num")
    ENTOR_STORE_NUM_FIELD_NUMBER: _ClassVar[int]
    BUY_NUM_FIELD_NUMBER: _ClassVar[int]
    entor_store_num: int
    buy_num: int
    def __init__(self, entor_store_num: _Optional[int] = ..., buy_num: _Optional[int] = ...) -> None: ...
