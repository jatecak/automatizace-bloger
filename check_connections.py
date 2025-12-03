import json

with open("archived-versions/AI Agent na blog 1.3.7 - DEBUG.json", "r", encoding="utf-8") as f:
    wf = json.load(f)

print("=== CONNECTIONS TO FINAL MERGE ===\n")

# Najít všechny uzly, které mají output do Final Merge
for node_name, outputs in wf["connections"].items():
    if "main" in outputs:
        for output_list in outputs["main"]:
            if output_list:
                for conn in output_list:
                    if conn.get("node") == "🔄 Final Merge":
                        print(f"✓ {node_name} → Final Merge")

print("\n=== EXPECTED ===")
print("✓ Send Media - Featured → Final Merge")
print("✓ Send Media - Content → Final Merge")
print("✓ Code JS add media content → Final Merge")
