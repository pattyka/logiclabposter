const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  try {
    console.log('🚀 PDF exportálás indítása...');
    const browser = await puppeteer.launch({
      headless: true
    });
    const page = await browser.newPage();
    
    // Betöltjük a helyi poster.html fájlt
    const filePath = 'file://' + path.resolve(__dirname, 'poster.html');
    console.log(`📂 Fájl betöltése: ${filePath}`);
    await page.goto(filePath, { waitUntil: 'networkidle0' });
    
    // Rákényszerítjük a screen megjelenítést, hogy a text-shadow és box-shadow elmosások (blur) tökéletesen kirajzolódjanak a PDF-ben is
    await page.emulateMediaType('screen');
    
    console.log('📄 PDF generálása (méretek a CSS-ből)...');
    await page.pdf({
      path: 'poster.pdf',
      preferCSSPageSize: true, // Ezzel megtartja a 95cm x 135cm méretet a CSS-ből!
      printBackground: true    // Megtartja a hátteret és a színeket
    });
    
    console.log('✅ Sikeres exportálás! A poszter elmentve: poster.pdf');
    await browser.close();
  } catch (error) {
    console.error('❌ Hiba történt a PDF exportálása közben:', error);
    process.exit(1);
  }
})();
