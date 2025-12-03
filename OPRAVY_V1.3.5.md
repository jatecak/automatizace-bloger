# 🔧 KRITICKÉ OPRAVY - Verze 1.3.5

**Datum:** 3. prosince 2025  
**Problém:** Obrázky se nahrály do knihovny, ale **nepřiřadily k článku** a **neměly správná metadata**

---

## 🔴 ZJIŠTĚNÉ PROBLÉMY

### 1. Metadata obrázků se NEPOSÍLALA do WordPress
**Příznaky:**
- Název souboru: `obrazek-cont-7.webp` (místo klíčových slov)
- Alt text: prázdný
- Title: prázdný
- Featured image: nepřiřazen k článku
- Content image: nepřiřazen k článku

**Příčina:**
Uzly `Send Media - Featured` a `Send Media - Content` nahrávaly pouze binární data, ale **neposílaly query parametry** s metadaty (`alt_text`, `title`, `caption`).

---

### 2. Slabá extrakce klíčových slov
**Příznaky:**
- Keywords byly prázdné → fallback na `'obrazek'`
- Použití pouze prvního odstavce (málo textu)
- Minimální délka slov: 4 znaky (příliš restriktivní)
- Pouze 6 klíčových slov

**Příčina:**
- Extrakce z příliš malého množství textu
- Příliš přísná regex (`\p{L}{4,}`)
- Málo klíčových slov pro výběr

---

## ✅ IMPLEMENTOVANÉ OPRAVY

### Oprava 1: WordPress API query parametry
**Změněné uzly:** `Send Media - Featured`, `Send Media - Content`

**PŘED:**
```json
{
  "method": "POST",
  "url": "https://craftime.cz/wp-json/wp/v2/media",
  "sendHeaders": true,
  "sendBody": true,
  "contentType": "binaryData"
}
```

**PO:**
```json
{
  "method": "POST",
  "url": "https://craftime.cz/wp-json/wp/v2/media",
  "sendHeaders": true,
  "sendQuery": true,
  "queryParameters": {
    "parameters": [
      {
        "name": "alt_text",
        "value": "={{ $json.media?.alt || '' }}"
      },
      {
        "name": "title",
        "value": "={{ $json.media?.title || '' }}"
      },
      {
        "name": "caption",
        "value": "={{ $json.media?.alt || '' }}"
      }
    ]
  },
  "sendBody": true,
  "contentType": "binaryData"
}
```

**Výsledek:**
✅ Alt text se nastaví z `$json.media.alt`  
✅ Title se nastaví z `$json.media.title`  
✅ Caption se nastaví z `$json.media.alt`

---

### Oprava 2: Vylepšená extrakce klíčových slov
**Změněné uzly:** `Code JS - Featured`, `Code JS Prepare media meta`

**Změny:**
1. **Více textu:** Extrakce z prvních **3 odstavců** (místo 1)
2. **Kratší slova:** Regex `\p{L}{3,}` (místo `\p{L}{4,}`)
3. **Více keywords:** 10 slov (místo 6)
4. **Fallback na title:** Pokud nejsou keywords, použije se název článku
5. **Debug logging:** Console.log pro sledování procesu

**Nový kód:**
```javascript
// Extrakce prvních 3 odstavců
const paragraphs = html.match(/<p>([\s\S]*?)<\/p>/gi) || [];
const first3 = paragraphs.slice(0, 3)
  .map(p => p.replace(/<[^>]+>/g, ' ').replace(/<!--[\s\S]*?-->/g, ' '))
  .join(' ')
  .replace(/\s+/g, ' ')
  .trim();

// Extrakce klíčových slov (minimálně 3 znaky)
const words = (text.match(/\p{L}{3,}/gu) || []).filter(w => !stop.has(w));
const uniq = [...new Set(words)].slice(0, 10);
const keywords = uniq.join(', ');

// Fallback na title pokud keywords prázdné
let keywordSlug = keywords.normalize('NFD')...;
if (!keywordSlug || keywordSlug.length < 3) {
  keywordSlug = title.normalize('NFD')...;
}

const fileName = (keywordSlug || 'minecraft-obrazek') + '-feat.webp';
```

**Výsledek:**
✅ Více textu pro analýzu  
✅ Menší slova se zachytí (např. "mob", "pvp")  
✅ Lepší šance na relevantní keywords  
✅ Vždy existuje smysluplný název souboru

---

### Oprava 3: Debug logging
**Přidáno do všech Code JS uzlů:**

