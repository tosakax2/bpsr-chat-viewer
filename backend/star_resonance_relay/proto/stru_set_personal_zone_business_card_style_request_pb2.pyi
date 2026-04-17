from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneBusinessCardStyleRequest(_message.Message):
    __slots__ = ("business_card_style_id",)
    BUSINESS_CARD_STYLE_ID_FIELD_NUMBER: _ClassVar[int]
    business_card_style_id: int
    def __init__(self, business_card_style_id: _Optional[int] = ...) -> None: ...
