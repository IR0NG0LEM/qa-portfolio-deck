# BUG-04: Checkout acepta código postal compuesto solo de símbolos

| Campo | Valor |
|-------|-------|
| **ID** | BUG-04 |
| **Severidad** | Media |
| **Prioridad** | Media |
| **Módulo** | Checkout — Formulario de datos (Step One) |
| **Entorno** | Windows 11, Chrome, https://www.saucedemo.com (standard_user) |
| **Fecha** | 2026-09-20 |

## Pasos para reproducir
1. Iniciar sesión con standard_user y agregar un producto al carrito
2. Ir al carrito → **Checkout**
3. Ingresar First Name y Last Name válidos
4. En Zip/Postal Code ingresar: `!!!!!????`
5. Hacer clic en **Continue**

## Resultado esperado
El campo valida el formato del código postal (ej. 5 dígitos para EE.UU.) y rechaza entradas no numéricas con un mensaje de error.

## Resultado actual
El formulario **acepta `!!!!!????` como código postal válido** y avanza al Overview de la compra.

## Evidencia
- Campo llenado: `postal-code` = `!!!!!????` (solo símbolos)
- Tras clic en Continue: URL = `checkout-step-two.html`, sin error visible
- El único caso donde muestra error es con el campo **vacío** (ej. 'Error: Last Name is required') — la validación existente es solo de presencia, no de formato.
