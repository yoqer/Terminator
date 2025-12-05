# Paper de Montaje Termineitor: Un Enfoque Minimalista y Agnóstico

**Autor:** Manus AI
**Fecha:** 23 de Noviembre de 2025
**Proyecto:** Termineitor (Amalia Gamma Open Source)

---

## 1. Introducción

El proyecto Termineitor busca la democratización de la robótica humanoide mediante un diseño de montaje minimalista y una arquitectura de software agnóstica al hardware. Este *paper* detalla el proceso de montaje físico del robot, basado en la plataforma **Aloha Mini** [1], y la integración de los componentes de inteligencia (Chip Principal, Sensores, Comunicación IoT) para crear un sistema robusto y portátil.

## 2. Principios de Montaje Minimalista

El montaje se adhiere a tres principios fundamentales:

1.  **Modularidad:** Cada componente debe ser fácilmente reemplazable o actualizable.
2.  **Integración Compacta:** Minimizar el volumen y el peso, concentrando la electrónica en la base móvil.
3.  **Abstracción de Hardware:** El montaje debe facilitar la conexión de diferentes chips (Jetson, Raspberry Pi, etc.) sin alterar la estructura mecánica.

## 3. Componentes Clave y Su Integración

El montaje se centra en la integración de los componentes de la **Unidad de Procesamiento Central (UPC)** y la **Unidad de Percepción**.

### 3.1. Unidad de Procesamiento Central (UPC)

La UPC, que alberga el chip principal (ej. NVIDIA Jetson Orin Nano), se monta en la base móvil del robot.

| Componente | Montaje | Conexión |
| :--- | :--- | :--- |
| **Chip Principal (Jetson)** | Montado en una placa de acrílico o aluminio en la base. Se utiliza un disipador de calor de bajo perfil. | Conexión directa a la fuente de alimentación y al *hub* USB para periféricos. |
| **Batería Li-Ion** | Ubicada en el centro de la base para optimizar el centro de gravedad. | Conectada a un Sistema de Gestión de Batería (BMS) y al módulo de carga inductiva. |
| **Módulo LoRa (868 MHz)** | Conectado a un puerto GPIO o USB de la Jetson. La antena se extiende verticalmente para una mejor cobertura. | Utilizado por el **IoT 868 MHz Node** (software) para el modo reposo/activación. |

### 3.2. Unidad de Percepción

La unidad de percepción se monta en la parte superior del robot para una visión de 360 grados y una interacción conversacional efectiva.

*   **Cámara RGB-D (ej. RealSense):** Montada en la "cabeza" del robot. Proporciona datos de profundidad esenciales para la manipulación y la navegación.
*   **Micrófono Array (ej. ReSpeaker):** Integrado en la carcasa de la cabeza, cerca de la cámara. Su función es capturar audio de alta calidad para el STT (Speech-to-Text) y la localización de la fuente de sonido.

## 4. Proceso de Montaje (Pasos Clave)

El proceso de montaje se realiza en un orden que minimiza la complejidad del cableado.

1.  **Ensamblaje Mecánico Base:** Montaje de la base móvil y los brazos de Aloha Mini.
2.  **Cableado de Actuadores:** Conexión de los servomotores a la placa de control de bajo nivel (ej. placa de control de motor de Aloha Mini).
3.  **Integración de la UPC:** Montaje del Chip Principal y la Batería en la base. Conexión de la fuente de alimentación.
4.  **Cableado de Percepción:** Conexión de la Cámara RGB-D y el Micrófono Array al Chip Principal (vía USB 3.0 o MIPI CSI).
5.  **Prueba de Conectividad:** Verificación de que el Chip Principal detecta todos los sensores y actuadores.
6.  **Carga del Software:** Instalación del sistema operativo y la imagen Docker del software Termineitor (HAL, Update Manager).

## 5. Conclusión

El montaje Termineitor es un diseño de referencia que prioriza la funcionalidad de la IA sobre la complejidad mecánica. Al utilizar una plataforma *open-source* y componentes comerciales de fácil acceso, se logra un robot minimalista y potente, listo para ser entrenado por el sistema Amalia Gamma. La clave de su éxito reside en la abstracción de hardware, que permite a los usuarios intercambiar la UPC sin necesidad de rediseñar el robot.

---
## Referencias

[1] Aloha Mini: $600 Open-Source Home Robot, Reddit.
[2] NVIDIA Jetson Orin Nano Developer Kit Documentation.
[3] Concepto de Hardware Abstraction Layer (HAL) en sistemas embebidos.
