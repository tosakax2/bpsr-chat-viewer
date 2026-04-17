import stru_home_land_item_instance_pb2 as _stru_home_land_item_instance_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityItemUpdateRequest(_message.Message):
    __slots__ = ("remove_instances", "add_instances", "update_instances")
    class RemoveInstancesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AddInstancesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_home_land_item_instance_pb2.HomeLandItemInstance
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ...) -> None: ...
    class UpdateInstancesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_home_land_item_instance_pb2.HomeLandItemInstance
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ...) -> None: ...
    REMOVE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ADD_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    remove_instances: _containers.ScalarMap[int, int]
    add_instances: _containers.MessageMap[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]
    update_instances: _containers.MessageMap[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]
    def __init__(self, remove_instances: _Optional[_Mapping[int, int]] = ..., add_instances: _Optional[_Mapping[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]] = ..., update_instances: _Optional[_Mapping[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]] = ...) -> None: ...
