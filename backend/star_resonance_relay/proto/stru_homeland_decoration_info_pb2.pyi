import stru_homeland_lamplight_info_pb2 as _stru_homeland_lamplight_info_pb2
import stru_homeland_material_info_pb2 as _stru_homeland_material_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandDecorationInfo(_message.Message):
    __slots__ = ("lamplight_info", "material_infos")
    class MaterialInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_homeland_material_info_pb2.HomelandMaterialInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_homeland_material_info_pb2.HomelandMaterialInfo, _Mapping]] = ...) -> None: ...
    LAMPLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_INFOS_FIELD_NUMBER: _ClassVar[int]
    lamplight_info: _stru_homeland_lamplight_info_pb2.HomelandLamplightInfo
    material_infos: _containers.MessageMap[int, _stru_homeland_material_info_pb2.HomelandMaterialInfo]
    def __init__(self, lamplight_info: _Optional[_Union[_stru_homeland_lamplight_info_pb2.HomelandLamplightInfo, _Mapping]] = ..., material_infos: _Optional[_Mapping[int, _stru_homeland_material_info_pb2.HomelandMaterialInfo]] = ...) -> None: ...
