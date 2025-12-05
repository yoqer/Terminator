# Plan de Creación Completo: Robot Humanoide Open-Source (Amalia Gamma Integrado)

## 1. Resumen del Proyecto

Este plan detalla la creación de un robot humanoide de estilo *open-source* (basado en **Aloha Mini**) integrado con el sistema de inteligencia artificial **Amalia Gamma**. El objetivo es un robot con autonomía avanzada, capacidad de reentrenamiento flexible (*Reinforcement Learning* - RL) en un entorno virtual (**Britetrainer/Omniverse**) y comunicación IoT de baja potencia (868 MHz).

## 2. Fases del Proyecto (Maquetación a Producción RL)

El proyecto se divide en cinco fases principales, desde el diseño físico hasta el despliegue de la IA en producción.

### Fase 1: Maquetación y Prototipado (Hardware)

| Tarea | Descripción | Componentes Clave |
| :--- | :--- | :--- |
| **1.1. Diseño 3D** | Adaptación de los archivos CAD de Aloha Mini para integrar la **Jetson Orin Nano** y la batería. Diseño de la carcasa para el módulo LoRa. | Archivos STL de Aloha Mini, Software CAD (ej. Fusion 360). |
| **1.2. Prototipado de Comunicación** | Montaje del módulo LoRa (868 MHz) y prueba de la comunicación con un dispositivo IoT simple (ej. un sensor de puerta). | Módulo LoRa (SX1276), Tarjeta de desarrollo (ej. Arduino/RPi Pico). |
| **1.3. Prototipado de Energía** | Montaje de la batería y el sistema de carga inductiva. Prueba de la lógica de *Health & Power Node* (detección de batería baja). | Batería Li-Ion, Módulo de carga inductiva. |

### Fase 2: Construcción y Ensamblaje (Hardware Final)

| Tarea | Descripción | Componentes Clave |
| :--- | :--- | :--- |
| **2.1. Impresión 3D y Ensamblaje** | Impresión de todas las piezas adaptadas. Ensamblaje de la estructura mecánica de Aloha Mini. | Impresora 3D, Filamento PLA/PETG. |
| **2.2. Integración de Electrónica** | Montaje de la **Jetson Orin Nano** (o RPi 5), el módulo LoRa y el *array* de micrófonos. Cableado final de los actuadores y sensores. | Jetson Orin Nano, Módulo LoRa, Actuadores de Aloha Mini. |
| **2.3. Instalación de Software Base** | Instalación del Sistema Operativo (Ubuntu), ROS 2 y el SDK de Aloha Mini. | Ubuntu, ROS 2, SDK de Aloha Mini. |

### Fase 3: Integración de Software (Amalia Gamma)

| Tarea | Descripción | Módulos de Amalia Gamma |
| :--- | :--- | :--- |
| **3.1. Configuración del API Gateway** | Despliegue del *API Gateway* (Fase 8) en el *hosting* del usuario (CorticalLabs NPU). | `api-gateway.py`, `deployment-config.yaml`. |
| **3.2. Desarrollo de Nodos ROS 2** | Creación de los nodos ROS 2 en la Jetson para: 1) Recopilar datos de sensores, 2) Enviar datos al *API Gateway*, 3) Recibir comandos de acción. | ROS 2 Nodes (Python/C++). |
| **3.3. Integración de Conversacionalidad** | Configuración del STT/TTS y el nodo ROS 2 para enviar la entrada de voz al *API Gateway* y recibir la respuesta de Kimi K2. | Módulo de Conversacionalidad (Fase 4). |

### Fase 4: Entrenamiento Inicial (Britetrainer RL)

| Tarea | Descripción | Componentes Clave |
| :--- | :--- | :--- |
| **4.1. Configuración de Britetrainer** | Creación del entorno de simulación en **NVIDIA Omniverse (Isaac Sim)** que replica el robot y el entorno de tareas. | NVIDIA Omniverse, USD files. |
| **4.2. Entrenamiento de la Tarea Base (Act-1)** | Uso de *Imitation Learning* (IL) y *Reinforcement Learning* (RL) para entrenar a **SIMA 2** en una tarea compleja (ej. "recoger un objeto y colocarlo en un estante"). | SIMA 2 Agent, MCCE (Módulo de Gestión de Contenido de Entrenamiento). |
| **4.3. Despliegue de la Política Inicial** | La política de acción entrenada se integra en el *API Gateway* para su uso en el robot real. | API Gateway (Fase 8). |

### Fase 5: Producción y Reentrenamiento Continuo (Refourcing Learning)

| Tarea | Descripción | Módulos de Amalia Gamma |
| :--- | :--- | :--- |
| **5.1. Pruebas Sim-to-Real** | Validación de la política de acción en el robot Aloha Mini real. Ajuste de parámetros de control. | Control Node (Borde), SIMA 2 Agent (Nube). |
| **5.2. Activación del MCCE** | Puesta en marcha del **MCCE** para la ingesta de contenido flexible y la actualización autónoma del software. | MCCE (Hosting del Usuario). |
| **5.3. Refourcing Learning** | El robot opera de forma autónoma, y cada nueva tarea o error desencadena un ciclo de reentrenamiento en Britetrainer (RL continuo), mejorando la política de acción de SIMA 2. | Todo el sistema Amalia Gamma. |

## 3. Análisis de Robots y Webs Alternativas

Se analizó el concepto de **Sunday Robotics (Act-1)** [1] y la plataforma **Source Robotics** [2].

*   **Sunday Robotics (Act-1):** Su enfoque en el *foundation model* entrenado sin datos robóticos directos (usando guantes de captura) valida la estrategia de Amalia de usar un LLM (Kimi K2) para generar la lógica de entrenamiento (función de recompensa y escenarios).
*   **Source Robotics:** Ofrece brazos robóticos *open-source* (ej. PAROL6), que podrían ser una alternativa a Aloha Mini si se requiere una mayor precisión en la manipulación estática, pero Aloha Mini es superior para la movilidad.

La elección de **Aloha Mini** y la integración de **SIMA 2** y **Omniverse** posicionan este proyecto en la vanguardia de la robótica *open-source* y la IA encarnada.

---
## Referencias

[1] Sunday Robotics ACT-1: A Robot Foundation Model Trained on Zero Robot Data, Sunday.ai.
[2] Source Robotics | Open Source Robotic Arms, Source Robotics.
[3] Aloha Mini: $600 Open-Source Home Robot, Reddit.
