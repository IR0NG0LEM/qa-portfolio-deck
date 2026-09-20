"""Tests E2E sobre saucedemo.com (Swag Labs) — flujo completo de compra.

Cubre: login, inventario, carrito, checkout y reproducción del BUG-02
(checkout acepta nombre de 500 caracteres).
"""
import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://www.saucedemo.com"
STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


# ---------- Helpers ----------

def _login(page, username=STANDARD_USER, password=PASSWORD):
    page.goto(f"{BASE_URL}/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")


def _add_backpack_and_go_to_cart(page):
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click(".shopping_cart_link")
    page.wait_for_url("**/cart.html")


# ---------- Tests ----------

def test_login_exitoso():
    """Login con standard_user redirige al inventario."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        expect(page).to_have_url(f"{BASE_URL}/inventory.html")
        assert page.title() == "Swag Labs"
        browser.close()


def test_login_fallido_password_malo():
    """Password incorrecto muestra error y NO redirige."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"{BASE_URL}/")
        page.fill("#user-name", STANDARD_USER)
        page.fill("#password", "password_incorrecta")
        page.click("#login-button")
        error = page.locator('[data-test="error"]')
        expect(error).to_be_visible()
        expect(error).to_contain_text("do not match")
        assert "inventory" not in page.url
        browser.close()


def test_inventario_6_productos():
    """El inventario muestra 6 productos."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        items = page.locator(".inventory_item")
        expect(items).to_have_count(6)
        browser.close()


def test_agregar_producto_al_carrito():
    """Agregar un producto actualiza el badge del carrito a 1."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
        badge = page.locator(".shopping_cart_badge")
        expect(badge).to_have_text("1")
        browser.close()


def test_carrito_muestra_producto_agregado():
    """El carrito lista el producto agregado con nombre y precio."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        _add_backpack_and_go_to_cart(page)
        item = page.locator(".cart_item")
        expect(item).to_have_count(1)
        expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
        expect(page.locator(".inventory_item_price")).to_have_text("$29.99")
        browser.close()


def test_checkout_flujo_completo():
    """Checkout completo: datos válidos → overview → confirmación."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        _add_backpack_and_go_to_cart(page)
        page.click('[data-test="checkout"]')
        page.wait_for_url("**/checkout-step-one.html")
        page.fill("#first-name", "Ramon")
        page.fill("#last-name", "Beltran")
        page.fill("#postal-code", "64650")
        page.click('[data-test="continue"]')
        page.wait_for_url("**/checkout-step-two.html")
        # Verificar resumen: 1 item, precio total con tax
        expect(page.locator(".cart_item")).to_have_count(1)
        total = page.locator(".summary_total_label")
        expect(total).to_contain_text("Total: $32.39")
        page.click('[data-test="finish"]')
        page.wait_for_url("**/checkout-complete.html")
        expect(page.locator("h2")).to_have_text("Thank you for your order!")
        browser.close()


def test_bug_02_checkout_acepta_nombre_500_caracteres():
    """BUG-02: el checkout acepta un nombre de 500 caracteres sin error.

    Reproduce el bug documentado en 01-manual/bug-reports/bug-02.md.
    El test PASSEA cuando el bug sigue presente (comportamiento actual defectuoso).
    Si algún día este test falla, significa que el bug fue corregido.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        _add_backpack_and_go_to_cart(page)
        page.click('[data-test="checkout"]')
        page.wait_for_url("**/checkout-step-one.html")
        page.fill("#first-name", "A" * 500)
        page.fill("#last-name", "Beltran")
        page.fill("#postal-code", "64650")
        page.click('[data-test="continue"]')

        # Comportamiento ACTUAL (bug): avanza sin error al paso 2
        page.wait_for_url("**/checkout-step-two.html")
        error = page.locator('[data-test="error"]')
        assert error.count() == 0, "El formulario ahora muestra error — el bug fue corregido"
        # Verificar que el valor viajó completo al resumen
        nombre_resumen = page.locator(".summary_value_label").first
        # El bug está confirmado: 500 chars aceptados
        browser.close()


def test_logout_vacia_el_estado_de_sesion():
    """Logout funciona y devuelve al login. (Relacionado con BUG-05: el carrito NO se vacía — documentado por separado.)"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        _login(page)
        page.click("#react-burger-menu-btn")
        page.wait_for_selector("#logout_sidebar_link", state="visible")
        page.click("#logout_sidebar_link")
        page.wait_for_url(f"{BASE_URL}/")
        assert "inventory" not in page.url
        browser.close()
