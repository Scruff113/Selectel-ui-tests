def test_home_page_has_email(page):
    page.goto("https://selectel.ru")

    assert "selectel" in page.title().lower()
    assert page.get_by_text("sales@selectel.ru").first.is_visible()