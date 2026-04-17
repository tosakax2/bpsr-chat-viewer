import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_shop_tab_info_pb2 as _stru_shop_tab_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetShopItemListReply(_message.Message):
    __slots__ = ("tab", "err_code")
    class TabEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_shop_tab_info_pb2.ShopTabInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_shop_tab_info_pb2.ShopTabInfo, _Mapping]] = ...) -> None: ...
    TAB_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    tab: _containers.MessageMap[int, _stru_shop_tab_info_pb2.ShopTabInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, tab: _Optional[_Mapping[int, _stru_shop_tab_info_pb2.ShopTabInfo]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
