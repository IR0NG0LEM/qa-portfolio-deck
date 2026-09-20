# TC-06: Verificar código de respuesta HTTP 200

| Campo | Valor |
|-------|-------|
| **ID** | TC-06 |
| **Tipo de prueba** | Funcional / API |
| **Prioridad** | Alta |
| **Módulo** | example.com |

## Precondiciones
- Herramienta curl o navegador disponible

## Pasos
1. Ejecutar: `curl -I https://example.com`
2. Observar el código de estado

## Resultado esperado
El servidor responde con código **HTTP 200 OK** y Content-Type **text/html**.

## Resultado actual
✅ PASS — Verificado el 2026-09-20
