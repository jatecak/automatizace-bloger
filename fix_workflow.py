import json

with open("archived-versions/AI Agent na blog 1.3.7 - DEBUG.json", "r", encoding="utf-8") as f:
    wf = json.load(f)

print("=== OPRAVA: Odstranění přímého spojení Code JS → Final Merge ===\n")

# Najít connection z "Code JS add media content"
if "Code JS add media content" in wf["connections"]:
    main_outputs = wf["connections"]["Code JS add media content"]["main"]
    
    print(f"Před opravou: {len(main_outputs[0])} výstupů")
    
    # Odfiltrovat Final Merge
    filtered = [conn for conn in main_outputs[0] if conn["node"] != "🔄 Final Merge"]
    
    wf["connections"]["Code JS add media content"]["main"][0] = filtered
    
    print(f"Po opravě: {len(filtered)} výstupů\n")
    print("Odstraněno: Code JS add media content → 🔄 Final Merge")
    print("\nZůstalo:")
    for conn in filtered:
        print(f"  ✓ Code JS add media content → {conn['node']}")

# Uložit
with open("AI Agent na blog 1.3.8 - FINAL-FIX.json", "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

wf["name"] = "AI Agent na blog 1.3.8 - FINAL-FIX"

with open("AI Agent na blog 1.3.8 - FINAL-FIX.json", "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("\n✅ Vytvořen soubor: AI Agent na blog 1.3.8 - FINAL-FIX.json")
print("\n🔍 TEORIE:")
print("Final Merge nyní dostane data až když:")
print("  1. Send Media - Featured doběhne (pošle featured media ID)")
print("  2. Send Media - Content doběhne (pošle content media ID)")  
print("  3. n8n automaticky přidá post_id z Code JS (protože je v execution path)")
