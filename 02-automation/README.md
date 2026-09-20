# Módulo 2: QA Automation

Automatización de pruebas UI (E2E) y API.

## 🎭 Playwright + Python + pytest

Tests E2E sobre dos aplicaciones objetivo:

| Suite | App | Tests | Qué cubre |
|-------|-----|-------|-----------|
| [test_example.py](playwright/test_example.py) | example.com | 2 | Título, contenido, enlace |
| [tests/test_saucedemo.py](playwright/tests/test_saucedemo.py) | saucedemo.com | 8 | Login (±), inventario, carrito, checkout completo, reproducción de BUG-02, logout |

```bash
cd playwright
pytest -v                # corre los 10 tests
```

## 🔌 API Testing con Postman + Newman

Colección sobre [JSONPlaceholder](https://jsonplaceholder.typicode.com) — los 5 métodos CRUD:

| Request | Validaciones |
|---------|--------------|
| GET /posts | 200, 100 posts, estructura de cada uno, tiempo < 2s |
| GET /posts/1 | 200, estructura, id=1, title no vacío |
| POST /posts | 201, recurso creado con id=101 |
| PUT /posts/1 | 200, campos actualizados |
| DELETE /posts/1 | 200, respuesta objeto vacío |

```bash
newman run postman/collection.json -e postman/environment.json
```

**Resultado local:** 5/5 requests, 14/14 assertions ✅

## 🤖 CI

GitHub Actions corre ambas suites en cada push: Playwright (10 tests) + Newman (5 requests). Ver [workflow](../.github/workflows/test.yml).
