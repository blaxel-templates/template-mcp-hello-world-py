from logging import getLogger
from typing import Annotated

from blaxel import env
from blaxel.core.mcp.server import FastMCP

mcp = FastMCP("mcp-helloworld-python")
logger = getLogger(__name__)


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.tool()
def hello_world(
    firstname: Annotated[
        str,
        "First name of the user",
    ],
) -> str:
    """Say hello to the user"""
    return f"Hello {firstname}!"


if not env["BL_DEBUG"]:
    mcp.run(transport="ws")
