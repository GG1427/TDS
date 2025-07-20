import asyncio
from playwright.async_api import async_playwright

seeds = range(23, 33)

async def run():
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for seed in seeds:
            url = f"https://exam.sanand.workers.dev/seed/{seed}"
            await page.goto(url)
            tables = await page.query_selector_all("table")
            for table in tables:
                text = await table.inner_text()
                numbers = [int(s) for s in text.split() if s.isdigit()]
                total += sum(numbers)
        print(f"Total sum across all seeds: {total}")
        await browser.close()

asyncio.run(run())
