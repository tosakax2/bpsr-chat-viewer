import stru_gasha_guarantee_info_pb2 as _stru_gasha_guarantee_info_pb2
import stru_gasha_info_pb2 as _stru_gasha_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GashaData(_message.Message):
    __slots__ = ("gasha_infos", "gasha_guarantee_infos")
    class GashaInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_gasha_info_pb2.GashaInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_gasha_info_pb2.GashaInfo, _Mapping]] = ...) -> None: ...
    class GashaGuaranteeInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_gasha_guarantee_info_pb2.GashaGuaranteeInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_gasha_guarantee_info_pb2.GashaGuaranteeInfo, _Mapping]] = ...) -> None: ...
    GASHA_INFOS_FIELD_NUMBER: _ClassVar[int]
    GASHA_GUARANTEE_INFOS_FIELD_NUMBER: _ClassVar[int]
    gasha_infos: _containers.MessageMap[int, _stru_gasha_info_pb2.GashaInfo]
    gasha_guarantee_infos: _containers.MessageMap[int, _stru_gasha_guarantee_info_pb2.GashaGuaranteeInfo]
    def __init__(self, gasha_infos: _Optional[_Mapping[int, _stru_gasha_info_pb2.GashaInfo]] = ..., gasha_guarantee_infos: _Optional[_Mapping[int, _stru_gasha_guarantee_info_pb2.GashaGuaranteeInfo]] = ...) -> None: ...
