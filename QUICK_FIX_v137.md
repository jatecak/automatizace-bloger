# 🎯 QUICK FIX REFERENCE - v1.3.7

## PŘESNÝ PROBLÉM

```
❌ HTTP Request četl:
   URL: /posts/{{ $('Code JS add media content').item.json.post_id }}
   
   → ALE uzel "Code JS add media content" už nebyl v execution flow!
   → post_id = undefined
   → WordPress API chyba: "Invalid post ID"
```

## ŘEŠENÍ

```
✅ HTTP Request nyní čte:
   URL: /posts/{{ $json.post_id }}
   
   → Čte z AKTUÁLNÍHO inputu (z Final Merge uzlu)
   → post_id = 123 (správně)
   → WordPress API: OK, článek 123 aktualizován
```

## TOK DAT (VIZUÁLNĚ)

### PŘED (nefungující):

```
┌─────────────────┐
│ Vytvoř příspěvek│
│   (ID: 123)     │
└────────┬────────┘
         │
         v
┌─────────────────────────┐
│ Code JS add media       │
│ (uloží post_id: 123)    │
└──┬──────────────────────┘
   │
   ├──> Generate Featured -> Send Media (456)
   │                            │
   └──> Generate Content -> Send Media (789)
                                │
                                v
                          ┌──────────────────┐
                          │ HTTP Request     │
                          │ ❌ post_id: ???  │ <- Nemá odkud číst!
                          │ ❌ media: ???    │
                          └──────────────────┘
```

### PO (fungující):

```
┌─────────────────┐
│ Vytvoř příspěvek│
│   (ID: 123)     │
└────────┬────────┘
         │
         v
┌───────────────────────────┐
│ Code JS add media         │
│ Output:                   │
│ - post_id: 123            │
│ - content_html: "..."     │
└──┬──────────┬─────────────┘
   │          │             │
   │          │             └────────────────┐
   │          │                              │
   v          v                              v
Generate   Generate                    ┌──────────┐
Featured   Content                     │          │
   │          │                         │          │
   v          v                         │          │
Send Media Send Media                   │  Final   │
(456)      (789)                        │  Merge   │ <- NOVÝ!
   │          │                         │          │
   └────┬─────┘                         │          │
        │                               │          │
        └───────────────────────────────>          │
                                        └─────┬────┘
                                              │
                                              v
                                    ┌─────────────────┐
                                    │ HTTP Request    │
                                    │ ✅ post_id: 123 │
                                    │ ✅ media: 456   │
                                    │ ✅ content: ... │
                                    └─────────────────┘
```

## CO FINAL MERGE DĚLÁ

```javascript
// Vstup 1: Send Media - Featured
{
  "id": 456,
  "slug": "keywords-feat",
  "source_url": "https://..."
}

// Vstup 2: Send Media - Content
{
  "id": 789,
  "slug": "keywords-cont",
  "source_url": "https://..."
}

// Vstup 3: Code JS add media content
{
  "post_id": 123,
  "content_html_updated": "<html>...</html>",
  "featured_media_id": null  // Ještě se nenahrál
}

↓↓↓ MERGE ↓↓↓

// Output pro HTTP Request:
{
  "post_id": 123,           // Z vstupu 3
  "featured_media": 456,    // Z vstupu 1
  "content": "<html>        // Z vstupu 3 + vložený obrázek z vstupu 2
    ...
    <img class='wp-image-789' ...>
    ...
  </html>"
}
```

## TESTOVÁNÍ - CHECKLIST

### 1. Před spuštěním
- [ ] Workflow importován do n8n
- [ ] Credentials správně nastaveny
- [ ] Console output viditelný

### 2. Během běhu - sleduj console
```
✅ Očekáváš vidět:
   "Post ID: 123"
   "Featured Media ID: null" (před nahráním)
   "✓ Featured Media ID: 456" (po nahrání)
   "✓ Content Media ID: 789" (po nahrání)
   "Post ID: 123" (před HTTP Request)
```

### 3. Po dokončení - zkontroluj WordPress
- [ ] Článek existuje (wp-admin/posts)
- [ ] Má náhledový obrázek (Featured Image)
- [ ] Obrázek je v obsahu článku
- [ ] Soubory mají správné názvy (ne obrazek-cont-7.webp)
- [ ] Média mají alt text a title

### 4. Pokud stále nefunguje
```bash
# Zkontroluj execution log v n8n:
1. Otevři Executions
2. Najdi poslední běh
3. Klikni na "🔄 Final Merge" uzel
4. Zkontroluj Input Data - měly by být 3 items
5. Zkontroluj Output - měl by být post_id + featured_media
```

## NEJČASTĚJŠÍ CHYBY

| Symptom | Příčina | Řešení |
|---------|---------|--------|
| post_id: undefined | Final Merge nedostává data z Code JS | Zkontroluj connection |
| featured_media: 0 | Send Media - Featured selhalo | Zkontroluj DALL-E API |
| Obrázek není v content | Regex nenašel odstavce | Zkontroluj HTML format |
| WordPress API error 400 | Špatný post_id formát | Zkontroluj $json.post_id |

---

**Pro podporu:** Zkontroluj DIAGNOZA_PROBLEMU.md pro detaily
