from google import genai
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FastVertexMCP")

@mcp.tool()
def ask_gemini(prompt: str) -> str:

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

if __name__ == "__main__":
    print("MCP Server Running...")
    mcp.run()