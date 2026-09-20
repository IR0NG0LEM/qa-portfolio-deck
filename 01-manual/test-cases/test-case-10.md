# TC-10: Verificar comportamiento con HTTP (sin S)

| Campo | Valor |
|-------|-------|
| **ID** | TC-10 |
| **Tipo de prueba** | Seguridad / Redirección |
| **Prioridad** | Media |
| **Módulo** | example.com |

## Precondiciones
- Herramienta curl disponible

## Pasos
1. Ejecutar: `curl -I http://example.com`
2. Observar el código de respuesta

## Resultado esperado
El servidor responde en HTTP (200 OK en la verificación actual). Nota: el comportamiento ideal sería redirigir 301 a HTTPS — se registra como observación de mejora.

## Resultado actual
✅ PASS — Verificado el 2026-09-20
