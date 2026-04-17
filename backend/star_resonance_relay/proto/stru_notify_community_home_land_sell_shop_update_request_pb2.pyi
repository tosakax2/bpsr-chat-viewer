import stru_home_land_sell_shop_info_pb2 as _stru_home_land_sell_shop_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityHomeLandSellShopUpdateRequest(_message.Message):
    __slots__ = ("home_land_sell_shop_info",)
    HOME_LAND_SELL_SHOP_INFO_FIELD_NUMBER: _ClassVar[int]
    home_land_sell_shop_info: _stru_home_land_sell_shop_info_pb2.HomeLandSellShopInfo
    def __init__(self, home_land_sell_shop_info: _Optional[_Union[_stru_home_land_sell_shop_info_pb2.HomeLandSellShopInfo, _Mapping]] = ...) -> None: ...
