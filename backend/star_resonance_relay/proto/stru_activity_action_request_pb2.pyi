import enum_e_pay_type_pb2 as _enum_e_pay_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityActionRequest(_message.Message):
    __slots__ = ("activity_uuid", "reward_id", "pay_type")
    ACTIVITY_UUID_FIELD_NUMBER: _ClassVar[int]
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    PAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    activity_uuid: int
    reward_id: int
    pay_type: _enum_e_pay_type_pb2.EPayType
    def __init__(self, activity_uuid: _Optional[int] = ..., reward_id: _Optional[int] = ..., pay_type: _Optional[_Union[_enum_e_pay_type_pb2.EPayType, str]] = ...) -> None: ...
