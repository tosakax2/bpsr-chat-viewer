import stru_mod_part_upgrade_record_pb2 as _stru_mod_part_upgrade_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModNewAttr(_message.Message):
    __slots__ = ("mod_parts", "upgrade_records")
    MOD_PARTS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    mod_parts: _containers.RepeatedScalarFieldContainer[int]
    upgrade_records: _containers.RepeatedCompositeFieldContainer[_stru_mod_part_upgrade_record_pb2.ModPartUpgradeRecord]
    def __init__(self, mod_parts: _Optional[_Iterable[int]] = ..., upgrade_records: _Optional[_Iterable[_Union[_stru_mod_part_upgrade_record_pb2.ModPartUpgradeRecord, _Mapping]]] = ...) -> None: ...
