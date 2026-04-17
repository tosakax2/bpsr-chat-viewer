import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RdCookReply(_message.Message):
    __slots__ = ("recipe_id", "food_id", "err_code")
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    FOOD_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    recipe_id: int
    food_id: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, recipe_id: _Optional[int] = ..., food_id: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
