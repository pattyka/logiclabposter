# LogicLab Kids: GA4 Tracking Guide

> Measurement ID: **G-E8W35XPSZN**

---

## Beépített események (automatikusan működnek)

Az alábbi események már be vannak építve a kódba és automatikusan tüzelnek.

### 1. `cta_click` - CTA gomb kattintás
Tüzel: amikor valaki rákattint bármely "Próbáld ki" / "Ingyenes próba" gombra.

| Paraméter | Értékek | Mit jelent |
|---|---|---|
| `cta_source` | `hero`, `navbar`, `mobile_bottom` | Melyik gomb lett megnyomva |

**Miért fontos**: Megmutatja, melyik CTA konvertál legjobban. Ha a `mobile_bottom` dominál, a mobil alsó sáv jól működik.

### 2. `plan_selected` - Csomag kiválasztás
Tüzel: amikor valaki rákattint egy csomagra a pricing szekcióban.

| Paraméter | Értékek | Mit jelent |
|---|---|---|
| `plan_type` | `free`, `monthly`, `yearly` | Kiválasztott csomag |
| `intent_of_payment` | `true` / `false` | Fizetési szándék (true = havi vagy éves) |

**Miért fontos**: Ha valaki a `free`-ről átvált `monthly`-ra vagy `yearly`-re, az INTENT OF PAYMENT. Ez a legfontosabb metrika a traction bizonyításához.

### 3. `checkout_click` - Checkout gomb kattintás
Tüzel: amikor a "Próbáld ki" / "Ingyenes próba indítása" gomb megnyomódik a pricing szekcióban.

| Paraméter | Értékek | Mit jelent |
|---|---|---|
| `plan_type` | `free`, `monthly`, `yearly` | Kiválasztott csomag a kattintáskor |
| `intent_of_payment` | `true` / `false` | Fizetési szándék |
| `source` | `cssabafinal_hu` | Oldal azonosító |

### 4. `waitlist_signup` - Email megadás (KONVERZIÓ)
Tüzel: amikor valaki sikeresen megadja az email címét.

| Paraméter | Értékek | Mit jelent |
|---|---|---|
| `plan_type` | `free`, `monthly`, `yearly` | Választott csomag |
| `intent_of_payment` | `true` / `false` | Fizetési szándék |
| `email_domain` | pl. `gmail.com` | Email domain |

**Ez a legfontosabb esemény.** Egy `waitlist_signup` ahol `intent_of_payment = true` azt jelenti: ez az ember **fizet is hajlandó lenne**.

---

## GA4 Beállítás lépésről lépésre

### 1. lépés: Nyisd meg a GA4 dashboardot

1. Menj ide: [analytics.google.com](https://analytics.google.com)
2. Válaszd ki a **G-E8W35XPSZN** property-t

### 2. lépés: Ellenőrizd, hogy jönnek az események

1. Bal oldali menü > **Reports** > **Realtime**
2. Nyisd meg az oldalt egy másik böngészőfülön
3. Kattints a gombokra, és nézd a Realtime riportban, hogy megjelennek-e az események

### 3. lépés: Egyéni események megtekintése

1. Bal menü > **Reports** > **Engagement** > **Events**
2. Itt látod az összes eseményt: `cta_click`, `plan_selected`, `checkout_click`, `waitlist_signup`
3. Kattints bármelyikre a részletekért

### 4. lépés: Jelöld meg a `waitlist_signup`-ot KONVERZIÓNAK

1. Bal menü > **Admin** (fogaskerék ikon alul)
2. **Data display** > **Events**
3. Keresd meg a `waitlist_signup` eseményt
4. Kapcsold be a **"Mark as key event"** (korábbi nevén "Mark as conversion") gombot

Ez után a konverziós riportokban is megjelenik.

---

## Intent of Payment mérése

### Hogyan nézd meg, hányan akarnak fizetni?

#### GA4-ben:
1. **Reports** > **Engagement** > **Events**
2. Kattints a `plan_selected` eseményre
3. Az esemény részleteinél keresd az `intent_of_payment` paramétert

#### Firebase-ben (pontosabb):
1. Menj a [Firebase Console](https://console.firebase.google.com)-ra
2. **Firestore Database** > `kids-waitlist` kollekció
3. Szűrd a dokumentumokat `plan` mező szerint:
   - `plan = "monthly"` vagy `plan = "yearly"` → **fizetési szándék**
   - `plan = "free"` → érdeklődő, de nem fizető szándékú

#### Traction riport sablonhoz:
```
Összesen feliratkozók:          X fő
Ebből fizetési szándékkal:      Y fő (Y/X = Z%)
   - Havi csomag választók:     A fő
   - Éves csomag választók:     B fő
```

---

## Custom Explorations (haladó)

### Free-to-Paid funnel

Ha azt akarod látni, hányan váltanak free-ről paid-re egy sessionön belül:

1. **Explore** > **Funnel exploration** (bal menü)
2. Add hozzá ezeket a lépéseket:
   - Step 1: `plan_selected` WHERE `plan_type` = `free`
   - Step 2: `plan_selected` WHERE `intent_of_payment` = `true`
   - Step 3: `waitlist_signup`

### CTA Teljesítmény összehasonlítás

1. **Explore** > **Free form**
2. Rows: `cta_source` (event parameter)
3. Values: Event count
4. Így látod, melyik gomb hoz a legtöbb kattintást

---

## Egyéni Dimenziók regisztrálása

A GA4-ben az egyéni event paraméterekat regisztrálni kell, hogy a riportokban megjelenjenek:

1. **Admin** > **Data display** > **Custom definitions**
2. Kattints **Create custom dimension**
3. Add hozzá ezeket:

| Dimension neve | Event parameter | Scope |
|---|---|---|
| Plan Type | `plan_type` | Event |
| Intent of Payment | `intent_of_payment` | Event |
| CTA Source | `cta_source` | Event |
| Email Domain | `email_domain` | Event |

> **FONTOS**: Az adatok az egyéni dimenziók létrehozása UTÁN gyűlt adatokra vonatkoznak. Tehát ezt minél hamarabb csináld meg!

---

## Összefoglaló: Milyen számokat mutathatsz?

| Metrika | Hol nézd | Amit mutat |
|---|---|---|
| Látogatók száma | GA4 > Reports > Overview | Hányan jönnek az oldalra |
| CTA kattintások | GA4 > Events > `cta_click` | Hányan érdeklődnek |
| Plan váltás free→paid | GA4 > Events > `plan_selected` | Intent of payment |
| Email feliratkozás | GA4 > Events > `waitlist_signup` | Aktív érdeklődők |
| Fizetési szándék % | Firebase > kids-waitlist (plan != free) | Traction bizonyítás |
