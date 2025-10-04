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
    mermaid = ["```mermaid", "gitGraph", "  commit id: \"Initial commit\""]

    commit_map = {}
    count = 1
    
    for commit, data in commits.items():
        commit_map[commit] = count
        message = data["message"].replace('"', "'")
        mermaid.append(f"  commit id: \"{message}\"")
        count += 1

    for parent, child in edges:
        if parent in commit_map and child in commit_map:
            mermaid.append(f"  {commit_map[parent]} --> {commit_map[child]}")

    mermaid.append("```")
    return "\n".join(mermaid)

if __name__ == "__main__":
    log_lines = get_git_log()
    commits, edges = parse_git_log(log_lines)
    mermaid_code = generate_mermaid_code(commits, edges)
    print(mermaid_code)