from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetFirstPayInfo(_message.Message):
    __slots__ = ("ladder_pay_info", "extra_award_id")
    class LadderPayInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LADDER_PAY_INFO_FIELD_NUMBER: _ClassVar[int]
    EXTRA_AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    ladder_pay_info: _containers.ScalarMap[int, int]
    extra_award_id: int
    def __init__(self, ladder_pay_info: _Optional[_Mapping[int, int]] = ..., extra_award_id: _Optional[int] = ...) -> None: ...
