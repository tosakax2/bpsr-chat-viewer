import stru_mail_level_condition_pb2 as _stru_mail_level_condition_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailExtraCondition(_message.Message):
    __slots__ = ("level", "login_channels", "last_active_days", "area_ids", "register_after_time")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LOGIN_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_DAYS_FIELD_NUMBER: _ClassVar[int]
    AREA_IDS_FIELD_NUMBER: _ClassVar[int]
    REGISTER_AFTER_TIME_FIELD_NUMBER: _ClassVar[int]
    level: _stru_mail_level_condition_pb2.MailLevelCondition
    login_channels: _containers.RepeatedScalarFieldContainer[int]
    last_active_days: int
    area_ids: _containers.RepeatedScalarFieldContainer[str]
    register_after_time: int
    def __init__(self, level: _Optional[_Union[_stru_mail_level_condition_pb2.MailLevelCondition, _Mapping]] = ..., login_channels: _Optional[_Iterable[int]] = ..., last_active_days: _Optional[int] = ..., area_ids: _Optional[_Iterable[str]] = ..., register_after_time: _Optional[int] = ...) -> None: ...
