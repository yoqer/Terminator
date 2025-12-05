# Manual de Operación Autónoma del Robot Amalia Gamma (Terminator)

## 1. Introducción

El robot Amalia Gamma está diseñado para la **operación autónoma** continua, gestionando su propio ciclo de vida, entrenamiento y necesidades de energía. Este manual detalla los modos de operación y la gestión de la autonomía.

## 2. Modos de Operación

Amalia opera en un sistema de arquitectura híbrida que garantiza la funcionalidad incluso sin conexión a la nube.

| Modo de Operación | Conectividad a la Nube | Inferencia LLM | Propósito |
| :--- | :--- | :--- | :--- |
| **Cloud Backup (Online)** | Requerida | **CorticalLabs NPU** (Kimi K2 completo) | Razonamiento complejo, planificación de tareas a largo plazo, entrenamiento continuo (SIMA 2/Genie 3). |
| **Local Offline** | No Requerida | **LLM Cuantizado** (Edge Device) | Conversacionalidad de baja latencia, control de emergencia, tareas de rutina. |

### 2.1. Conmutación de Modos

El **Sync Manager** (parte de la Fase 8: Arquitectura Híbrida) gestiona la conmutación:

1.  **Fallo de Conexión:** Si la conexión a la API Gateway (para el NPU) falla durante más de 30 segundos, el robot conmuta automáticamente a **Local Offline**.
2.  **Baja Latencia:** Para comandos de voz urgentes, el robot prioriza el LLM local cuantizado para una respuesta inmediata, incluso en modo **Cloud Backup**.
3.  **Tarea Compleja:** Si una tarea requiere un razonamiento que excede la capacidad del LLM cuantizado, el robot espera la reconexión o solicita al usuario que simplifique la tarea.

## 3. Gestión de la Autonomía y Energía

### 3.1. Ciclo de Sueño/Vigilia (Sleep/Wake)

El robot utiliza un sistema de gestión de energía para optimizar el consumo:

*   **Modo Activo (Vigilia):** Todos los sensores y actuadores están activos. El LLM local está en modo de escucha.
*   **Modo de Bajo Consumo (Sueño):** El robot entra en este modo después de 30 minutos de inactividad o por comando de voz. Solo el módulo LoRa 868 MHz y un sensor de proximidad de bajo consumo permanecen activos.
*   **Activación:** El robot se activa por:
    *   Detección de movimiento por el sensor de proximidad.
    *   Comando de voz (palabra clave).
    *   Mensaje a través de la red LoRa.

### 3.2. Autocarga (Self-Charging)

El robot está equipado con un sistema de acoplamiento para la estación de carga inductiva.

1.  **Monitoreo:** El **HAL** informa el nivel de batería. Si el nivel cae por debajo del **20%**, el **Suna AI Navigator Agent** inicia la planificación de la tarea de recarga.
2.  **Planificación:** El agente utiliza el LLM (NPU o local) para calcular la ruta más eficiente a la estación de carga.
3.  **Ejecución:** El robot utiliza su **Movilidad Avanzada** (característica del "3er Robot") y la **Visión 3D** para acoplarse con precisión a la estación.

## 4. Entrenamiento Continuo y Auto-Actualización

El robot está diseñado para el **Aprendizaje Continuo** (Mem0).

*   **Detección de Fallos:** Si el robot falla en una tarea, el **MCCE Manager** registra el evento y genera un nuevo escenario de entrenamiento (utilizando SIMA 2 o Genie 3).
*   **Auto-Actualización:** Después de que el agente de RL (SIMA 2/Genie 3) genera una política de acción mejorada, el **Update Manager** descarga e instala automáticamente la nueva política en el robot, sin necesidad de intervención humana.

---
*Este documento es parte de la documentación de producción del Proyecto Amalia Gamma (Terminator).*
