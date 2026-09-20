# BUG-02: Checkout acepta nombre de 500 caracteres sin límite de longitud

| Campo | Valor |
|-------|-------|
| **ID** | BUG-02 |
| **Severidad** | Media |
| **Prioridad** | Media |
| **Módulo** | Checkout — Formulario de datos (Step One) |
| **Entorno** | Windows 11, Chrome, https://www.saucedemo.com (standard_user) |
| **Fecha** | 2026-09-20 |

## Pasos para reproducir
1. Iniciar sesión con standard_user y agregar un producto al carrito
2. Ir al carrito y hacer clic en **Checkout**
3. En First Name ingresar 500 caracteres (`A` × 500)
4. En Last Name ingresar un apellido válido
5. En Zip/Postal Code ingresar un código válido
6. Hacer clic en **Continue**

## Resultado esperado
El formulario rechaza entradas con longitud irrazonable (ej. máximo 50 caracteres por campo) mostrando un mensaje de error.

## Resultado actual
El formulario **acepta los 500 caracteres y avanza a la pantalla de Overview** (checkout-step-two) sin ningún mensaje de error. Los datos viajan tal cual al resumen de compra.

## Evidencia
- Campo llenado: `first-name` = 500 caracteres 'A' (verificado: `value.length = 500`)
- Tras clic en Continue: URL cambió a `checkout-step-one.html` → `checkout-step-two.html`
- Elemento de error `[data-test=error]`: ausente — ningún mensaje mostrado
