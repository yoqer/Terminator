# Requisitos de Hardware Específicos y Bill of Materials (BOM) Preliminar

## 1. Requisitos de Hardware Específicos (Robot Aloha Mini - Amalia Gamma)

El robot minimalista, basado en la plataforma *open-source* **Aloha Mini**, requiere componentes específicos para soportar la arquitectura de software agnóstico y las capacidades de IA de Amalia Gamma.

### 1.1. Chip de Procesamiento (Cerebro de Borde)

El chip debe ser capaz de ejecutar ROS 2 y el *middleware* de la HAL, además de manejar tareas de pre-procesamiento de sensores.

| Componente | Requisito Mínimo | Requisito Recomendado | Justificación |
| :--- | :--- | :--- | :--- |
| **Chip Principal** | Raspberry Pi 5 (8GB RAM) | **NVIDIA Jetson Orin Nano (8GB)** | La Jetson ofrece una NPU (GPU) para el pre-procesamiento de visión (Edge AI), reduciendo la latencia antes de enviar datos al *hosting* de CorticalLabs NPU. |
| **Memoria (RAM)** | 4 GB | **8 GB** | Necesario para ejecutar el sistema operativo (Ubuntu), ROS 2 y los nodos de fusión de sensores. |
| **Almacenamiento** | 64 GB MicroSD (Clase 10) | **128 GB NVMe SSD** | El SSD es crucial para la velocidad de arranque, la gestión de logs y la estabilidad de las actualizaciones de software. |

### 1.2. Sensores (Percepción)

La percepción es vital para que el agente SIMA 2 (en la nube) pueda generar políticas de acción efectivas.

| Componente | Requisito | Justificación |
| :--- | :--- | :--- |
| **Visión Principal** | Cámara de Profundidad RGB-D (ej. Intel RealSense D435i) | Proporciona datos de color (RGB) y profundidad, esenciales para la manipulación de objetos (inspirado en Act-1). |
| **Audio (Conversacionalidad)** | Micrófono Array de 4 Micrófonos (ej. ReSpeaker) | Necesario para la cancelación de eco, la localización de la fuente de sonido y la interacción conversacional. |
| **IMU** | Unidad de Medición Inercial (Integrada en la Jetson o externa) | Proporciona datos de orientación y aceleración para el control de equilibrio y la cinemática. |

### 1.3. Comunicación y Energía

| Componente | Requisito | Justificación |
| :--- | :--- | :--- |
| **Comunicación IoT** | Módulo LoRa (868 MHz) con antena externa | Permite la comunicación de baja potencia para el modo reposo/activación y la integración con dispositivos IoT domésticos. |
| **Comunicación de Datos** | Wi-Fi 5 GHz (Integrado en el chip) | Enlace de alta velocidad al *API Gateway* en el *hosting* del usuario. |
| **Batería** | Batería Li-Ion 12V (10Ah - 15Ah) | Equilibrio entre peso y autonomía (aproximadamente 1-2 horas de operación activa). |
| **Recarga Autónoma** | Módulo de Carga Inductiva (15W - 30W) | Permite al robot acoplarse a la base de carga sin intervención humana. |

## 2. Bill of Materials (BOM) Preliminar

Esta es una estimación de los componentes necesarios para la construcción del robot.

| Categoría | Componente | Cantidad | Costo Estimado (USD) |
| :--- | :--- | :--- | :--- |
| **Plataforma Base** | Kit de Impresión 3D Aloha Mini (Piezas) | 1 | $300 |
| | Actuadores/Servomotores (Aloha Mini) | 12 | $400 |
| | Base Móvil (Ruedas/Motores) | 1 | $150 |
| **Procesamiento** | NVIDIA Jetson Orin Nano (8GB) | 1 | $199 |
| | NVMe SSD (128 GB) | 1 | $30 |
| **Sensores** | Intel RealSense D435i (o similar) | 1 | $250 |
| | ReSpeaker 4-Mic Array | 1 | $50 |
| **Comunicación/Energía** | Módulo LoRa (868 MHz) | 1 | $20 |
| | Batería Li-Ion 12V 10Ah | 1 | $80 |
| | Módulo de Carga Inductiva | 1 | $40 |
| **Varios** | Cableado, Conectores, Fuente de Alimentación Externa | 1 | $50 |
| **TOTAL ESTIMADO** | | | **$1670 USD** |

*Nota: Este costo es una estimación preliminar y no incluye el costo de la mano de obra, el hosting de la IA (CorticalLabs NPU) ni el software propietario (SIMA 2, Omniverse).*
