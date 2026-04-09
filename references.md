# LogicLab Kids | Landing Page Reference

> Ez a dokumentum azt tartalmazza, hogy mi történt eddig a projektben, mi az oldal célja, milyen technológiák és fájlok vannak használatban, és mit kell tudni egy új AI-nak ahhoz, hogy folytassa a munkát.

---

## ⚠️ FONTOS SZABÁLY: SOHA NE HASZNÁLJ EM DASH-T (—)

Az em dash karakter (—) TILTOTT ebben a projektben. Sem a HTML tartalomban, sem a CSS-ben, sem a markdown dokumentumokban. Helyette használj:
- Pontot és új mondatot
- Vesszőt
- Kettőspontot
- Pontosvesszőt
- Vagy egyszerűen fogalmazd át a mondatot

---

## Projekt összefoglaló

A **LogicLab Kids** egy edukációs mobil alkalmazás 8–14 éves gyerekeknek, ami a kritikus gondolkodást fejleszti. A projekt webes marketing landing page-ét a `cssabafinal` mappa tartalmazza. Az oldal célja: szülőknek bemutatni a terméket és e-mail listára feliratkoztatni őket (waitlist), mivel az app még nem elérhető.

---

## Fájlstruktúra

```text
/ (Repository gyökérkönyvtár)
├── index.html                  ← Főoldal (landing page)
├── kids-shared.css             ← Közös CSS (stílusok, változók, responsive)
├── kids-shared.js              ← Közös JS (téma váltás, animációk, modal, Firebase waitlist)
├── firebase-config.js          ← Firebase Firestore konfiguráció (feliratkozók mentése)
├── Logo.png                    ← Világos módú logó
├── AppIconDark.png             ← Sötét módú logó / favicon
├── references.md               ← EZ A FÁJL (dokumentáció)
├── ga4-tracking-guide.md       ← Részletes útmutató a Google Analytics eseményekről
├── FIREBASE_SETUP.md           ← Útmutató az adatbázis beállításához
└── apple-iphone-15-pro-blue-titanium-mockup-3/   ← iPhone mockup képek
    ├── App normal/             ← 5 kép: főoldal, jutalom aktiválás, profil
    │   ├── Unknown-27-portrait.png   (Főoldal: napi kérdés + jutalom képernyőidő 140p)
    │   ├── Unknown-28-portrait.png   (Jutalom aktiválás modal: 10 perc választó)
    │   ├── Unknown-37-portrait.png   (Profil: szint, eredmények, pontok)
    │   ├── Unknown-39-portrait.png   (Profil: eredmények lista, badge-ek)
    │   └── Unknown-48-portrait.png   (Főoldal: napi kérdés + jutalom 210p)
    └── Course/                 ← 8 kép: edzés képernyők, nyomozás
        ├── Unknown-29-portrait.png   (Edzés főoldal: "Gondolkodj mélyebben", Sherlock kihívás)
        ├── Unknown-30-portrait.png   (Sherlock: nyomok+gyanúsítottak listázva, választás)
        ├── Unknown-35-portrait.png   (Nyomozás: gyanúsítottak kizárás, gondolkodj kérdés)
        ├── Unknown-36-portrait.png   (Ügy lezárva: +50 pont, megoldás)
        ├── Unknown-38-portrait.png   (Profil alap: eredmények + statisztikák + szülői zóna)
        ├── Unknown-41-portrait.png   (Lecke lista: leckék + progress)
        ├── Unknown-44-portrait.png   (Lecke részlet / folyamat)
        └── Unknown-45-portrait.png   (Lecke kezelés / beállítások)
```

---

## Amit eddig csináltunk (lépések)

### 1. Eredeti állapot
- Az oldal egy hosszú, szöveges, emotion-driven sales page volt (magyar nyelven).
- Nem tartalmazott semmilyen app mockupot/képet.
- A layout szöveg-alapú volt (hero, narrative, prose, checkout), vizuálisan szürke, képek nélkül.

