from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CompensationData(_message.Message):
    __slots__ = ("overflow_energy", "finish_times", "climb_up_layer_id")
    OVERFLOW_ENERGY_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIMES_FIELD_NUMBER: _ClassVar[int]
    CLIMB_UP_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    overflow_energy: int
    finish_times: int
    climb_up_layer_id: int
    def __init__(self, overflow_energy: _Optional[int] = ..., finish_times: _Optional[int] = ..., climb_up_layer_id: _Optional[int] = ...) -> None: ...
