import stru_social_data_pb2 as _stru_social_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountInfo(_message.Message):
    __slots__ = ("account_id", "open_id", "chars", "token", "restrict_time", "delete_char_ids_left_time", "ban_reason")
    class DeleteCharIdsLeftTimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    CHARS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_CHAR_IDS_LEFT_TIME_FIELD_NUMBER: _ClassVar[int]
    BAN_REASON_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    open_id: str
    chars: _containers.RepeatedCompositeFieldContainer[_stru_social_data_pb2.SocialData]
    token: str
    restrict_time: int
    delete_char_ids_left_time: _containers.ScalarMap[int, int]
    ban_reason: int
    def __init__(self, account_id: _Optional[str] = ..., open_id: _Optional[str] = ..., chars: _Optional[_Iterable[_Union[_stru_social_data_pb2.SocialData, _Mapping]]] = ..., token: _Optional[str] = ..., restrict_time: _Optional[int] = ..., delete_char_ids_left_time: _Optional[_Mapping[int, int]] = ..., ban_reason: _Optional[int] = ...) -> None: ...
