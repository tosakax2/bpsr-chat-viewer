from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RdCookRequest(_message.Message):
    __slots__ = ("main_materials", "cook_methods")
    MAIN_MATERIALS_FIELD_NUMBER: _ClassVar[int]
    COOK_METHODS_FIELD_NUMBER: _ClassVar[int]
    main_materials: _containers.RepeatedScalarFieldContainer[int]
    cook_methods: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, main_materials: _Optional[_Iterable[int]] = ..., cook_methods: _Optional[_Iterable[int]] = ...) -> None: ...
