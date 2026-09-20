# BUG-03: Checkout acepta inyección HTML en campo Last Name (posible XSS)

| Campo | Valor |
|-------|-------|
| **ID** | BUG-03 |
| **Severidad** | Alta (seguridad) |
| **Prioridad** | Alta |
| **Módulo** | Checkout — Formulario de datos (Step One) |
| **Entorno** | Windows 11, Chrome, https://www.saucedemo.com (standard_user) |
| **Fecha** | 2026-09-20 |

## Pasos para reproducir
1. Iniciar sesión con standard_user y agregar un producto al carrito
2. Ir al carrito → **Checkout**
3. En First Name ingresar un nombre válido
4. En Last Name ingresar: `Beltran <script>alert(1)</script>`
5. En Zip/Postal Code ingresar un código válido
6. Hacer clic en **Continue**

## Resultado esperado
El formulario sanitiza o rechaza entradas con etiquetas HTML/script, mostrando un error de validación.

## Resultado actual
El formulario **acepta la cadena con `<script>` y avanza al Overview** sin error. El contenido se procesa sin sanitización aparente en el paso de revisión.

## Evidencia
- Campo llenado: `last-name` = `Beltran <script>alert(1)</script>`
- Tras clic en Continue: URL = `checkout-step-two.html`, error `[data-test=error]` ausente
- En una app real, si ese valor se renderiza sin escapar en alguna vista (historial de pedidos, email de confirmación, panel admin), la carga se ejecutaría (XSS almacenado).
## Notas
Clasificado como Alta por ser un patrón de seguridad, aunque en esta app demo el impacto real es limitado. El punto para la entrevista: identificar que la falta de validación de entrada es la causa raíz compartida con BUG-02 y BUG-04.
