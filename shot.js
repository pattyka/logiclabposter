const puppeteer = require('puppeteer-core');
const path = require('path'), os = require('os');
const CHROME = path.join(os.homedir(),
  'Library/Caches/ms-playwright/chromium-1237/chrome-mac-arm64',
  'Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');
(async () => {
  const [url, out, w, h] = process.argv.slice(2);
  const b = await puppeteer.launch({ executablePath: CHROME, headless: true });
  const p = await b.newPage();
  await p.setViewport({ width: +w || 1780, height: +h || 1120, deviceScaleFactor: 1 });
  await p.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
  await p.evaluate(() => document.fonts.ready);
  const el = await p.$('.poster'); await el.screenshot({ path: out });
  await b.close();
  console.log('wrote', out);
})();
