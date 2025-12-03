# 🤖 Automatizace Blogeru - AI Agent pro craftime.cz

Automatický generátor Minecraft článků pomocí n8n a AI agentů.

## 📋 Přehled

Tento projekt obsahuje n8n workflow, které:
- 🔍 Denně monitoruje Minecraft novinky z Google News
- 🤖 Filtruje relevantní témata pomocí AI
- ✍️ Generuje kvalitní české články (~1000 slov)
- 🖼️ Vytváří DALL-E obrázky ve stylu Minecraftu
- 📰 Publikuje přímo na WordPress (craftime.cz)
- 📧 Odesílá notifikace a zálohy

**Frekvence:** 3× týdně (Neděle, Úterý, Pátek v 8:00)

---

## 🚀 Rychlý start

```bash
# 1. Stáhni soubor
git clone https://github.com/jatecak/automatizace-bloger.git

# 2. Importuj do n8n
# n8n → Import from file → vybrat "AI Agent na blog 1.3.4 - craftime.cz (14).json"

# 3. Nastav credentials (6 různých služeb)

# 4. Spusť testovací běh
```

📖 **Podrobný návod:** [NAVOD_SPUSTENI.md](NAVOD_SPUSTENI.md)

---

## 📁 Struktura projektu

```
automatizace-bloger/
├── AI Agent na blog 1.3.4 - craftime.cz (14).json    ← Hlavní workflow (v1.3.7)
├── OPRAVA_KOMPLETNI.md        ← ✅ ZAČNI TADY - Stručný návod k testování
├── DIAGNOZA_PROBLEMU.md       ← Detailní vysvětlení oprav v1.3.7
├── QUICK_FIX_v137.md          ← Vizuální diagramy a debug checklist
├── FINALNI_AUDIT.md           ← Kompletní technická analýza
├── NAVOD_SPUSTENI.md          ← Návod krok za krokem (původní)
├── QUICK_REFERENCE.md         ← Rychlá reference
└── README.md                  ← Tento soubor
```

---

## 🆕 NEJNOVĚJŠÍ ZMĚNY - v1.3.7 (3. prosince 2024)

### ✅ OPRAVENO: Přiřazování obrázků k článkům

**Problém:** Obrázky se nahrávaly do WordPress Media Library, ale nepřiřazovaly se k článkům.

**Řešení:** Přidán uzel **🔄 Final Merge**, který spojuje:
- Featured Media ID (náhledový obrázek)
- Content Media ID (obrázek do obsahu)
- Post ID (ID vytvořeného článku)

**Výsledek:** ✅ Náhledové obrázky se nyní přiřazují ✅ Obrázky se vkládají do obsahu článků

📖 **Podrobnosti:** [OPRAVA_KOMPLETNI.md](OPRAVA_KOMPLETNI.md)

---

## ✅ Verze 1.3.4 - Co je opraveno

### Potvrzené opravy:
- ✅ RegEx pro konec odstavce: `/wp:paragraph/g`
- ✅ Správné čtení WordPress dat: `content.raw` a `title.rendered`
- ✅ HTTP Request optimalizace: `bodyParameters` místo `jsonParameters`

### Nové opravy:
- ✅ Přiřazení obrázku do obsahu článku
- ✅ Aktualizace stop-slov pro Minecraft
- ✅ Oprava názvu uzlů a Gmail zálohy

**Detaily:** [FINALNI_AUDIT.md](FINALNI_AUDIT.md)

---

## 🛠️ Technologie

- **n8n** - Workflow automation
- **OpenAI GPT-4.1** - Generování textu
- **OpenAI DALL-E 3** - Generování obrázků
- **WordPress REST API** - Publikace
- **Google News RSS** - Zdroj novinek
- **Gmail/SMTP** - Notifikace

---

## 📊 Klíčové parametry

| Parametr | Hodnota |
|----------|---------|
| Frekvence | 3× týdně (Ne, Út, Pá) |
| Čas spuštění | 8:00 CET |
| Délka článku | ~1000 slov |
| Obrázky | 2× (Featured 660×370, Content 990×565) |
| Formát | Gutenberg bloky |
| Kategorie WP | ID: 15 |

---

## 📧 Kontakt

**Autor:** Jarda  
**Email:** jarda.majer@centrum.cz  
**Web:** [craftime.cz](https://craftime.cz)

---

## 📄 Licence

Tento projekt je určen pro interní použití na craftime.cz.

---

**Verze:** 1.3.4 | **Datum:** 3.12.2025 | **Status:** ✅ Production Ready
