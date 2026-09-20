// Script k6 — Prueba de carga básica para example.com
// Generado por qwen3:14b (local) — corregido tras revisión (imports, thresholds, headers)
// Objetivo: 10 VUs, 30s, status 200, p95 < 2000ms, error rate < 1%
// Nota: example.com rechaza el User-Agent por defecto de k6 (403) — se envían headers de navegador

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<2000'],
    http_req_failed: ['rate<0.01'],
  },
};

const headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.9',
};

export default function () {
  const res = http.get('https://example.com', { headers });
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
