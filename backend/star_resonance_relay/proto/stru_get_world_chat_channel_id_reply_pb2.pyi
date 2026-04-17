import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWorldChatChannelIdReply(_message.Message):
    __slots__ = ("channel_id", "user_num", "max_num", "state", "err_code")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NUM_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    channel_id: int
    user_num: int
    max_num: int
    state: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, channel_id: _Optional[int] = ..., user_num: _Optional[int] = ..., max_num: _Optional[int] = ..., state: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
