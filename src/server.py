from blaxel import env
from blaxel.mcp.server import FastMCP

from typing import Annotated
from logging import getLogger

mcp = FastMCP("mcp-helloworld-python")
logger = getLogger(__name__)

@mcp.tool()
def hello_world(
    first_name: Annotated[
        str,
        "First name of the user",
    ],
) -> str:
    """Say hello to the user"""
    return f"Hello {first_name}!"

if not env["BL_DEBUG"]:
    mcp.run(transport="ws")