# mcpvertexai

for mcpclaude install 

pip install mcp fastmcp google-genai grpcio

in claudedesktop config file

{
  "mcpServers": {
    "VertexAIMCP": {
      "command": "python",
      "args": [
        "C:\\vertexragadk\\mcpclaude.py"
      ]
    }
  },

  "preferences": {
    "coworkWebSearchEnabled": true,
    "remoteToolsDeviceName": "",
    "coworkScheduledTasksEnabled": false,
    "ccdScheduledTasksEnabled": false,

    "epitaxyPrefs": {
      "starred-local-code-sessions": [],
      "starred-cowork-spaces": [],
      "starred-session-groups": []
    }
  }
}
