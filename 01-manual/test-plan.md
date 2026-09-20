# Test Plan — example.com

## 1. Objetivo
Validar el comportamiento, contenido y disponibilidad del sitio **https://example.com** como aplicación objetivo de pruebas, cubriendo aspectos funcionales, de UI, seguridad básica y performance.

## 2. Alcance

### Dentro del alcance
- Verificación de contenido (título, encabezados, texto, enlaces)
- Comprobación de respuesta HTTP y certificado SSL
- Medición de tiempos de carga
- Visualización responsive en 3 viewpoints
- Validez estructural del HTML

### Fuera del alcance
- Pruebas de backend / base de datos (el sitio es estático)
- Pruebas de carga masiva (se cubren en el módulo 03-performance con k6)
- Pruebas en navegadores obsoletos (IE, etc.)

## 3. Tipos de prueba

| Tipo | Descripción | Casos |
|------|-------------|-------|
| Funcional | Contenido y comportamiento esperado | TC-01, TC-02, TC-03, TC-04, TC-06 |
| UI / Compatibilidad | Visualización y responsive | TC-02, TC-08 |
| Seguridad básica | HTTPS, certificado, redirección | TC-05, TC-10 |
| Performance | Tiempos de respuesta | TC-07 |
| Estructural | Validez del HTML | TC-09 |

## 4. Criterios de entrada
- Sitio https://example.com accesible desde la red de pruebas
- Navegador actualizado (Chrome/Edge/Firefox)
- Herramientas disponibles: curl, DevTools

## 5. Criterios de salida
- 100% de los casos ejecutados
- 0 defectos críticos o altos abiertos
- Evidencia registrada en cada test case

## 6. Entregables
- 10 test cases documentados (carpeta test-cases/)
- Reportes de bugs (carpeta bug-reports/)
- Matriz de trazabilidad (próxima entrega)
