from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MailStateInfo(_message.Message):
    __slots__ = ("mail_state", "mail_config_id")
    MAIL_STATE_FIELD_NUMBER: _ClassVar[int]
    MAIL_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    mail_state: int
    mail_config_id: int
    def __init__(self, mail_state: _Optional[int] = ..., mail_config_id: _Optional[int] = ...) -> None: ...
