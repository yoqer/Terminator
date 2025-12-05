# Diseño de Arquitectura Amalia Gamma v2.0: Integración Híbrida y Producción

## 1. Introducción

Esta versión de la arquitectura del Proyecto Amalia Gamma se centra en la **producción no simulada** y la **democratización** a través de la portabilidad de hardware y la contenedorización. Se introduce un sistema de entrenamiento híbrido que combina la arquitectura **Sim-to-Real** existente con NVIDIA Omniverse y SIMA 2, con la nueva capacidad de **Entrenamiento Programable** a través de Google Genie 3.

## 2. Arquitectura de Entrenamiento Híbrida

El sistema de entrenamiento se divide en dos módulos principales, ambos gestionados por el **Suna AI Navigator Agent** (Fase 4):

| Módulo | Base Tecnológica | Propósito Principal | Requisito de Producción |
| :--- | :--- | :--- | :--- |
| **Britetrainer (Sim-to-Real)** | NVIDIA Omniverse Isaac Sim, SIMA 2 | Aprendizaje por Refuerzo (RL) y Transferencia de Habilidades (Sim-to-Real). | **Implementación funcional y no simulada** de la API de SIMA 2 para traducir acciones virtuales a comandos ROS 2. |
| **Genie-Programmer** | Google Genie 3 World Model | Generación de escenarios de entrenamiento interactivos y programables a partir de lenguaje natural. | Uso de la API de Genie 3 para crear entornos 3D en tiempo real que sirvan como *input* para el sistema de visión y planificación de Amalia. |

### 2.1. Integración Funcional SIMA 2 (No Simulada)

Para cumplir con el requisito de "no simulado", la integración de SIMA 2 se implementará a nivel de la **API de Control de Agente**.

1.  **SIMA 2 Output**: El agente genera una secuencia de acciones de alto nivel (ej. "Recoger taza", "Abrir puerta").
2.  **Planificador de Tareas (ROS 2)**: Un nodo de ROS 2 recibe la acción de alto nivel.
3.  **Módulo de Cinemática Inversa (IK)**: El planificador descompone la acción en comandos de bajo nivel (posiciones articulares, velocidades) utilizando el modelo cinemático del robot (basado en Aloha Mini + características del "3er Robot").
4.  **HAL (Hardware Abstraction Layer)**: El HAL traduce los comandos de bajo nivel a señales específicas para los actuadores (Jetson, Raspberry Pi, etc.).

Esto asegura que el código de producción en el robot es la implementación de la lógica de control, no la simulación en sí.

### 2.2. Integración de Google Genie 3

Genie 3 se utilizará para la **creación rápida de escenarios de entrenamiento** para el **Aprendizaje por Imitación (IL)** y la **Planificación de Tareas**.

-   **Generación de Escena**: El usuario o Suna AI Navigator proporciona un *prompt* (ej. "Un entorno de cocina desordenado con una taza roja en la mesa"). Genie 3 genera el entorno 3D interactivo.
-   **Entrenamiento Programable**: Amalia se entrena en este entorno virtual generado por Genie 3, aprendiendo la secuencia de acciones para lograr el objetivo.
-   **Ventaja**: Permite un entrenamiento flexible y rápido sin la necesidad de modelado 3D manual en Omniverse.

## 3. Integración de Características del "3er Robot"

Asumiendo que el "3er Robot" representa una evolución del diseño de Aloha Mini hacia un sistema más robusto y móvil, se integrarán las siguientes características clave, esenciales para un "superRobot Multiusos":

1.  **Movilidad Avanzada**: Adición de una base móvil omnidireccional (Mecanum Wheels) para navegación autónoma en entornos complejos.
2.  **Visión Estéreo/3D**: Integración de un sensor de profundidad (ej. Intel RealSense o similar) para una percepción 3D precisa, crucial para la manipulación y la navegación.
3.  **Capacidad de Carga y Autonomía**: Diseño de un sistema de acoplamiento para la estación de carga y optimización del *firmware* para modos de bajo consumo (sleep/wake).

## 4. Contenedorización para Portabilidad (Docker)

Para lograr la portabilidad a través de las plataformas (Jetson, Raspberry Pi, Mini PC, Qualcomm/Arduino), se utilizará **Docker** con imágenes base específicas para la arquitectura (ARM64 para Pi/Jetson/Qualcomm, AMD64 para Mini PC).

-   **`Dockerfile.robot_core`**: Contiene el *stack* de ROS 2, el HAL, y el código de control de bajo nivel.
-   **`Dockerfile.ai_inference`**: Contiene el *runtime* de LLM (Kimi K2) y las bibliotecas de inferencia (ej. ONNX Runtime, TFLite) para modelos cuantizados.

Esto garantiza que el software es **hardware-agnostic** y se puede desplegar con un solo comando.

## 5. Documentación y Modelos Cuantizados

Se actualizará la documentación para incluir:

-   **Instrucciones de Cuantización**: Guía detallada para cuantizar el modelo Kimi K2 (ej. a INT8) y cargarlo en dispositivos de borde (Jetson, Pi).
-   **Manuales de Operación**: Instrucciones para la operación autónoma con respaldo en la nube (CorticalLabs NPU) y capacidad *offline* local.
-   **Actualización del README**: Inclusión de Genie 3, SIMA 2 funcional, contenedorización y la lista completa de hardware compatible.

## 6. Migración a "yoqer/Terminator"

Todos los archivos de código y documentación serán migrados al repositorio **yoqer/Terminator** para la versión de producción extendida.

---
*Este documento de diseño es la base para la implementación de la Fase 3.*
