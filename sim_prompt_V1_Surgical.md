---
layout: default
title: 'Optimización de Memoria Swap y ZRAM en Hardware Antiguo'
date: 2026-04-28
---

# Optimización de Memoria Swap y ZRAM en Hardware Antiguo

## 🛠️ Resumen Técnico
Implementación de un sistema de swap híbrido utilizando ZRAM (compresión en RAM) para reducir la latencia de E/S en discos mecánicos o SSDs antiguos, maximizando el uso de memoria física disponible.

## 🔍 Análisis de Kernel y Hardware
En hardware antiguo, el acceso a la partición de swap en disco (HDD/SSD) genera un cuello de botella masivo debido a la latencia de búsqueda y escritura. ZRAM crea un dispositivo de bloque comprimido en la RAM; el kernel mueve las páginas de memoria menos utilizadas a este espacio comprimido antes de intentar escribirlas en el disco. Esto reduce drásticamente los ciclos de escritura en el disco y acelera la recuperación de datos.

## 🚀 Protocolo de Implementación

1. **Instalación de dependencias:**
   ```bash
   sudo apt update && sudo apt install zram-config -y
   ```

2. **Configuración de Prioridades:**
   Editar `/etc/fstab` para asegurar que la swap de disco tenga una prioridad menor que ZRAM.
   ```bash
   # Ejemplo de entrada en fstab
   /swapfile none swap sw 0 0
   ```

3. **Ajuste de Swappiness:**
   Configurar el kernel para que prefiera el uso de swap comprimida.
   ```bash
   sudo sysctl vm.swappiness=100
   sudo sysctl -p
   ```

4. **Verificación del Estado:**
   ```bash
   zramctl
   ```

## 🏁 Veredicto de Soberanía
La implementación de ZRAM rompe la dependencia de la compra de hardware nuevo (más RAM física) al optimizar matemáticamente la memoria existente. Es un acto de eficiencia técnica que extiende la vida útil del hardware legacy.
