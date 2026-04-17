from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TssAccountInfoProto(_message.Message):
    __slots__ = ("account", "account_type", "plat_id", "game_id", "world_id", "channel_id", "role_id", "anti_data", "account_id", "client_ip", "role_name", "index")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAT_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    WORLD_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ANTI_DATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    account: str
    account_type: int
    plat_id: int
    game_id: int
    world_id: int
    channel_id: int
    role_id: int
    anti_data: bytes
    account_id: str
    client_ip: str
    role_name: str
    index: int
    def __init__(self, account: _Optional[str] = ..., account_type: _Optional[int] = ..., plat_id: _Optional[int] = ..., game_id: _Optional[int] = ..., world_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., role_id: _Optional[int] = ..., anti_data: _Optional[bytes] = ..., account_id: _Optional[str] = ..., client_ip: _Optional[str] = ..., role_name: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...
