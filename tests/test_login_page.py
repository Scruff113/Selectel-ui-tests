def test_login_page_opens(page):
    response = page.goto("https://my.selectel.ru/login")

    assert response.status == 200

    assert "login" in page.url