# Módulo 1: QA Manual

En este módulo se documentan los casos de prueba, matrices de ejecución y reportes de errores (bugs).

## 📋 Documentación

- [Test Plan](test-plan.md) — Objetivo, alcance y criterios del ciclo de pruebas

## 🧪 Test Cases (example.com)

| ID | Título | Tipo | Prioridad | Resultado |
|----|--------|------|-----------|-----------|
| [TC-01](test-cases/test-case-01.md) | Verificar título de la página | Funcional | Alta | ✅ PASS |
| [TC-02](test-cases/test-case-02.md) | Verificar encabezado principal H1 | Funcional / UI | Alta | ✅ PASS |
| [TC-03](test-cases/test-case-03.md) | Verificar texto descriptivo del dominio | Funcional | Media | ✅ PASS |
| [TC-04](test-cases/test-case-04.md) | Verificar enlace Learn more | Funcional | Alta | ✅ PASS |
| [TC-05](test-cases/test-case-05.md) | Verificar HTTPS con certificado válido | Seguridad | Alta | ✅ PASS |
| [TC-06](test-cases/test-case-06.md) | Verificar respuesta HTTP 200 | Funcional | Alta | ✅ PASS |
| [TC-07](test-cases/test-case-07.md) | Verificar tiempo de carga < 2s | Performance | Media | ✅ PASS |
| [TC-08](test-cases/test-case-08.md) | Verificar visualización responsive | UI | Media | ✅ PASS |
| [TC-09](test-cases/test-case-09.md) | Verificar estructura HTML válida | Estructural | Baja | ✅ PASS |
| [TC-10](test-cases/test-case-10.md) | Verificar comportamiento con HTTP | Seguridad | Media | ✅ PASS |

## 🐞 Bug Reports (saucedemo.com — Swag Labs)

| ID | Título | Severidad | Prioridad |
|----|--------|-----------|-----------|
| [BUG-01](bug-reports/bug-01.md) | Producto 'Backpack' descrito como 'Sly Pack' (inconsistencia de contenido) | Baja | Baja |
| [BUG-02](bug-reports/bug-02.md) | Checkout acepta nombre de 500 caracteres sin límite | Media | Media |
| [BUG-03](bug-reports/bug-03.md) | Checkout acepta inyección HTML en Last Name (posible XSS) | Alta | Alta |
| [BUG-04](bug-reports/bug-04.md) | Checkout acepta código postal de solo símbolos | Media | Media |
| [BUG-05](bug-reports/bug-05.md) | El carrito persiste después del logout | Media | Alta |

*Todos los bugs fueron reproducidos y verificados manualmente el 2026-09-20 con evidencia del DOM y flujo real.*

## 📝 Próximos pasos
- Matriz de trazabilidad
