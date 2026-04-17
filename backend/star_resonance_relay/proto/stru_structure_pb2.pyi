import stru_int_vec3_pb2 as _stru_int_vec3_pb2
import stru_structure_farmland_info_pb2 as _stru_structure_farmland_info_pb2
import stru_structure_lamplight_info_pb2 as _stru_structure_lamplight_info_pb2
import stru_structure_material_info_pb2 as _stru_structure_material_info_pb2
import stru_vec4_pb2 as _stru_vec4_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Structure(_message.Message):
    __slots__ = ("uuid", "client_uuid", "group_id", "item_id", "char_id", "position", "quaternion", "operator_char_id", "name", "material_info", "lamplight_info", "farmland_info")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_UUID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_INFO_FIELD_NUMBER: _ClassVar[int]
    LAMPLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
    FARMLAND_INFO_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    client_uuid: int
    group_id: int
    item_id: int
    char_id: int
    position: _stru_int_vec3_pb2.IntVec3
    quaternion: _stru_vec4_pb2.Vec4
    operator_char_id: int
    name: str
    material_info: _stru_structure_material_info_pb2.StructureMaterialInfo
    lamplight_info: _stru_structure_lamplight_info_pb2.StructureLamplightInfo
    farmland_info: _stru_structure_farmland_info_pb2.StructureFarmlandInfo
    def __init__(self, uuid: _Optional[int] = ..., client_uuid: _Optional[int] = ..., group_id: _Optional[int] = ..., item_id: _Optional[int] = ..., char_id: _Optional[int] = ..., position: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ..., quaternion: _Optional[_Union[_stru_vec4_pb2.Vec4, _Mapping]] = ..., operator_char_id: _Optional[int] = ..., name: _Optional[str] = ..., material_info: _Optional[_Union[_stru_structure_material_info_pb2.StructureMaterialInfo, _Mapping]] = ..., lamplight_info: _Optional[_Union[_stru_structure_lamplight_info_pb2.StructureLamplightInfo, _Mapping]] = ..., farmland_info: _Optional[_Union[_stru_structure_farmland_info_pb2.StructureFarmlandInfo, _Mapping]] = ...) -> None: ...
