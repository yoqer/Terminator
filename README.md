# Proyecto Amalia Gamma: Terminator - Robótica de Producción y Democratización

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)](./plan_de_implementacion_detallado.md)
[![Patrocinado por](https://img.shields.io/badge/Sponsored%20by-WC-purple.svg)](http://torete.net/terminator)

## 🚀 Visión General del Proyecto

**Amalia Gamma (Terminator)** es la versión de producción extendida de nuestro proyecto *Open Source*, diseñada para la **democratización de la robótica avanzada** y la **Inteligencia Artificial encarnada**.

Esta versión se centra en la **portabilidad de hardware** a través de la contenedorización (Docker) y un sistema de entrenamiento híbrido de vanguardia, asegurando que el software sea completamente **agnóstico al hardware** y esté listo para su despliegue en múltiples plataformas.

---

## 🤖 Plataforma Robótica Base y Características del "SuperRobot Multiusos"

El diseño base es el manipulador de doble brazo **Aloha Mini** [1], pero extendido con las características clave del **"3er Robot"** para crear un **SuperRobot Multiusos** con capacidades avanzadas de movilidad y percepción.

| Característica | Base Tecnológica | Rol en Amalia Gamma |
| :--- | :--- | :--- |
| **Manipulación** | Aloha Mini (Doble Brazo) | Tareas de destreza y manipulación fina. |
| **Movilidad Avanzada** | Base Omnidireccional (Inferencia) | Navegación autónoma y precisa en entornos complejos. |
| **Visión 3D** | Sensor de Profundidad Estéreo (Inferencia) | Percepción espacial precisa, crucial para la planificación de tareas y la evitación de obstáculos. |
| **Autonomía** | Sistema de Carga Inductiva y Modos Sleep/Wake | Operación continua y gestión inteligente de energía. |

## 🧠 Arquitectura de Software Agnóstica y Contenedorización

El software de Amalia Gamma es completamente independiente del hardware gracias a la **Capa de Abstracción de Hardware (HAL)** y se despliega mediante **contenedores Docker** para garantizar la máxima portabilidad.

### 1. Compatibilidad de Hardware (HAL)

El sistema de control funciona en una amplia gama de dispositivos, con imágenes Docker optimizadas para cada arquitectura.

| Chip Compatible | Arquitectura | Tipo de Despliegue |
| :--- | :--- | :--- |
| **NVIDIA Jetson Orin Nano** | ARM64 | **Recomendado:** Docker (ROS 2, Edge AI) |
| **Raspberry Pi 5** | ARM64 | Docker (ROS 2, Bajo Costo) |
| **Mini PC (x86)** | AMD64 | Docker (ROS 2, Alto Rendimiento) |
| **Qualcomm/Arduino** | ARM/Microcontrolador | Firmware (C/C++) + HAL Bridge |

### 2. Software Híbrido (Nube y Borde)

| Componente | Ubicación | Función Clave |
| :--- | :--- | :--- |
| **HAL** | Robot (Borde) | Abstracción de hardware y control de bajo nivel. |
| **LLM Engine (Kimi K2)** | Nube (**CorticalLabs NPU**) | Razonamiento, planificación y conversacionalidad. |
| **RL Agent (SIMA 2)** | Nube/Borde | Generación de políticas de acción robótica. **Implementación Funcional (No Simulada)**. |
| **Programable Trainer (Genie 3)** | Nube | Generación de escenarios de entrenamiento interactivos y programables. |

## 🌐 Sistema de Entrenamiento Híbrido (SIMA 2 Funcional + Genie 3)

El sistema de entrenamiento utiliza una arquitectura híbrida para maximizar la eficiencia y la flexibilidad.

### 1. SIMA 2: Sim-to-Real Funcional

La integración de **Google DeepMind SIMA 2** es **funcional y no simulada**. El agente genera acciones de alto nivel en el entorno virtual (NVIDIA Omniverse), que son traducidas por el Planificador de Tareas de ROS 2 en comandos de bajo nivel que se ejecutan directamente en el hardware a través de la HAL.

### 2. Genie 3: Entrenamiento Programable

**Google Genie 3** se integra como un generador de mundos interactivos. Permite a los investigadores o al **Suna AI Navigator Agent** crear escenarios de entrenamiento complejos a partir de *prompts* de lenguaje natural (ej. "Entrena al robot para que navegue por un almacén desordenado"). Esto acelera el **Aprendizaje por Imitación (IL)** y la validación de políticas.

## 💾 Despliegue y Modelos Cuantizados

### 1. Contenedorización (Docker)

El despliegue en dispositivos de borde se realiza mediante Docker:

```bash
# Para Jetson, Raspberry Pi (ARM64)
docker build -f deployment/Dockerfile.arm64 -t amalia-gamma-arm64 .
docker run --privileged -d --net=host amalia-gamma-arm64

# Para Mini PC (AMD64)
docker build -f deployment/Dockerfile.amd64 -t amalia-gamma-amd64 .
docker run --privileged -d --net=host amalia-gamma-amd64
```

### 2. Instrucciones para LLM Cuantizados en Edge

Para la operación local *offline* y la conversacionalidad de baja latencia, Amalia utiliza modelos de lenguaje cuantizados (ej. Llama 3 Q4, Phi-3 Mini).

**Consulte el manual detallado:** [llm_quantization_guide.md](./llm_quantization_guide.md)

Este manual incluye:
*   Guía de conversión de Kimi K2 a formatos cuantizados (GGUF, ONNX).
*   Instrucciones de carga y uso de *runtimes* optimizados (ej. llama.cpp, ONNX Runtime) para cada plataforma.

## 📖 Manuales de Operación

Se han desarrollado manuales completos para la operación autónoma:

*   **Manual de Operación Autónoma:** [autonomous_operation_manual.md](./autonomous_operation_manual.md)
    *   Detalla los modos de operación (*Cloud Backup* vs. *Local Offline*).
    *   Instrucciones para la gestión de la batería y el ciclo de sueño/vigilia.
*   **Guía de Cuantización de LLM:** [llm_quantization_guide.md](./llm_quantization_guide.md)

---

## 🔗 Enlaces y Documentación

*   **Web Oficial del Proyecto:** [http://torete.net/terminator](http://torete.net/terminator)
*   **Plan de Implementación Detallado:** [plan_de_implementacion_detallado.md](./plan_de_implementacion_detallado.md)
*   **Requisitos de Hardware y BOM:** [hardware_requirements_and_bom.md](./hardware_requirements_and_bom.md)
*   **Código Fuente del Software Agnóstico:** [amalia_gamma_project/software/](./amalia_gamma_project/software/)

---
## 📜 Licencia y Patrocinio

Este proyecto es patrocinado por la **WC (World Community)** como una iniciativa para la democratización de la robótica.

**Licencia:** **Apache License 2.0** (Ver archivo [LICENSE](./LICENSE))

---
## Referencias

[1] Aloha Mini: $600 Open-Source Home Robot, Trossen Robotics.
[2] Google DeepMind SIMA 2: An agent that plays, reasons, and learns with you in virtual 3D worlds.
[3] Google DeepMind Genie 3: A new frontier for world models.
