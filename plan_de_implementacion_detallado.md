# Plan de Implementación Detallado: Robot Amalia Gamma (Aloha Mini)

## 1. Visión General del Plan

El plan de implementación se estructura en cuatro fases principales, siguiendo un enfoque de desarrollo ágil y modular. El objetivo es pasar del prototipo de hardware a un sistema de IA en producción con capacidad de *Refourcing Learning* continuo.

| Fase | Título | Duración Estimada | Hitos Clave |
| :--- | :--- | :--- | :--- |
| **I** | Preparación de Infraestructura y Hardware | 4 Semanas | Hardware ensamblado, ROS 2 instalado, API Gateway desplegado. |
| **II** | Integración de Software y HAL | 3 Semanas | Comunicación bidireccional Robot-Nube funcional, HAL probada en Jetson y Arduino (simulado). |
| **III** | Configuración del Entorno de Entrenamiento | 5 Semanas | Entorno Britetrainer (Omniverse) configurado, MCCE funcional, Primera política de acción entrenada (Act-1). |
| **IV** | Producción y Refourcing Learning | Continuo | Despliegue de la política de acción en el robot real, Activación del ciclo de actualización autónoma. |

## 2. Fase I: Preparación de Infraestructura y Hardware (4 Semanas)

### Hitos Clave:
*   Hardware ensamblado y funcional.
*   Sistema Operativo y ROS 2 instalados en el chip principal.
*   API Gateway de Amalia desplegado en el *hosting* del usuario.

| Tarea | Dependencias | Responsable |
| :--- | :--- | :--- |
| **1.1. Adquisición de Componentes** | BOM (Bill of Materials) aprobado. | Usuario/Equipo de Adquisiciones |
| **1.2. Ensamblaje Mecánico** | Piezas impresas en 3D (Aloha Mini) y actuadores disponibles. | Equipo de Hardware |
| **1.3. Instalación de SO y ROS 2** | Chip principal (Jetson Orin Nano) disponible. | Equipo de Software/Robótica |
| **1.4. Despliegue de Infraestructura de Nube** | Acceso al *hosting* (CorticalLabs NPU) y credenciales. | Equipo de DevOps |
| **1.5. Prueba de Comunicación 868 MHz** | Módulo LoRa ensamblado. | Equipo de Hardware |

## 3. Fase II: Integración de Software y HAL (3 Semanas)

### Hitos Clave:
*   HAL (Capa de Abstracción de Hardware) implementada y probada en el chip principal.
*   Nodos ROS 2 funcionales para la lectura de sensores y la ejecución de acciones.
*   Comunicación bidireccional Robot-Nube (ROS 2 - API Gateway) estable.

| Tarea | Dependencias | Responsable |
| :--- | :--- | :--- |
| **2.1. Implementación de la HAL** | Diseño de la HAL (Documento `hal_interface.py`). | Equipo de Software Embebido |
| **2.2. Desarrollo de Nodos ROS 2** | HAL funcional. | Equipo de Robótica |
| **2.3. Integración de API Gateway** | API Gateway desplegado (Fase I). | Equipo de Software/DevOps |
| **2.4. Desarrollo de la UI de Control Local** | Diseño de la UI (Documento `control_ui.py`). | Equipo de Software de Escritorio |
| **2.5. Prueba del Sistema de Actualización** | HAL y API Gateway funcionales. | Equipo de QA/DevOps |

## 4. Fase III: Configuración del Entorno de Entrenamiento (5 Semanas)

### Hitos Clave:
*   Entorno de simulación **Britetrainer (Omniverse)** configurado.
*   MCCE Manager funcional y probado.
*   Primera política de acción entrenada (Act-1) y validada en simulación.

| Tarea | Dependencias | Responsable |
| :--- | :--- | :--- |
| **3.1. Configuración de Omniverse** | Licencias de NVIDIA y acceso al entorno. | Equipo de Simulación |
| **3.2. Implementación del MCCE Manager** | Kimi K2 (CorticalLabs NPU) accesible. | Equipo de IA/Software |
| **3.3. Desarrollo del Agente SIMA 2** | Mapeo de acciones de Aloha Mini a comandos de SIMA 2. | Equipo de IA/RL |
| **3.4. Entrenamiento Inicial (Act-1)** | MCCE y SIMA 2 funcionales. Ingesta de datos de video (simulando el guante de captura). | Equipo de IA/RL |
| **3.5. Validación Sim-to-Sim** | Prueba de la política de acción en el entorno virtual. | Equipo de QA/Simulación |

## 5. Fase IV: Producción y Refourcing Learning (Continuo)

### Hitos Clave:
*   Despliegue de la política de acción en el robot real.
*   Activación del ciclo de *Refourcing Learning* continuo.
*   Robot operando de forma autónoma (incluyendo recarga).

| Tarea | Dependencias | Responsable |
| :--- | :--- | :--- |
| **4.1. Despliegue de Política en Robot Real** | Política de acción validada (Fase III). | Equipo de Robótica/DevOps |
| **4.2. Prueba de Recarga Autónoma** | Módulo de carga inductiva instalado. | Equipo de Hardware/Robótica |
| **4.3. Activación del MCCE y RL Continuo** | Sistema en producción. | Equipo de IA/DevOps |
| **4.4. Monitoreo y Optimización** | Recolección de datos de fallos y éxitos para el reentrenamiento. | Equipo de QA/IA |

## 6. Dependencias Críticas

*   **Acceso a CorticalLabs NPU:** Es fundamental para el despliegue del LLM Kimi K2 y el funcionamiento del MCCE.
*   **Licencias de NVIDIA Omniverse:** Necesarias para la configuración del entorno de entrenamiento virtual (Britetrainer).
*   **Disponibilidad de Componentes:** La adquisición de la Jetson Orin Nano y la cámara RGB-D debe ser prioritaria.
