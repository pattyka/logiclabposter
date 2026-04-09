# Saját Firebase Adatbázis Beállítása

Jelenleg az e-mailek elmentése a mentésem által biztosított konfigurációra támaszkodik. Hogy a saját fiókodba gyűljenek az e-mailek és a csomagválasztások, létre kell hoznod egy saját "Firebase" projektet a Google-nél (teljesen ingyenes).

Itt van lépésről lépésre, hogyan csináld meg, és mit kell nekem elküldened a végén:

## 1. Firebase Projekt létrehozása
1. Nyisd meg a [Firebase Console](https://console.firebase.google.com/)-t és jelentkezz be a Google fiókoddal.
2. Kattints a **"Add project"** (Projekt hozzáadása) gombra.
3. Adj neki egy nevet (pl. `LogicLab Kids`).
4. A Google Analytics bekapcsolását kérdezi: hagyd bekapcsolva, és válaszd ki a már meglévő GA4 fiókodat, amit ehhez csináltál!
5. Kattints a **"Create project"** gombra és várd meg amíg végez.

## 2. Web App regisztrálása
1. A projekt áttekintő (Overview) oldalán látsz középen egy **`</>`** (Web) ikont. Kattints rá.
2. Adj meg egy app nevet (pl. `Website`). A "Firebase Hosting" bepipálása **nem** szükséges (hiszen GitHub Pages-t használsz).
3. Kattints a **"Register app"** gombra.
4. Meg fog jelenni a **Firebase SDK snippet**. Itt találod azt a "config" kódot, ami nekem kell! Ezt másold ki! (Később is megtalálható a Settings > General alatt).

## 3. Firestore Adatbázis létrehozása (Ide jönnek az e-mailek)
1. A bal oldali menüben válaszd ki a **"Firestore Database"**-t a "Build" (Fejlesztés) fül alatt.
2. Kattints a **"Create database"** gombra.
3. Válaszd a **"Start in test mode"** (Tesztelési mód) lehetőséget (hogy azonnal lehessen írni bele), majd menj tovább.
4. Válassz egy európai szerver lokációt (pl. `eur3 (Europe)`), és hozd létre.

## MIT KELL ELKÜLDENED NEKEM?
Ahhoz, hogy átírjam a weboldalad kódját a te saját adatbázisodra, csak is oszd meg az **"firebaseConfig"** objektumot, amit a 2. lépésben kaptál.

Valahogy így fog kinézni, ezt másold be ide a chatbe:
```javascript
const firebaseConfig = {
  apiKey: "AIzaSyB...",
  authDomain: "logiclab-kids.firebaseapp.com",
  projectId: "logiclab-kids",
  storageBucket: "logiclab-kids.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdefg",
  measurementId: "G-0106KW4DEW"
};
```

Amint ezt elküldöd, én beleteszem a kódba, deployolok, és onnantól kezdve 100%-ban nálad landolnak az e-mailek és az "intent of payment" adatok!
