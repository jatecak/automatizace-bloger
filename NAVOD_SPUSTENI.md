# 🚀 NÁVOD NA SPUŠTĚNÍ: AI Agent na blog - craftime.cz

## ✅ FINÁLNÍ KONTROLA PŘED SPUŠTĚNÍM

### 1. OVĚŘENÍ PŘIHLAŠOVACÍCH ÚDAJŮ V n8n

Ujisti se, že následující credentials jsou aktivní a správně nastavené:

- **AgentUploadCraftime** (HTTP Basic Auth) - pro nahrávání médií a aktualizaci postů
- **Wordpress craftime.cz** (WordPress API) - pro vytváření příspěvků
- **OpenAi account** (OpenAI API) - pro AI generování
- **Gmail - craftime.cz** (Gmail OAuth2) - pro zálohu článků
- **webmail.cesky-hosting.cz - jsem** (SMTP) - pro notifikace

---

## 📋 KROKY PRO SPUŠTĚNÍ WORKFLOW

### KROK 1: Import workflow do n8n
1. Otevři n8n
2. Klikni na **"Import from file"**
3. Vyber soubor: `AI Agent na blog 1.3.4 - craftime.cz (14).json`
4. Zkontroluj, že se všechny uzly načetly správně (žádné červené chyby)

### KROK 2: Kontrola Schedule
1. Najdi uzel **"Schedule Minecraft Blog"**
2. Ověř nastavení:
   - **Spouštění**: Neděle, Úterý, Pátek v 8:00
   - **Časová zóna**: Europe/Berlin (UTC+01:00)
3. Případně uprav podle potřeby

### KROK 3: Testovací spuštění
1. Klikni na uzel **"Schedule Minecraft Blog"**
2. Klikni **"Execute Node"** (malé šipka/play tlačítko)
3. Sleduj průběh v workflow:
   - ✅ RSS Read - načtení článků z Google News
   - ✅ Agent filtr - výběr relevantních Minecraft novinek
   - ✅ Agent osnovy - vytvoření struktury článku
   - ✅ Agent copywriter - napsání článku
   - ✅ Agent korektor - kontrola a úpravy
   - ✅ Vytvoř příspěvek - publikace na WordPress
   - ✅ Generate image - Featured & Content
   - ✅ HTTP Request - přiřazení médií
   - ✅ Odeslání emailu s notifikací

### KROK 4: Ověření výsledku
1. Zkontroluj email na `jarda.majer@centrum.cz` - měla přijít notifikace
2. Zkontroluj Gmail `jdemecraftit@gmail.com` - záloha článku
3. Otevři `https://craftime.cz/wp-admin/edit.php` - ověř, že post je publikován
4. Zkontroluj:
   - ✅ Náhledový obrázek (featured media) je přiřazen
   - ✅ Obrázek v obsahu je vložen mezi 1.-5. odstavcem
   - ✅ Gutenberg bloky jsou správně formátované

---

## 🔧 CO BYLO OPRAVENO (verze 1.3.4)

### ✅ Vyřešené problémy:

1. **RegEx pro konec odstavce** - opraveno na `/wp:paragraph/g`
2. **Čtení dat článku** - správná detekce `content.raw` a `title.rendered`
3. **Přiřazení obsahu** - HTTP Request správně odesílá `content_html_updated`
4. **Optimalizace HTTP** - používá `bodyParameters` místo `jsonParameters`
5. **Stop-slova** - aktualizována pro Minecraft (odstraněna: 'hra', 'svět', 'bloky'; přidána: 'minecraft', 'update', 'snapshot', 'java', 'bedrock', atd.)
6. **Název uzlu** - přejmenován z "Finanční Gramotnost" na "Minecraft Blog"
7. **Gmail záloha** - opraveno čtení dat z Code JS Style

---

## ⚙️ POKROČILÉ NASTAVENÍ

### Úprava frekvence publikování
V uzlu **"Schedule Minecraft Blog"**:
```
"triggerAtDay": [0, 2, 5]  // 0=Neděle, 2=Úterý, 5=Pátek
"triggerAtHour": 8         // Hodina spuštění
```

### Úprava kategorie WordPress
V uzlu **"Vytvoř příspěvek"**:
```
"categories": [15]  // ID kategorie v WordPress
```

### Úprava autorství
V uzlu **"Vytvoř příspěvek"**:
```
"authorId": 3  // ID autora v WordPress
```

---

## 🐛 ŘEŠENÍ PROBLÉMŮ

### Workflow selže v uzlu "Generate image"
**Příčina**: Nedostatek kreditů OpenAI nebo rate limit  
**Řešení**: 
- Zkontroluj zůstatek na OpenAI účtu
- Nastavení v uzlu má `retryOnFail: true` a `maxTries: 5`

### Obrázek se nevloží do obsahu
**Příčina**: Content Media se negeneroval (chyba AI)  
**Řešení**:
- Workflow pokračuje i bez Content Media (IF podmínka)
- Zkontroluj output uzlu "Generate image - Content"

### Post se vytvoří, ale bez featured media
**Příčina**: Featured Media se nenahrálo nebo ID není správně předáno  
**Řešení**:
- Zkontroluj uzel "Send Media - Featured" - měl by vrátit `id`
- Ověř uzel "Code JS add media content" - měl by mít `featured_media_id`

### Email notifikace nepřišla
**Příčina**: SMTP credentials vypršely  
**Řešení**:
- Zkontroluj credentials "webmail.cesky-hosting.cz - jsem"
- Ověř správnost emailové adresy `jarda.majer@centrum.cz`

---

## 📊 MONITORING

### Co sledovat:
1. **Úspěšnost generování** - % úspěšných běhů workflow
2. **Kvalita článků** - kontrola prvních 3-5 publikací
3. **SEO metadata** - správnost meta description (max 155 znaků)
4. **Obrázky** - relevance k tématu, rozměry, alt texty
5. **Gutenberg formátování** - správné bloky a styling

---

## 📞 KONTAKT PRO PODPORU

Pokud narazíš na problém:
1. Zkontroluj **Execution Log** v n8n (červená ikonka u uzlu)
2. Ověř **Error Details** - pravý panel v n8n
3. Prověř **WordPress Error Log** pokud problém souvisí s publikací

---

## 🎯 OČEKÁVANÉ VÝSLEDKY

- **Frekvence**: 3× týdně (Ne, Út, Pá v 8:00)
- **Délka článku**: ~1000 slov
- **Obrázky**: 2× (Featured 660x370, Content 990x565)
- **Čas zpracování**: ~5-10 minut na článek
- **Kategorie**: Minecraft novinky, snapshoty, updaty

---

**Verze workflow:** 1.3.4  
**Poslední aktualizace:** 3.12.2025  
**Status:** ✅ PŘIPRAVENO K PRODUKČNÍMU NASAZENÍ
