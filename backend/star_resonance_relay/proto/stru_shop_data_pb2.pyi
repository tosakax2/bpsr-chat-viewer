import stru_player_buy_record_pb2 as _stru_player_buy_record_pb2
import stru_shop_compensation_data_pb2 as _stru_shop_compensation_data_pb2
import stru_shop_refresh_record_pb2 as _stru_shop_refresh_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShopData(_message.Message):
    __slots__ = ("refresh_list", "normal_shop_records", "season_shop_records", "compensation_item_data")
    class RefreshListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_shop_refresh_record_pb2.ShopRefreshRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_shop_refresh_record_pb2.ShopRefreshRecord, _Mapping]] = ...) -> None: ...
    class NormalShopRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_player_buy_record_pb2.PlayerBuyRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_player_buy_record_pb2.PlayerBuyRecord, _Mapping]] = ...) -> None: ...
    class SeasonShopRecordsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_player_buy_record_pb2.PlayerBuyRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_player_buy_record_pb2.PlayerBuyRecord, _Mapping]] = ...) -> None: ...
    REFRESH_LIST_FIELD_NUMBER: _ClassVar[int]
    NORMAL_SHOP_RECORDS_FIELD_NUMBER: _ClassVar[int]
    SEASON_SHOP_RECORDS_FIELD_NUMBER: _ClassVar[int]
    COMPENSATION_ITEM_DATA_FIELD_NUMBER: _ClassVar[int]
    refresh_list: _containers.MessageMap[int, _stru_shop_refresh_record_pb2.ShopRefreshRecord]
    normal_shop_records: _containers.MessageMap[int, _stru_player_buy_record_pb2.PlayerBuyRecord]
    season_shop_records: _containers.MessageMap[int, _stru_player_buy_record_pb2.PlayerBuyRecord]
    compensation_item_data: _stru_shop_compensation_data_pb2.ShopCompensationData
    def __init__(self, refresh_list: _Optional[_Mapping[int, _stru_shop_refresh_record_pb2.ShopRefreshRecord]] = ..., normal_shop_records: _Optional[_Mapping[int, _stru_player_buy_record_pb2.PlayerBuyRecord]] = ..., season_shop_records: _Optional[_Mapping[int, _stru_player_buy_record_pb2.PlayerBuyRecord]] = ..., compensation_item_data: _Optional[_Union[_stru_shop_compensation_data_pb2.ShopCompensationData, _Mapping]] = ...) -> None: ...
