import stru_char_list_pb2 as _stru_char_list_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteFriendRequest(_message.Message):
    __slots__ = ("char_list",)
    CHAR_LIST_FIELD_NUMBER: _ClassVar[int]
    char_list: _stru_char_list_pb2.CharList
    def __init__(self, char_list: _Optional[_Union[_stru_char_list_pb2.CharList, _Mapping]] = ...) -> None: ...
