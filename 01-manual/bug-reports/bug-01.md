# BUG-01: Inconsistencia de contenido: producto 'Backpack' descrito como 'Sly Pack'

| Campo | Valor |
|-------|-------|
| **ID** | BUG-01 |
| **Severidad** | Baja (cosmético) |
| **Prioridad** | Baja |
| **Módulo** | Inventario — Detalle de producto |
| **Entorno** | Windows 11, Chrome, https://www.saucedemo.com (standard_user) |
| **Fecha** | 2026-09-20 |

## Pasos para reproducir
1. Iniciar sesión en saucedemo.com con standard_user
2. Observar la tarjeta del primer producto del inventario
3. Comparar el **nombre** del producto con su **descripción**

## Resultado esperado
El nombre del producto y la descripción refieren al mismo artículo de forma consistente.

## Resultado actual
El producto se llama **Sauce Labs Backpack** ($29.99) pero su descripción lo nombra como **'Sly Pack'**: *"carry.allTheThings() with the sleek, streamlined Sly Pack..."*. El cliente no sabe si compra un Backpack o un Sly Pack.

## Evidencia
- Nombre extraído del DOM: `Sauce Labs Backpack`
- Descripción extraída del DOM: `carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.`
- Hallazgo relacionado: el producto *Sauce Labs Fleece Jacket* usa el archivo de imagen `sauce-pullover-1200x1500-BfbI-PSd.jpg` (el asset se llama 'pullover' para un producto 'jacket').
## Notas
Ambas inconsistencias provienen de la misma extracción de datos del inventario (6 productos). No afectan funcionalidad pero dañan la confianza del usuario en el catálogo.
