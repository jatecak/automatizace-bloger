# ⚡ QUICK REFERENCE - AI Agent na blog 1.3.4

## ✅ STATUS: PŘIPRAVENO K NASAZENÍ

---

## 🎯 PROVEDENÉ OPRAVY (6+2)

### Ověřené (již implementované):
1. ✅ RegEx `/wp:paragraph/g` - Code JS add media content
2. ✅ Detekce `item.json?.content?.raw` - Code JS add media content  
3. ✅ Čtení `content.raw` a `title.rendered` - Code JS add media content

### Nově opravené:
4. ✅ HTTP Request odesílá `content_html_updated` - správné přiřazení obsahu
5. ✅ Používá `bodyParameters` - optimalizace
6. ✅ Stop-slova aktualizována - Minecraft keywords (2× uzly)

### Bonusové optimalizace:
7. ✅ Název uzlu: `Schedule Minecraft Blog`
8. ✅ Gmail záloha bez `JSON.parse()`

---

## 📂 SOUBORY

```
/workspaces/automatizace-bloger/
├── AI Agent na blog 1.3.4 - craftime.cz (14).json      ← HLAVNÍ WORKFLOW (OPRAVENÝ)
├── AI Agent na blog 1.3.4 - craftime.cz (14).json.backup  ← ZÁLOHA
├── FINALNI_AUDIT.md                                     ← KOMPLETNÍ ANALÝZA
├── NAVOD_SPUSTENI.md                                    ← NÁVOD PRO JARDU
└── QUICK_REFERENCE.md                                   ← TENTO SOUBOR
```

---

## 🚀 JAK SPUSTIT (3 KROKY)

### 1. Import do n8n
```
n8n → Import from file → vybrat JSON → Save
```

### 2. Kontrola credentials (6×)
- AgentUploadCraftime (HTTP Basic Auth)
- Wordpress craftime.cz (WordPress API)
- OpenAi account (OpenAI API)
- Gmail - craftime.cz (Gmail OAuth2)
- webmail.cesky-hosting.cz (SMTP)

### 3. Testovací běh
```
Klik na uzel "Schedule Minecraft Blog" → Execute Node
```

---

## 📊 KLÍČOVÉ PARAMETRY

| Parametr | Hodnota |
|----------|---------|
| **Frekvence** | Ne, Út, Pá v 8:00 CET |
| **Délka článku** | ~1000 slov |
| **Featured image** | 660×370 px (webp) |
| **Content image** | 990×565 px (webp) |
| **WP kategorie** | ID: 15 |
| **WP autor** | ID: 3 |
| **Email notifikace** | jarda.majer@centrum.cz |
| **Email záloha** | jdemecraftit@gmail.com |

---

## 🔍 CO KONTROLOVAT PO PUBLIKACI

- [ ] Post je na `craftime.cz`
- [ ] Featured image přiřazen
- [ ] Content image vložen (1.-5. odstavec)
- [ ] Gutenberg bloky správné
- [ ] Meta description ≤ 155 znaků
- [ ] 2× emaily doručeny

---

## 🐛 RYCHLÉ ŘEŠENÍ PROBLÉMŮ

| Problém | Řešení |
|---------|--------|
| Obrázek se negeneroval | Zkontroluj OpenAI kredity, má retry 5× |
| Post bez featured media | Zkontroluj uzel "Send Media - Featured" |
| Email nepřišel | Ověř SMTP credentials |
| Špatný formát článku | Agent korektor má `onError: continueRegularOutput` |

---

## 📈 MONITORING

**První týden:**
- Kontroluj 3 publikace (Ne, Út, Pá)
- Ověř kvalitu článků
- Sleduj SEO metriky

**Měsíční:**
- OpenAI cost (∼$5-15/měsíc)
- Úspěšnost workflow (>90%)
- Návštěvnost článků

---

## 🎓 DALŠÍ KROKY

1. ✅ **Nyní:** Import do n8n a testovací běh
2. 📅 **Tento týden:** 3× manuální kontrola publikací
3. 📊 **Za měsíc:** Vyhodnocení SEO a návštěvnosti
4. 🔧 **Průběžně:** Optimalizace promptů podle výsledků

---

**Dokumentace:** `FINALNI_AUDIT.md` | **Návod:** `NAVOD_SPUSTENI.md`  
**Verze:** 1.3.4 | **Datum:** 3.12.2025 | **Status:** ✅ READY
