/**
 * Exports each poster to its own print-ready PDF at true physical size.
 *
 * Sizes come from each file's own `@page { size: ... }` rule via
 * preferCSSPageSize, so P1/P3 land at 70x100 cm and P2 at 170x100 cm
 * without a magic number in here.
 *
 * Uses the Chrome for Testing already on disk (Playwright's cache), so
 * nothing needs downloading. Run:  node export-posters-pdf.js
 */
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');
const os = require('os');

const CHROME = path.join(
  os.homedir(),
  'Library/Caches/ms-playwright/chromium-1237/chrome-mac-arm64',
  'Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
);

const OUT_DIR = path.resolve(__dirname, 'pdf');

const POSTERS = [
  { src: 'poster_1.html', out: 'LogicLabKids_P1_Introduction_70x100.pdf' },
  { src: 'poster_2.html', out: 'LogicLabKids_P2_ExperimentalAndMethod_170x100.pdf' },
  { src: 'poster_3.html', out: 'LogicLabKids_P3_ResultsAndConclusion_70x100.pdf' },
];

(async () => {
  if (!fs.existsSync(CHROME)) {
    console.error('Chrome for Testing not found at:\n  ' + CHROME);
    process.exit(1);
  }
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true });

  for (const { src, out } of POSTERS) {
    const page = await browser.newPage();
    // served over http so the relative images and Google Fonts both resolve
    await page.goto(`http://localhost:8899/${src}`, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);

    const target = path.join(OUT_DIR, out);
    await page.pdf({
      path: target,
      preferCSSPageSize: true,   // honours each poster's own @page size
      printBackground: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 },
    });

    const mb = (fs.statSync(target).size / 1024 / 1024).toFixed(1);
    console.log(`${out}  (${mb} MB)`);
    await page.close();
  }

  await browser.close();
  console.log('\nwritten to ' + OUT_DIR);
})();
