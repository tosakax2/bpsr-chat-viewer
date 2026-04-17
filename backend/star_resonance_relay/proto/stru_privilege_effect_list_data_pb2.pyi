import stru_single_privilege_effect_data_pb2 as _stru_single_privilege_effect_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivilegeEffectListData(_message.Message):
    __slots__ = ("privilege_effect_data",)
    PRIVILEGE_EFFECT_DATA_FIELD_NUMBER: _ClassVar[int]
    privilege_effect_data: _containers.RepeatedCompositeFieldContainer[_stru_single_privilege_effect_data_pb2.SinglePrivilegeEffectData]
    def __init__(self, privilege_effect_data: _Optional[_Iterable[_Union[_stru_single_privilege_effect_data_pb2.SinglePrivilegeEffectData, _Mapping]]] = ...) -> None: ...
