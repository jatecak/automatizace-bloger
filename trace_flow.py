import json

with open("archived-versions/AI Agent na blog 1.3.7 - DEBUG.json", "r", encoding="utf-8") as f:
    wf = json.load(f)

print("=== EXECUTION FLOW ===\n")

def trace(node_name, indent=0):
    prefix = "  " * indent
    print(f"{prefix}→ {node_name}")
    
    if node_name in wf["connections"] and "main" in wf["connections"][node_name]:
        for output_list in wf["connections"][node_name]["main"]:
            if output_list:
                for conn in output_list:
                    trace(conn["node"], indent + 1)

print("Starting from: Code JS add media content\n")
trace("Code JS add media content")

print("\n=== PROBLEM ===")
print("Code JS add media content má 3 výstupy:")
print("1. Generate image - Featured")
print("2. Generate image - Content") 
print("3. 🔄 Final Merge")
print("\nALE: Final Merge se spustí IHNED, zatímco Featured/Content média se ještě generují!")
print("ŘEŠENÍ: Final Merge musí čekat, až Send Media - Featured a Send Media - Content doběhnou")
