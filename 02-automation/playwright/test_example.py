"""
Test de ejemplo para el QA Portfolio.
Verifica que Playwright funciona correctamente.
"""
from playwright.sync_api import sync_playwright, expect


def test_example_domain_title():
    """Verifica que example.com tiene el título correcto."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        
        # Verificar título
        expect(page).to_have_title("Example Domain")
        
        # Verificar que existe el heading h1
        heading = page.locator("h1")
        expect(heading).to_have_text("Example Domain")
        
        browser.close()


def test_example_domain_has_learn_more_link():
    """Verifica que example.com tiene el enlace 'Learn more'."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        
        # Verificar enlace "Learn more"
        link = page.locator("a")
        expect(link).to_have_text("Learn more")
        expect(link).to_have_attribute("href", "https://iana.org/domains/example")
        
        browser.close()


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
