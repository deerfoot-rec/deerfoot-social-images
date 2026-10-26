"""Render an HTML post template to a 1080x1350 PNG.
Usage: python3 src/render.py <input.html> <output.png>
The HTML may reference ../assets/logo.svg or ../assets/icon.svg relatively."""
import asyncio, sys, pathlib
from playwright.async_api import async_playwright
async def main(src, out):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        await pg.goto(pathlib.Path(src).resolve().as_uri())
        await pg.wait_for_load_state('networkidle')
        await pg.evaluate('document.fonts.ready')
        await pg.screenshot(path=out)
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
