# TC-07: Verificar tiempo de carga bajo 2 segundos

| Campo | Valor |
|-------|-------|
| **ID** | TC-07 |
| **Tipo de prueba** | Performance |
| **Prioridad** | Media |
| **Módulo** | example.com |

## Precondiciones
- Conexión estable a internet

## Pasos
1. Ejecutar: `curl -o /dev/null -w "%{{time_total}}" https://example.com`
2. Repetir 3 veces y promediar

## Resultado esperado
El tiempo total de respuesta es **menor a 2 segundos**. (Medición real: ~0.12s)

## Resultado actual
✅ PASS — Verificado el 2026-09-20
