# Reporte: Prueba de carga example.com (k6)

**Fecha:** 2026-09-20 | **Herramienta:** k6 v2.2.0 | **Script:** [example-load-test.js](k6-scripts/example-load-test.js)

## Configuración

| Parámetro | Valor |
|-----------|-------|
| Usuarios virtuales (VUs) | 10 |
| Duración | 30 segundos |
| Requests totales | 290 |
| Throughput | 9.43 req/s |

## Thresholds (criterios de aceptación)

| Métrica | Criterio | Resultado | Estado |
|---------|----------|-----------|--------|
| p95 de respuesta | < 2000 ms | **64.01 ms** | ✅ PASS |
| Tasa de error | < 1% | **0.00%** | ✅ PASS |
| Status 200 | 100% checks | 290/290 | ✅ PASS |

## Métricas completas

| Métrica | Valor |
|---------|-------|
| avg | 54.57 ms |
| min | 48.51 ms |
| med | 53.26 ms |
| max | 67.68 ms |
| p(90) | 60.49 ms |
| p(95) | 64.01 ms |

## Hallazgo técnico relevante

Durante la primera ejecución, **el 100% de los requests fallaron** (status 403) pese a que el sitio responde 200 a curl y navegadores. Diagnóstico:

1. `curl -A "k6/2.2.0"` → 200 (el UA de k6 por sí solo no es bloqueado)
2. `k6` con UA por defecto → **403** (la CDN de example.com bloquea la huella TLS del cliente Go de k6)
3. `k6` con headers de navegador (UA + Accept + Accept-Language) → **200**

**Conclusión:** la CDN aplica fingerprinting TLS + header. Solución: enviar headers de navegador en el script. Este es un hallazgo típico de pruebas de performance reales: el primer obstáculo suele ser que el objetivo te detecta como bot antes de medir nada.

## Generación del script

Script generado por **qwen3:14b** (Ollama local, hf.co/unsloth/Qwen3-14B-GGUF:Q5_K_M) y corregido en revisión:
- ~~`import { threshold }`~~ → no existe en k6 (eliminado)
- ~~`http_req_duration{percentile:0.95}`~~ → sintaxis correcta: `http_req_duration: ['p(95)<2000']`
- ~~`rate < 0.01`~~ → sintaxis correcta: `rate<0.01`
- Headers de navegador agregados (hallazgo del 403)
