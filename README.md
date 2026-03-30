# Dev-Agent MCP Toolkit

An MCP (Model Context Protocol) server designed to orchestrate AI agents for **Angular 21** and **Spring Boot** development. This toolkit enables Gemini to interact directly with a local RHEL/WSL filesystem to scaffold components, manage mock data, and maintain automated developer logs.

## 🛠 Features
- **Local File Management:** Read/Write access to project source code.
- **Angular 21 Scaffolding:** Automated creation of components using `rxResource` and Signals.
- **Automated Audit Trail:** A custom tool to maintain `developer_log.md` for every AI action.
- **Mock Data Generation:** Rapid prototyping of JSON resources for frontend development.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Node.js (for the MCP Inspector)
- A Google Gemini API Key (Vertex AI or AI Studio)

### 2. Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd mcp-server
```

# Setup Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]" fastmcp
```

### 3. Running the Server (Development)
```bash
npx -y @modelcontextprotocol/inspector python server.py
```

# 🤖 Gemini CLI Configuration

To use this toolkit with the gemini npm package, update your settings.

# Environment Variables
Create a .env file in your project root (this is ignored by git):

# For AI Studio Key:
GEMINI_API_KEY=your_key_here

# OR for Vertex AI (Enterprise):
GOOGLE_API_KEY=your_key_here
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_GENAI_USE_VERTEXAI=true

# Settings Configuration
Add the server to your ~/.gemini/settings.json:

```JSON
{
  "mcpServers": {
    "work-tools": {
      "command": "/absolute/path/to/your/.venv/bin/python",
      "args": ["/absolute/path/to/your/server.py"]
    }
  }
}
```

### 📜 System Blueprint (GEMINI.md)
This project relies on a GEMINI.md file in the target project root to enforce standards such as:

Using rxResource with the stream property.

Enforcing the inject() pattern for services.

Mandatory updates to the developer_log.md.