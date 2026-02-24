def test_prices_page_opens(page):
    page.goto("https://selectel.ru/prices/")

    assert "/prices" in page.url
    assert "Цены" in page.content()