### 2. Mockup mappa felfedezése
- A `cssabafinal/apple-iphone-15-pro-blue-titanium-mockup-3/` mappa tartalmaz **iPhone 15 Pro Blue Titanium** mockupokat az app különböző képernyőiről.
- **App normal** (5 kép): főoldal, jutalom rendszer, profil/eredmények
- **Course** (8 kép): edzés módok, Sherlock nyomozás kihívás, ügy lezárva, profil statisztikák, lecke lista

### 3. Landing page átalakítás (2026-04-09)
Az oldalt **teljesen átalakítottuk** Superhuman.com-stílusú modern landing page-re:

#### Design döntések:
- **Referencia**: [superhuman.com](https://superhuman.com) stílusú: nagy hero, feature showcase szekciók, mockup képek, interstitial statement, statisztikák, CTA
- **Sticky navbar**: LogicLab logó + "Próbáld ki" CTA gomb
- **Hero szekció**: nagy cím, alcím, CTA gomb, alatta 3 telefon mockup fan-elrendezésben (enyhe forgatás, hover animáció)
- **Trust bar**: MIT kutatás, napi 15 perc, korosztály, stb.
- **Feature showcase szekciók**: alternáló kétoszlopos layout (szöveg | kép, kép | szöveg), mindegyik egy-egy app feature-t mutat be mockupokkal
- **Big statement szekciók**: nagy betűs kijelentések
- **3 oszlopos feature grid**: I, II, III, az app 3 fő funkciója
- **Statisztikák sor**: 15 perc/nap, 8–14 év, 4 terület, ∞ kihívás
- **Checkout szekció**: bal oldal szöveges pitch, jobb oldal árazás (havi €9.99, éves €79, 34% kedvezmény)
- **Info strip**: alul háromoszlopos (probléma, megoldás, amit te látsz)
- **Modal**: e-mail cím megadás Firebase waitlistre (Firestore-ba menti)

#### Animációk:
- **Scroll reveal** (`lp-reveal`): elemek felfelé csúsznak és megjelennek, amikor a viewportba kerülnek (Intersection Observer)
- **Staggered reveal** (`lp-reveal-children`): gyerekelemek késleltetett megjelenése
- **Hero animáció**: badge, cím, alcím, CTA, telefonok, egymás után 0.2s-es késleltetéssel (`@keyframes lpFadeUp`)
- **Telefon hover**: scale + translateY effekt
- **Smooth scroll**: anchor linkek smooth scroll viselkedéssel

#### Technikai részletek:
- A `kids-shared.js` módosítva: `initTheme()` most `prefers-color-scheme` media query-t használ alapértelmezettként (nem idő-alapú)
- A CSS a `<style>` tag-ben van az index.html-ben, a landing page specifikus stílusok nem kerültek a shared CSS-be
- A `kids-shared.css` tartalmazza az alap változókat (színek, tipográfia, dark mode, modal, stb.)
- A `kids-shared.js` tartalmazza a téma váltást, scroll animációkat, pricing selection logikát, modal/checkout, Firebase waitlist mentést
- Nav logó theme-toggle: az `index.html`-ben egy extra script figyeli a `body.dark-mode` class változásokat és frissíti a nav logót
- A page magyar nyelvű (lang="hu")

### 4. Finomhangolás (2026-04-09, 2. kör)

#### Módosítások:
- **Mockup border eltávolítás**: az összes iPhone mockup képről levettük a `border-radius` és `box-shadow` CSS-t, így a mockup képek "tisztán", keret nélkül jelennek meg (a kép maga tartalmazza az iPhone keretet)
- **Logó theme toggle**: a navbar-ban lévő LogicLab logóra kattintva dark/light mode váltás történik (fade ki, class toggle, fade be animáció), ugyanúgy mint az eredeti oldalon
- **Böngésző alapértelmezett téma**: a `kids-shared.js` `initTheme()` funkciója átalakítva. Az idő-alapú (este 7 után sötét) helyett a `prefers-color-scheme: dark` media query-t használja, tehát a felhasználó OS/böngésző beállítását követi
- **"Ingyenes próba" gomb, modal**: a hero szekció "Ingyenes próba" és a navbar "Próbáld ki" gombok közvetlenül megnyitják az email-bekérő modalt (nem görgetnek le az árazás szekcióhoz)
- **Érintett fájlok**: `index.html` (CSS + HTML + inline script), `kids-shared.js` (initTheme)

### 5. Tartalmi és UX fejlesztés (2026-04-09, 3. kör)

#### Módosítások:
- **Em dash eltávolítás**: az összes em dash karakter (—) eltávolítva a teljes index.html-ből és references.md-ből. Szabály rögzítve: SOHA NE HASZNÁLJ EM DASH-T ebben a projektben.
- **Dark mode kontraszt javítás**: 
  - Trust bar span opacity 0.3-ról 0.55-re növelve, dark mode-ban 0.6-ra
  - Showcase visual háttér: dark mode-ban `rgba(255, 255, 255, 0.04)` (fehéres tónus), light mode-ban `rgba(42, 42, 42, 0.03)` (sötétes tónus). Így mindkét módban olvasható.
- **Képernyőidő feature kiemelés (KILLER FEATURE)**: 
  - A hero szekció szövege átalakítva: "Tanul. Gondolkodik. Képernyőidőt nyer."
  - A képernyőidő jutalom feature átkerült az 1. showcase pozícióra (közvetlenül a trust bar után)
  - Részletes leírás a képernyőidő jutalomról: a gyerek tanulással képernyőidőt szerez, nem kell veszekedni a telefonért, a gyerek organikusan motiválja magát, létfontosságú appok (telefon, üzenetküldő, térkép) sosem tiltottak
  - Új statement szekció: "Ne vedd el a telefont. Add hozzá az okot."
- **Szülői vélemények (testimonials) szekció hozzáadása**: 
  - 3 fiktív szülői idézet kártyákon (Kriszta, Gergő, Réka)
  - Csillag értékelés, szöveg, és név/leírás
  - Responsive: 3 oszlop > 1 oszlop mobilon
- **Lista bullet csere**: az em dash (—) helyett középső pont (·) a showcase feature listákban
- **Szekció sorrend**: 1. Képernyőidő (killer), 2. Statement, 3. Napi kérdés, 4. Sherlock, 5. AI statement, 6. Features grid, 7. Profil, 8. Stats, 9. Ügy lezárva, 10. Agy izom statement, 11. Testimonials, 12. Checkout
- **Érintett fájlok**: `index.html`, `references.md`

### 6. Szövegezés finomhangolása (2026-04-09, 4. kör)

#### Módosítások:
- **Hero**: "Az AI kényelmessé teszi a gondolkodást. Mi újra formába hozzuk." + "A LogicLab Kids visszaadja azokat a kognitív képességeket, amelyeket az algoritmusok leépítenek."
- **Képernyőidő szekció**: "Vége a képernyőidő körüli csatáknak" + részletes bullet pontok (Jutalom alapú haladás, Testreszabott kontroll, Biztonság, Belső motiváció)
- **Napi kérdés**: "Gondolkodás, ami napi rutinná válik" + új leírás az AI rávezető szerepéről
- **Sherlock**: "Élesítsd az elmét nyomozással" + "Interaktív detektívtörténetek..."
- **Három pillér**: "Napi 15 perc mentális tréning", "AI Vitapartner", "Tudatos tartalomfogyasztás" + új leírások
- **Záró CTA**: "Az elme olyan, mint egy izom. Ne hagyd ellustulni." + "Nem tilthatod ki az AI-t..."
- **Testimonials finomítás**: Kriszta ("TikTokot pörgetné", "feszültség"), Gergő ("rossz zsaru", "reggeleinket")
- **Probléma/Megoldás**: MIT kutatási adatai + "tornáztatja az érvelési és logikai képességeket"
- **Globális**: "gyereked" helyett "gyermeked" az egész oldalon
- **Érintett fájlok**: `index.html`

### 7. Mobil optimalizálás (2026-04-09, 5. kör)

#### Módosítások:
- **3 responsive breakpoint** hozzáadva (korábban 2 volt):
  - **Tablet (max 900px)**: egyoszlopos showcase, kisebb heading, tömörebb spacing, statement min-height auto
  - **Telefon (max 600px)**: kompakt nav, kisebb betűk, teljes szélességű CTA gomb (flex-direction: column), 2x2 stats grid, tömörebb testimonial kártyák, csökkentett paddinok, kisebb showcase képek
  - **Kis telefon (max 400px)**: még kisebb headingek és mockup képek
- **Touch-friendly gombok**: teljes szélességű CTA gomb mobilon
- **Trust bar**: kisebb font és spacing mobilon
- **Érintett fájlok**: `index.html`

### 8. Apple 2022 lekerekített sarkok (2026-04-09, 6. kör)

#### Módosítások:
- **Design rendszer**: Apple 2022 squircle stílusú lekerekített sarkok az egész oldalon:
  - Nav logó: `border-radius: 22.37%` (iOS app ikon arány)
  - Nav CTA gomb: `12px`
  - Hero CTA gomb: `14px`
  - Showcase visual háttér: `24px` + `margin: 2rem` (lebegő kártya hatás)
  - Plan option kártyák: `14px`
  - Checkout gomb: `14px`
  - Plan badge: `6px`
  - Testimonial kártyák: `16px`
  - Modal dialog: `20px`
  - Email input: `12px` (teljes border, nem csak alul)
  - Modal submit gomb: `14px`
- **Érintett fájlok**: `index.html`, `kids-shared.css`

### 9. Lekerekítés finomhangolás (2026-04-09, 7. kör)

#### Módosítások:
- Minden border-radius csökkentve (túl extrém volt):
  - Nav logó: `22.37%` > `10px`
  - Nav CTA: `12px` > `8px`
  - Hero CTA, Plan, Checkout btn: `14px` > `10px`
  - Testimonial: `16px` > `10px`
  - Showcase visual: `24px` > `16px`
  - Plan badge: `6px` > `4px`
  - Modal: `20px` > `16px` (kids-shared.css)
  - Email input, Modal submit: `12px`/`14px` > `8px`/`10px` (kids-shared.css)
- **Érintett fájlok**: `index.html`, `kids-shared.css`

### 10. Mobil alsó CTA sáv + scroll viselkedés (2026-04-09, 8. kör)

#### Módosítások:
- **Mobil bottom bar** (`.lp-mobile-bottom-bar`): fix alsó sáv "Próbáld ki" gombbal, csak mobilon (max 600px)
  - Frosted glass háttér, dark mode támogatás
  - A navbar "Próbáld ki" gomb elrejtve mobilon (`display: none`), helyette az alsó sáv
- **Scroll-based show/hide**: IntersectionObserver logika:
  - Rejtett amíg a hero "Ingyenes próba" CTA gomb látható (oldal teteje)
  - Megjelenik amint legörgetsz (0.4s fade-in + slide-up animáció)
  - Eltűnik amint a "Válassz csomagot" (pricing, `#pricing`) szekció megjelenik
  - Ugyanez a logika a desktop navbar "Próbáld ki" gombjára is
- **Érintett fájlok**: `index.html`, `kids-shared.js`

### 11. Teljes navbar scroll viselkedés (2026-04-09, 9. kör)

#### Módosítások:
- A teljes `.lp-nav` navbar rejtett az oldal tetején és az alján (pricing szekció)
- Csak a köztük lévő tartalom görgetésekor jelenik meg
- Animáció: `translateY(-100%)` > `translateY(0)` + `opacity` 0.4s transition
- Mindkét eszközön (desktop + mobil) azonos viselkedés
- **Érintett fájlok**: `index.html`

### 12. Ingyenes próba opció + intent of payment (2026-04-09, 10. kör)

#### Módosítások:
- **Új plan opció**: "Ingyenes próbaidőszak" hozzáadva az első helyre a pricing szekcióban
  - "7 nap / ingyen" + "Bankkártya nem szükséges"
  - Alapértelmezetten kiválasztva (`selected` class + `selectedPlan = 'free'`)
- **Dinamikus gomb szöveg**: 
  - Free kiválasztva: "PRÓBÁLD KI"
  - Havi/Éves: "INGYENES PRÓBA INDÍTÁSA"
- **Guard eltávolítva**: a gomb mindig megnyitja az email modalt, akkor is ha nincs terv kiválasztva (default: free)
- **Cél**: Intent of payment mérése. A Firebase waitlistbe mentett adatokból meg lehet állapítani, hányan akarják aktívan megvenni az appot (plan mező: free/monthly/yearly)
- **Korosztály frissítés**: 8-14 > 7-14 éves kor az egész oldalon (user manuális módosítás)
- **Érintett fájlok**: `index.html`, `kids-shared.js`

### 13. GA4 Tracking integráció (2026-04-09, 11. kör)

#### Módosítások:
- **GA Measurement ID csere**: G-D5VXHDLRWJ > G-0106KW4DEW
- **Tracking események beépítve** (`kids-shared.js` + `index.html`):
  - `cta_click`: CTA gomb kattintás, `cta_source` paraméterrel (hero/navbar/mobile_bottom)
  - `plan_selected`: csomag kiválasztás, `plan_type` + `intent_of_payment` paraméterekkel
  - `checkout_click`: checkout gomb, `plan_type` + `intent_of_payment` + `source`
  - `waitlist_signup`: email megadás, `plan_type` + `intent_of_payment` + `email_domain`
- **Intent of payment**: `intent_of_payment = true` ha a user havi vagy éves csomagot választott (nem free)
- **Guide**: `ga4-tracking-guide.md` létrehozva a teljes GA4 beállítási útmutatóval
- **GitHub deploy**: `csabagabor21/LogicLabWebsite` repóba pusholva, csak cssabafinal tartalom a root-ban
- **Érintett fájlok**: `index.html`, `kids-shared.js`, `ga4-tracking-guide.md`

### 14. UI Polish: Selection, Scrollbar, Mobile fontnagyság, Dot fix (2026-04-09, 12. kör)

#### Módosítások:
- **Custom text selection highlight**: 
  - Világos mód: sötét háttér, krém szöveg
  - Sötét mód: krém háttér, sötét szöveg
  - `::selection` + `::-moz-selection` (Firefox kompatibilitás)
- **Custom scrollbar**: 
  - Vékony, kerekített, brand-színű thumb
  - Hover effekt (`--hover-color`)
  - Firefox: `scrollbar-color` + `scrollbar-width: thin`
  - Webkit: `::-webkit-scrollbar-thumb` 8px, 10px border-radius
- **Mobil font méret növelés** (max 600px):
  - Hero h1: 1.8rem > 2rem
  - Hero sub, Showcase p, Statement p, Subline, Info p: 0.92rem > 1rem
  - Showcase h2: 1.5rem > 1.6rem, Statement h2: 1.6rem > 1.7rem
  - Feature p: 0.88rem > 0.95rem, Feature li: 0.85rem > 0.95rem
  - Testimonial text: 0.92rem > 1rem
  - Trust span: 0.6rem > 0.65rem
  - Plan info h3: 0.9rem > 0.95rem
  - Összes line-height: 1.5 > 1.6 (jobb olvashatóság)
- **Plan option dot fix** (`.plan-option.selected::before`):
  - Desktop: `top: 1rem` > `top: 50%; transform: translateY(-50%)` (vertikálisan középre igazítva)
  - Mobil: extra left padding (2rem) a dot-nak + kisebb dot méret (6px)
- **Érintett fájlok**: `index.html`

### 15. Plan selection color inversion + Mobile bar blur (2026-04-09, 13. kör)

#### Módosítások:
- **Plan option kiválasztás**: dot indicator eltávolítva, helyette teljes szín inverziót kap:
  - Háttér: `var(--text-color)`, szöveg: `var(--bg-color)`
  - Plan badge is invertálódik (bg/text csere)
  - Subtitle opacity 0.6 kiválasztott állapotban
  - Automatikusan működik light/dark mode-ban
- **Mobil bottom bar blur**: opacity 0.92 > 0.85 (megegyezik a navbar-ral)
  - Dark mode is frissítve
- **Érintett fájlok**: `index.html`

### 16. Repository konszolidáció és végső simítások (2026-04-09)

#### Módosítások:
- **Root mappa struktúra**: A `cssabafinal` és egyéb almappák törölve lettek, immár minden fájl (HTML, JS, CSS) a repó gyökérkönyvtárában található a GitHub Pages maximális kompatibilitása érdekében.
- **Saját Firebase Adatbázis**: Beállítottuk a user saját Firebase projektjét (`logiclab-kids-290f5`). A Firestore Security Rules `write-only` módba lett állítva a maximális adatvédelem érdekében. 
- **Bővített adatgyűjtés**: Amikor egy felhasználó feliratkozik, az email mellett az eszköze (userAgent) és a pontos lokációja (Timezone és IP alapú ország/város) is elmentésre kerül a Firestore DB-be. Beépült egy XSS biztonsági szűrés is az e-mail megjelenítéséhez a felugró ablakban.
- **Általános "Intent of Payment"**: Minden CTA kattintás generalizált havi (Monthly) szándéknak, vagy egyszerűen fizetési szándéknak (`intent_of_payment = true`) minősül a Google Analytics mérések kiszolgálása miatt, még az Ingyenes csomag is.
- **Mobil Tap Highlight fix**: Kikapcsolva az iOS Safari idegesítő kék kijelölési villogása gombnyomáskor (`-webkit-tap-highlight-color: transparent`), így sokkal native-alkalmazásosabb az érzet mobiltelefonon.
- **Záró copy finomhangolások**: 
  - A `<title>` "Képernyőidő bűntudat nélkül"-re lett módosítva.
  - A modal popup szövege marketingesebb ("Hamarosan érkezünk!").
  - A Testimonial szekció átalakult egy erősen probléma-központú, pre-launch empátia blokká, ahol a szülők a gyakori problémákat (telefonos hisztik, iPad reflexek, gondolkodás hiány) fogalmazzák meg, nem magát az appot értékelik. A csillagok eltávolítva.
- **Érintett fájlok**: `index.html`, `kids-shared.js`, `kids-shared.css`, mappastruktúra

---

## Fontos változók (CSS)

```css
--color-cream: #EFE3C7;       /* Világos háttér */
--color-dark: #2a2a2a;         /* Sötét szöveg / sötét mód háttér */
--font-main: "Times New Roman", Times, serif;
--faint-line: rgba(42, 42, 42, 0.2);  /* Halvány elválasztó vonalak */
--faint-bg: rgba(42, 42, 42, 0.05);   /* Enyhén tónusos háttér */
```

Dark mode automatikusan a böngésző/OS `prefers-color-scheme` beállítása szerint indul, vagy manuálisan a logóra kattintva váltható.

---

## Firebase (Firestore waitlist)

- Kollekció: `kids-waitlist`
- Dokumentum ID formátum: `{source}_{email}` (pl. `cssabafinal_hu_john@example.com`)
- Mezők: `email`, `plan`, `source`, `lang`, `timestamp`

---

## Jövőbeli teendők / fejlesztési ötletek

- [ ] Angol nyelvű verzió (index-en.html vagy language switcher)
- [ ] Valódi szülői vélemények beszerzése a fiktívek helyett
- [ ] Video demó szekció (screen recording az appból)
- [ ] App Store / Google Play gombok, amikor az app elérhető
- [ ] A/B teszt különböző hero üzenetekkel
- [ ] SEO optimalizáció: Open Graph meta tag-ek, Twitter card
- [ ] Performance: képek optimalizálása (WebP formátum, lazy loading már van)
- [ ] Parallax vagy más scroll effektek a mockupoknál
- [ ] Cookie consent banner
- [ ] FAQ szekció hozzáadás
- [ ] Blog / tartalom marketing integráció

---

## Hogyan dolgozz ezzel az oldallal

1. **A gyökérkönyvtárban dolgozz**, nincsenek almappák (kivéve a képeket).
2. **SOHA ne használj em dash-t (—)** semmilyen fájlban
3. A stílusokat lehetőleg az `index.html` `<style>` blokkjában tartsd, vagy ha megosztott, `kids-shared.css`-ben
4. A JS logika a `kids-shared.js`-ben van. Ha módosítod, az összes oldal érintett lehet
5. Az oldal statikus HTML, nem használ build tool-t. Egyszerűen megnyitható böngészőben
6. A mockup képek az `apple-iphone-15-pro-blue-titanium-mockup-3/` mappában vannak, relatív útvonallal hivatkozva
