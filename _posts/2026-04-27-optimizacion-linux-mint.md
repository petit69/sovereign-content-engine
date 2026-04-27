---
layout: post
title: Optimización de Linux Mint para CPUs antiguas
date: 2026-04-27
---

# Optimización de Linux Mint para CPUs antiguas

Para lograr la soberanía tecnológica en hardware legado, el primer paso es reducir la carga del sistema operativo. Linux Mint XFCE es la mejor opción, pero requiere ajustes específicos.

## Pasos de Optimización
1. **Desactivar Servicios Innecesarios:** Elimina el indexador de archivos y servicios de impresión si no los usas.
2. **Gestión de Memoria:** Implementa ZRAM para comprimir la RAM y evitar el uso excesivo del disco.
3. **Ajuste de Swappiness:** Cambia el valor de `vm.swappiness` a 10 para priorizar la RAM física.

**Conclusión:** Un sistema optimizado es la base de la soberanía técnica.
