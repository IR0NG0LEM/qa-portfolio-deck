# TC-05: Verificar carga por HTTPS con certificado válido

| Campo | Valor |
|-------|-------|
| **ID** | TC-05 |
| **Tipo de prueba** | Seguridad |
| **Prioridad** | Alta |
| **Módulo** | example.com |

## Precondiciones
- Conexión a internet activa

## Pasos
1. Cargar https://example.com
2. Verificar el candado de seguridad en el navegador
3. Inspeccionar el certificado

## Resultado esperado
La página carga por HTTPS sin advertencias. El certificado SSL es válido y está firmado por una CA reconocida (Let's Encrypt / IANA).

## Resultado actual
✅ PASS — Verificado el 2026-09-20
