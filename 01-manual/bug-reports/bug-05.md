# BUG-05: El carrito persiste después de cerrar sesión (logout no limpia el estado)

| Campo | Valor |
|-------|-------|
| **ID** | BUG-05 |
| **Severidad** | Media |
| **Prioridad** | Alta |
| **Módulo** | Sesión / Carrito de compras |
| **Entorno** | Windows 11, Chrome, https://www.saucedemo.com (standard_user) |
| **Fecha** | 2026-09-20 |

## Pasos para reproducir
1. Iniciar sesión con standard_user
2. Agregar un producto al carrito (ej. Sauce Labs Backpack) — el badge muestra **1**
3. Abrir el menú (esquina superior izquierda) y hacer clic en **Logout**
4. Volver a iniciar sesión con el mismo usuario
5. Observar el badge del carrito

## Resultado esperado
Al cerrar sesión, el carrito se vacía (o al menos el usuario espera empezar limpio). El badge no debería mostrar productos de una sesión anterior.

## Resultado actual
Tras logout + re-login, **el badge del carrito sigue mostrando 1** — el producto agregado antes del logout sigue en el carrito. El estado de sesión no se limpia al cerrar.

## Evidencia
- Secuencia verificada: login → add-to-cart → badge **1** → logout (URL vuelve a `/`) → login → badge **1** (persistente)
- El carrito sobrevive al ciclo completo de sesión, lo que indica que se almacena sin vincularse al ciclo de vida de la sesión.
