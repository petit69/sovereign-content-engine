---
layout: default
title: Configuración de swap y zram para sistemas con poca RAM
date: 2026-04-27
image: https://images.unsplash.com/photo-1518770660439-4636efebcaef?auto=format&fit=crop&w=600&q=80
---

# Configuración de swap y zram para sistemas con poca RAM

Cuando tienes 2GB o 4GB de RAM, el sistema colapsa rápidamente. ZRAM es la solución técnica para evitar el congelamiento del sistema.

## Implementación Técnica
1. **Instalar zram-tools:** `sudo apt install zram-config`.
2. **Verificación:** Ejecuta `zramctl` para ver la compresión activa.
3. **Sinergia con Swap:** Mantén una pequeña partición de swap en el SSD como respaldo.

**Conclusión:** ZRAM permite ejecutar aplicaciones modernas en hardware limitado.
