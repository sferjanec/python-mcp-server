from mcp.server.fastmcp import FastMCP
from datetime import datetime
import os

mcp = FastMCP("DevAgentToolkit")

@mcp.tool()
def read_project_file(file_path: str) -> str:
    """
    Reads the content of a local project file (Spring Boot or Angular)
    :param file_path: The absolute path to the file.
    """

    #Simple security check for demo purposes
    if not os.path.exists(file_path):
        return f"Error: File {file_path} does not exist."
    
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def write_project_file(file_path: str, content: str) -> str:
    """
    Writes or overwrites a file in the project. 
    Use this to scaffold Angular components or Spring Boot services.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"
    
@mcp.tool()
def analyze_jira_text(story_text: str) -> str:
    """
    A placeholder tool that structures raw JIRA text into a technical
    summary for other agents to consume
    """
    return f"Process JIRA requirements:\n{story_text}"

@mcp.tool()
def list_directory(path: str = ".") -> str:
    """
    Lists files and directories in a given path. 
    Use this to explore the Spring Boot or Angular project structure.
    """
    try:
        items = os.listdir(path)
        # Filter out noise like .git or node_modules for cleaner AI context
        filtered = [i for i in items if i not in ['.git', 'node_modules', '.venv', 'target', 'dist']]
        return "\n".join(filtered)
    except Exception as e:
        return f"Error listing directory: {str(e)}"

@mcp.tool()
def create_mock_resource(filename: str, record_count: int = 10) -> str:
    """
    Generates a mock JSON file in src/assets/ for prototying
    """
    mock_data = [
        {
            "id": i,
            "taskName": f"Admin Task {i}",
            "status": random.choice(["Pending", "In Progress", "Completed"]),
            "priority": random.choice(["Low", "Medium", "High"])
        } for i in range(1, record_count + 1)
    ]

    path =f"src/assets/{filename}.json"
    os.makedirs("src/assets", exist_ok=True)
    with open(path, "w") as f:
        json.dump(mock_data, f, indent=2)
    return f"Mock resource created at {path}"

@mcp.tool()
def append_developer_log(change_description: str, files_affected: str) -> str:
    """
    Appends a timestamped entry to the developer_log.md file.
    :param change_description: A brief summary of what was changed.
    :param files_affected: A comma-separated string of file names.
    """
    log_path = "DEVELOPER_LOG.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = (
        f"\n## [{timestamp}]\n"
        f"- **Action:** {change_description}\n"
        f"- **Files:** {files_affected}\n"
        f"- **Status:** Verified via Build\n"
        "---"
    )
    
    try:
        with open(log_path, "a") as f:
            f.write(log_entry)
        return f"Successfully updated DEVELOPER_LOG.md"
    except Exception as e:
        return f"Error updating log: {str(e)}"

    
if __name__ == "__main__":
    mcp.run(transport="stdio")