import stru_clutter_pb2 as _stru_clutter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityHomeLandClutterInfoRemoveRequest(_message.Message):
    __slots__ = ("community_id", "homeland_id", "remove_home_land_clutter")
    class RemoveHomeLandClutterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_clutter_pb2.Clutter
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_clutter_pb2.Clutter, _Mapping]] = ...) -> None: ...
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_HOME_LAND_CLUTTER_FIELD_NUMBER: _ClassVar[int]
    community_id: int
    homeland_id: int
    remove_home_land_clutter: _containers.MessageMap[int, _stru_clutter_pb2.Clutter]
    def __init__(self, community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., remove_home_land_clutter: _Optional[_Mapping[int, _stru_clutter_pb2.Clutter]] = ...) -> None: ...
