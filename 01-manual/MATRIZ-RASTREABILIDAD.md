# Matriz de Trazabilidad — Requerimientos → Pruebas

Mapea cada requerimiento funcional con sus casos de prueba manuales (TC-XX), tests automatizados (Playwright), requests de API (Postman/Newman) y pruebas de performance (k6).

**Criterio de estado:**
- ✅ **Cubierto** — tiene cobertura manual Y automatizada (o API/performance verificada en CI)
- ⚠️ **Parcial** — cubierto en una sola capa
- ❌ **No cubierto** — sin cobertura

---

## App 1: example.com (sitio informativo)

| REQ | Requerimiento | TC Manual | Automatizado | Performance | Estado |
|-----|---------------|-----------|--------------|-------------|--------|
| REQ-01 | La página muestra el título "Example Domain" | [TC-01](test-cases/test-case-01.md) | `test_example_domain_title` | — | ✅ |
| REQ-02 | La página muestra H1 y texto descriptivo correctos | [TC-02](test-cases/test-case-02.md), [TC-03](test-cases/test-case-03.md) | `test_example_domain_title` | — | ✅ |
| REQ-03 | La página contiene el enlace "Learn more" a iana.org | [TC-04](test-cases/test-case-04.md) | `test_example_domain_has_learn_more_link` | — | ✅ |
| REQ-04 | El sitio sirve por HTTPS con certificado válido | [TC-05](test-cases/test-case-05.md) | — | — | ⚠️ |
| REQ-05 | El servidor responde HTTP 200 | [TC-06](test-cases/test-case-06.md) | — | k6: check `status is 200` (290/290) | ✅ |
| REQ-06 | Tiempo de respuesta < 2 segundos | [TC-07](test-cases/test-case-07.md) | — | k6: threshold `p(95)<2000` (64ms) | ✅ |
| REQ-07 | Visualización responsive en 3 viewports | [TC-08](test-cases/test-case-08.md) | — | — | ⚠️ |
| REQ-08 | HTML estructuralmente válido | [TC-09](test-cases/test-case-09.md) | — | — | ⚠️ |
| REQ-09 | Comportamiento definido al entrar por HTTP | [TC-10](test-cases/test-case-10.md) | — | — | ⚠️ |

## App 2: saucedemo.com — Swag Labs (e-commerce)

| REQ | Requerimiento | TC Manual | Automatizado | Bug vinculado | Estado |
|-----|---------------|-----------|--------------|---------------|--------|
| REQ-10 | Login exitoso con credenciales válidas | — | `test_login_exitoso` | — | ⚠️ |
| REQ-11 | Login rechazado con credenciales inválidas | — | `test_login_fallido_password_malo` | — | ⚠️ |
| REQ-12 | El inventario muestra 6 productos | — | `test_inventario_6_productos` | — | ⚠️ |
| REQ-13 | Agregar producto actualiza el badge del carrito | — | `test_agregar_producto_al_carrito` | — | ⚠️ |
| REQ-14 | El carrito muestra el producto agregado con nombre y precio | — | `test_carrito_muestra_producto_agregado` | — | ⚠️ |
| REQ-15 | Checkout completo hasta confirmación de orden | — | `test_checkout_flujo_completo` | — | ⚠️ |
| REQ-16 | El checkout valida formato y longitud de los datos de entrada | Exploración manual (evidencia DOM) | `test_bug_02_checkout_acepta_nombre_500_caracteres` | [BUG-02](bug-reports/bug-02.md), [BUG-03](bug-reports/bug-03.md), [BUG-04](bug-reports/bug-04.md) | ✅ |
| REQ-17 | Logout cierra la sesión correctamente | — | `test_logout_vacia_el_estado_de_sesion` | [BUG-05](bug-reports/bug-05.md) | ⚠️ |

## API: JSONPlaceholder (jsonplaceholder.typicode.com)

| REQ | Requerimiento | Request API | Estado |
|-----|---------------|-------------|--------|
| REQ-18 | Leer la lista completa de posts (GET /posts) | `GET /posts` (Newman, 4 assertions) | ✅ |
| REQ-19 | Leer un post específico (GET /posts/1) | `GET /posts/1` (Newman, 3 assertions) | ✅ |
| REQ-20 | Crear un post (POST /posts) | `POST /posts` (Newman, 2 assertions) | ✅ |
| REQ-21 | Actualizar un post (PUT /posts/1) | `PUT /posts/1` (Newman, 2 assertions) | ✅ |
| REQ-22 | Eliminar un post (DELETE /posts/1) | `DELETE /posts/1` (Newman, 2 assertions) | ✅ |

---

## 📊 Cobertura

| Métrica | Valor |
|---------|-------|
| **Total de requerimientos** | 22 |
| ✅ Cubiertos (multi-capa) | 11 |
| ⚠️ Parciales (una capa) | 11 |
| ❌ No cubiertos | 0 |
| **Cobertura completa** | **50%** |
| **Cobertura con al menos una capa** | **100%** |

### Gaps identificados (próximos pasos)

1. **saucedemo sin TCs manuales formales** (REQ-10 a REQ-15, REQ-17): los flujos están automatizados y verificados en CI, pero no tienen casos de prueba manuales documentados previos. La evidencia manual existe como bug reports (exploración), no como diseño de casos.
2. **REQ-04, REQ-07, REQ-08, REQ-09 (example.com)**: solo manuales — certificado SSL, responsive, validación HTML y comportamiento HTTP no están automatizados.

*Matriz generada el 2026-09-20. Todas las referencias apuntan a artefactos existentes en este repo.*