```javascript
console.log('=== Code JS - Featured DEBUG ===');
console.log('Title:', title);
console.log('First 3 paragraphs length:', first3.length);
console.log('Extracted keywords:', keywords);
console.log('Final fileName:', fileName);
console.log('Final alt:', alt);
```

**Účel:**
- Sledování procesu extrakce
- Diagnostika problémů
- Ověření správného toku dat

---

## 📊 OČEKÁVANÉ VÝSLEDKY

### Před opravou:
```
Název: obrazek-cont-7.webp
Alt text: (prázdné)
Title: (prázdné)
Featured media: nepřiřazen
```

### Po opravě:
```
Název: novinka-25w05a-změny-biomy-feat.webp
Alt text: Minecraft Snapshot 25w05a – Nové biomy a změny — novinka, změny, biomy, crafting, předměty
Title: Minecraft Snapshot 25w05a – Nové biomy a změny
Featured media: ✅ přiřazen (ID z Send Media - Featured)
Content image: ✅ vložen do článku
```

---

## 🔍 JAK OVĚŘIT OPRAVU

### 1. Spusť workflow v n8n
```
Klik na "Schedule Minecraft Blog" → Execute Node
```

### 2. Sleduj Console Log
V n8n Execution → Najdi uzly:
- `Code JS - Featured` → zkontroluj log
- `Code JS Prepare media meta` → zkontroluj log
- `Code JS add media content` → zkontroluj featured_media_id

### 3. Zkontroluj WordPress Media Library
```
WP Admin → Média → Najdi poslední 2 obrázky
```

**Měly by mít:**
- ✅ Název s klíčovými slovy (např. `novinka-snapshot-25w05a-feat.webp`)
- ✅ Alt text vyplněný
- ✅ Title vyplněný
- ✅ Caption vyplněný

### 4. Zkontroluj článek
```
WP Admin → Příspěvky → Poslední článek
```

**Měl by mít:**
- ✅ Featured image nastavený (náhledový obrázek)
- ✅ Obrázek v obsahu (mezi 1.-5. odstavcem)
- ✅ Správné alt texty u obrázků

---

## 🐛 TROUBLESHOOTING

### Problém: Název je stále "obrazek-..."
**Příčina:** Keywords jsou prázdné a fallback na title také selhal

**Řešení:**
1. Zkontroluj console log v uzlu `Code JS - Featured`
2. Zkontroluj, že `$json.title` obsahuje text
3. Zkontroluj, že `$json.content_html` obsahuje odstavce `<p>...</p>`

---

### Problém: Alt text je stále prázdný
**Příčina:** Query parametry se neodeslaly nebo `$json.media.alt` je prázdné

**Řešení:**
1. Zkontroluj uzel `Send Media - Featured` → měl by mít `sendQuery: true`
2. Zkontroluj output z `Code JS - Featured` → měl by obsahovat `media.alt`
3. Zkontroluj, že Merge správně spojil data

---

### Problém: Featured image není přiřazen
**Příčina:** `featured_media_id` není správně předáno do HTTP Request

**Řešení:**
1. Zkontroluj `Code JS add media content` → output by měl obsahovat `featured_media_id`
2. Zkontroluj `HTTP Request - priradit media` → měl by odesílat `featured_media`
3. Zkontroluj n8n Execution log pro tento uzel

---

## 📝 SHRNUTÍ ZMĚN

| Co | Před | Po |
|----|------|-----|
| **Send Media - Featured** | Bez query params | ✅ `alt_text`, `title`, `caption` |
| **Send Media - Content** | Bez query params | ✅ `alt_text`, `title`, `caption` |
| **Keywords extrakce** | 1 odstavec, 4+ znaky, 6 slov | ✅ 3 odstavce, 3+ znaky, 10 slov |
| **Fallback** | `'obrazek'` | ✅ `title` → `'minecraft-obrazek'` |
| **Debug logging** | Minimální | ✅ Kompletní |

---

## ✅ CHECKLIST PRO TESTOVÁNÍ

- [ ] Import upraveného JSON do n8n
- [ ] Spuštění testovacího běhu
- [ ] Kontrola console logů v Code JS uzlech
- [ ] Kontrola media library (názvy, alt texty)
- [ ] Kontrola článku (featured image, content image)
- [ ] Ověření, že vše funguje správně

---

**Verze:** 1.3.5  
**Status:** ✅ READY FOR TESTING  
**Další krok:** Testovací běh v n8n
