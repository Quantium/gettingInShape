import subprocess
import re
from collections import defaultdict

def get_git_log():
    """Runs the git log command and returns the formatted output."""
    command = ['git', 'log', '--all', '--graph', '--pretty=format:%h %p %s']
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.split("\n")

def parse_git_log(log_lines):
    """Parses the git log output and structures commit relationships."""
    commits = {}
    edges = []
    branches = defaultdict(list)
    
    for line in log_lines:
        match = re.match(r'(\*+)?\s*([\da-f]+)\s*([\da-f\s]*)\s*(.+)', line)
        if match:
            graph, commit, parents, message = match.groups()
            parents = parents.split() if parents else []
            
            commits[commit] = {
                "message": message,
                "parents": parents
            }
            
            if parents:
                for parent in parents:
                    edges.append((parent, commit))

    return commits, edges

def generate_mermaid_code(commits, edges):
    """Generates Mermaid gitGraph code from parsed commits and edges."""
    mermaid = ["```mermaid", "gitGraph"]
    
    # Get commits in chronological order (reverse of git log)
    commit_list = list(commits.items())
    commit_list.reverse()  # Reverse to get chronological order
    
    for commit, data in commit_list:
        message = data["message"].replace('"', "'")
        # Truncate very long messages
        if len(message) > 50:
            message = message[:47] + "..."
        mermaid.append(f"  commit id: \"{message}\"")

    mermaid.append("```")
    return "\n".join(mermaid)

if __name__ == "__main__":
    log_lines = get_git_log()
    commits, edges = parse_git_log(log_lines)
    mermaid_code = generate_mermaid_code(commits, edges)
    print(mermaid_code)