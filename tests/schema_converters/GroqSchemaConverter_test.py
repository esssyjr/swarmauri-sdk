import pytest
import logging
import json
from swarmauri.standard.tools.concrete.AdditionTool import AdditionTool
from swarmauri.standard.toolkits.concrete.Toolkit import Toolkit
from swarmauri.standard.agents.concrete.ToolAgent import ToolAgent

from swarmauri.standard.schema_converters.concrete.GroqSchemaConverter import (
    CohereSchemaConverter as Schema,
)


@pytest.mark.unit
def test_ubc_resource():
    assert Schema().resource == "SchemaConverter"


@pytest.mark.unit
def test_ubc_type():
    schema = Schema()
    assert schema.type == "GroqSchemaConverter"


@pytest.mark.unit
def test_serialization():
    schema = Schema()
    assert schema.id == Schema.model_validate_json(schema.model_dump_json()).id


@pytest.mark.unit
def test_convert():
    toolkit = Toolkit()
    tool = AdditionTool()
    toolkit.add_tool(tool)
    result = [Schema().convert(toolkit.tools[tool]) for tool in toolkit.tools]
    logging.info(result)
    assert json.loads(json.dumps(result))
