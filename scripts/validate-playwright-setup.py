from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.set_content("""
        <html>
            <head>
                <title>Playwright Test OK</title>
            </head>
            <body>
                <h1>Hello Playwright</h1>
            </body>
        </html>
    """)

    print(page.title())
    print(page.locator("h1").inner_text())

    browser.close()