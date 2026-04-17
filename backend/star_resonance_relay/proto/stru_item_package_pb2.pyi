import stru_package_pb2 as _stru_package_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemPackage(_message.Message):
    __slots__ = ("packages", "unlock_items", "quick_bar", "item_uuid", "use_group_cd")
    class PackagesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_package_pb2.Package
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_package_pb2.Package, _Mapping]] = ...) -> None: ...
    class UnlockItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class UseGroupCdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    QUICK_BAR_FIELD_NUMBER: _ClassVar[int]
    ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    USE_GROUP_CD_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.MessageMap[int, _stru_package_pb2.Package]
    unlock_items: _containers.ScalarMap[int, int]
    quick_bar: int
    item_uuid: int
    use_group_cd: _containers.ScalarMap[int, int]
    def __init__(self, packages: _Optional[_Mapping[int, _stru_package_pb2.Package]] = ..., unlock_items: _Optional[_Mapping[int, int]] = ..., quick_bar: _Optional[int] = ..., item_uuid: _Optional[int] = ..., use_group_cd: _Optional[_Mapping[int, int]] = ...) -> None: ...
