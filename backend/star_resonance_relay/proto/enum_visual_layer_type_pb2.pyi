from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VisualLayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VisualLayerTypePublic: _ClassVar[VisualLayerType]
    VisualLayerTypeMultiPlayer: _ClassVar[VisualLayerType]
    VisualLayerTypePrivate: _ClassVar[VisualLayerType]
    VisualLayerTypeMultiPlayerUuid: _ClassVar[VisualLayerType]
    VisualLayerTypeCommunityOutdoor: _ClassVar[VisualLayerType]
    VisualLayerTypeCommunityIndoor: _ClassVar[VisualLayerType]
VisualLayerTypePublic: VisualLayerType
VisualLayerTypeMultiPlayer: VisualLayerType
VisualLayerTypePrivate: VisualLayerType
VisualLayerTypeMultiPlayerUuid: VisualLayerType
VisualLayerTypeCommunityOutdoor: VisualLayerType
VisualLayerTypeCommunityIndoor: VisualLayerType
