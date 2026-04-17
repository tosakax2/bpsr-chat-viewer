import stru_item_pb2 as _stru_item_pb2
import stru_mail_extra_condition_pb2 as _stru_mail_extra_condition_pb2
import stru_mail_multilingual_text_pb2 as _stru_mail_multilingual_text_pb2
import enum_mail_state_pb2 as _enum_mail_state_pb2
import enum_mail_type_pb2 as _enum_mail_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MailBase(_message.Message):
    __slots__ = ("mail_uuid", "mail_config_id", "create_time", "mail_type", "send_id", "send_name", "mail_title", "mail_body", "timeout_ms", "appendix", "mail_state", "title_prams", "body_prams", "accept_id", "importance", "award_ids", "register_before_time", "condition", "is_collect", "multilingual_text")
    MAIL_UUID_FIELD_NUMBER: _ClassVar[int]
    MAIL_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEND_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_NAME_FIELD_NUMBER: _ClassVar[int]
    MAIL_TITLE_FIELD_NUMBER: _ClassVar[int]
    MAIL_BODY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    APPENDIX_FIELD_NUMBER: _ClassVar[int]
    MAIL_STATE_FIELD_NUMBER: _ClassVar[int]
    TITLE_PRAMS_FIELD_NUMBER: _ClassVar[int]
    BODY_PRAMS_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    REGISTER_BEFORE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    IS_COLLECT_FIELD_NUMBER: _ClassVar[int]
    MULTILINGUAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    mail_uuid: int
    mail_config_id: int
    create_time: int
    mail_type: _enum_mail_type_pb2.MailType
    send_id: int
    send_name: str
    mail_title: str
    mail_body: str
    timeout_ms: int
    appendix: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    mail_state: _enum_mail_state_pb2.MailState
    title_prams: _containers.RepeatedScalarFieldContainer[str]
    body_prams: _containers.RepeatedScalarFieldContainer[str]
    accept_id: int
    importance: int
    award_ids: _containers.RepeatedScalarFieldContainer[int]
    register_before_time: int
    condition: _stru_mail_extra_condition_pb2.MailExtraCondition
    is_collect: bool
    multilingual_text: _containers.RepeatedCompositeFieldContainer[_stru_mail_multilingual_text_pb2.MailMultilingualText]
    def __init__(self, mail_uuid: _Optional[int] = ..., mail_config_id: _Optional[int] = ..., create_time: _Optional[int] = ..., mail_type: _Optional[_Union[_enum_mail_type_pb2.MailType, str]] = ..., send_id: _Optional[int] = ..., send_name: _Optional[str] = ..., mail_title: _Optional[str] = ..., mail_body: _Optional[str] = ..., timeout_ms: _Optional[int] = ..., appendix: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., mail_state: _Optional[_Union[_enum_mail_state_pb2.MailState, str]] = ..., title_prams: _Optional[_Iterable[str]] = ..., body_prams: _Optional[_Iterable[str]] = ..., accept_id: _Optional[int] = ..., importance: _Optional[int] = ..., award_ids: _Optional[_Iterable[int]] = ..., register_before_time: _Optional[int] = ..., condition: _Optional[_Union[_stru_mail_extra_condition_pb2.MailExtraCondition, _Mapping]] = ..., is_collect: bool = ..., multilingual_text: _Optional[_Iterable[_Union[_stru_mail_multilingual_text_pb2.MailMultilingualText, _Mapping]]] = ...) -> None: ...
