import stru_player_refresh_shop_record_pb2 as _stru_player_refresh_shop_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShopRefreshRecord(_message.Message):
    __slots__ = ("refresh_timestamp", "refresh_count", "shop_refresh_records")
    class ShopRefreshRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_player_refresh_shop_record_pb2.PlayerRefreshShopRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_player_refresh_shop_record_pb2.PlayerRefreshShopRecord, _Mapping]] = ...) -> None: ...
    REFRESH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REFRESH_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHOP_REFRESH_RECORDS_FIELD_NUMBER: _ClassVar[int]
    refresh_timestamp: int
    refresh_count: int
    shop_refresh_records: _containers.MessageMap[int, _stru_player_refresh_shop_record_pb2.PlayerRefreshShopRecord]
    def __init__(self, refresh_timestamp: _Optional[int] = ..., refresh_count: _Optional[int] = ..., shop_refresh_records: _Optional[_Mapping[int, _stru_player_refresh_shop_record_pb2.PlayerRefreshShopRecord]] = ...) -> None: ...
