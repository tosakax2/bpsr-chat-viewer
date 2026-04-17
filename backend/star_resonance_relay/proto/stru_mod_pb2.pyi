import stru_mod_info_pb2 as _stru_mod_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mod(_message.Message):
    __slots__ = ("mod_slots", "mod_infos")
    class ModSlotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ModInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_mod_info_pb2.ModInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_mod_info_pb2.ModInfo, _Mapping]] = ...) -> None: ...
    MOD_SLOTS_FIELD_NUMBER: _ClassVar[int]
    MOD_INFOS_FIELD_NUMBER: _ClassVar[int]
    mod_slots: _containers.ScalarMap[int, int]
    mod_infos: _containers.MessageMap[int, _stru_mod_info_pb2.ModInfo]
    def __init__(self, mod_slots: _Optional[_Mapping[int, int]] = ..., mod_infos: _Optional[_Mapping[int, _stru_mod_info_pb2.ModInfo]] = ...) -> None: ...
