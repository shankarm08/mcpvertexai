import os
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "false"

from google import genai
from mcp.server.fastmcp import FastMCP

# -----------------------------------
# Create MCP Server
# -----------------------------------
mcp = FastMCP("VertexAIMCP")


# -----------------------------------
# Gemini Tool
# -----------------------------------
@mcp.tool()
def ask_gemini(prompt: str) -> str:
    """
    Ask Gemini using Vertex AI
    """

    client = genai.Client(
        vertexai=True,
        project="",
        location=""
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text


# -----------------------------------
# Addition Tool
# -----------------------------------
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers
    """

    result = a + b

    print(f"Adding {a} + {b} = {result}")

    return result


# -----------------------------------
# Summary Tool
# -----------------------------------
@mcp.tool()
def summarize_text(text: str) -> str:
    """
    Summarize text using Gemini
    """

    client = genai.Client(
        vertexai=True,
        project="rag-project-495007",
        location="us-central1"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Summarize this:\n{text}"
    )

    return response.text


# -----------------------------------
# Main
# -----------------------------------
if __name__ == "__main__":

    print("\nTesting Tools...\n")

    # Test Addition Tool
    add_result = add_numbers(5, 10)
    print("Addition Result:", add_result)

    # Test Gemini Tool
    gemini_result = ask_gemini("Explain AI in one line")
    print("Gemini Result:", gemini_result)

    print("\nMCP Server Running...\n")

    # Run MCP Server
    mcp.run()