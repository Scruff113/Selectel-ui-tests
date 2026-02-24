def test_navigation_to_prices(page):
    page.goto("https://selectel.ru/")

    page.get_by_role("link", name="Цены").first.click()

    assert "/prices" in page.url
    assert "Цены" in page.content()