from playwright.sync_api import sync_playwright

def get_total():
    total_sum = 0
    base_url = "https://exam.sanand.workers.dev/seed/{}"
    seeds = range(23, 33)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for seed in seeds:
            url = base_url.format(seed)
            page.goto(url, wait_until="networkidle")

            # Select all <td> elements
            td_elements = page.query_selector_all("table td")
            for td in td_elements:
                text = td.inner_text().strip()
                if text.isdigit():
                    total_sum += int(text)

        browser.close()

    return total_sum

if __name__ == "__main__":
    total = get_total()
    print(f"sum: {total}")
