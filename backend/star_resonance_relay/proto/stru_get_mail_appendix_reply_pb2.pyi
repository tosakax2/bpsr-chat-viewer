import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_item_pb2 as _stru_item_pb2
import stru_mail_base_pb2 as _stru_mail_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailAppendixReply(_message.Message):
    __slots__ = ("mails", "rewards", "err_code")
    class MailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_mail_base_pb2.MailBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_mail_base_pb2.MailBase, _Mapping]] = ...) -> None: ...
    MAILS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    mails: _containers.MessageMap[int, _stru_mail_base_pb2.MailBase]
    rewards: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, mails: _Optional[_Mapping[int, _stru_mail_base_pb2.MailBase]] = ..., rewards: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
