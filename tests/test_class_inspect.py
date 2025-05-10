from dataclasses import dataclass

import pytest
from attr import dataclass as attr_dataclass
from msgspec import Struct
from pydantic import BaseModel
from pydantic.dataclasses import dataclass as pydantic_dataclass

from dataclass_settings import load_settings


@attr_dataclass
class AttrFoo:
    foo: int = 0


@attr_dataclass
class AttrConfig:
    foo: AttrFoo


@dataclass
class DataclassFoo:
    foo: int = 0


@dataclass
class DataclassConfig:
    foo: DataclassFoo


class MsgspecFoo(Struct):
    foo: int = 0


class MsgspecConfig(Struct):
    foo: MsgspecFoo


class PydanticFoo(BaseModel):
    foo: int = 0


class PydanticConfig(BaseModel):
    foo: PydanticFoo


@pydantic_dataclass
class PDataclassFoo:
    foo: int = 0


@pydantic_dataclass
class PDataclassConfig:
    foo: PDataclassFoo


@pytest.mark.parametrize(
    "config_class, nested",
    [
        (AttrConfig, AttrFoo),
        (DataclassConfig, DataclassFoo),
        (MsgspecConfig, MsgspecFoo),
        (PydanticConfig, PydanticFoo),
        (PDataclassConfig, PDataclassFoo),
    ],
)
def test_successful_validation_of_fully_default_subobjects(config_class, nested):
    config = load_settings(config_class)
    assert config == config_class(foo=nested(foo=0))
