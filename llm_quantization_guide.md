# Guía de Cuantización de Modelos de Lenguaje (LLM) para Dispositivos Edge

## 1. Introducción

El Proyecto Amalia Gamma (Terminator) está diseñado para operar de forma autónoma con capacidades de razonamiento local. Esto requiere la ejecución de modelos de lenguaje grandes (LLM) como **Kimi K2** en dispositivos de borde con recursos limitados (Jetson, Raspberry Pi, Qualcomm). La **cuantización** es un proceso esencial para reducir el tamaño del modelo y la latencia de inferencia.

## 2. Modelos de Referencia Cuantizados

Aunque el modelo central es **Kimi K2**, se proporcionan instrucciones para modelos de referencia de código abierto que pueden ser cuantizados y utilizados como alternativa local.

| Modelo | Parámetros | Cuantización Recomendada | Plataforma Objetivo |
| :--- | :--- | :--- | :--- |
| **Kimi K2 (Local)** | ~8B | Q4_K_M (GGUF) | Jetson Orin Nano (8GB+), Mini PC |
| **Llama 3** | 8B | Q4_K_M (GGUF) | Jetson Orin Nano (8GB+), Mini PC |
| **Phi-3 Mini** | 3.8B | Q4_0 (GGUF/ONNX) | Raspberry Pi 5 (8GB), Qualcomm |

## 3. Proceso de Cuantización (Kimi K2/Llama 3)

El método preferido para la cuantización es el formato **GGUF** (GPT-J-style Gated Unit Format), que es compatible con el *runtime* `llama.cpp` y sus *bindings* en Python.

### Paso 3.1: Conversión a Formato Intermedio

Asumiendo que el modelo Kimi K2 está disponible en formato PyTorch o Hugging Face, el primer paso es convertirlo a un formato intermedio.

```bash
# Ejemplo de conversión a GGUF (requiere el repositorio llama.cpp)
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
# Copiar los archivos del modelo Kimi K2 a una carpeta local
python3 convert.py --outfile k2_fp16.gguf --outtype f16 /path/to/kimi_k2_hf_model
```

### Paso 3.2: Cuantización a 4-bit (Q4_K_M)

El formato `Q4_K_M` ofrece un buen equilibrio entre tamaño de archivo y rendimiento.

```bash
# Ejecutar la cuantización
./quantize k2_fp16.gguf k2_q4_k_m.gguf Q4_K_M
```

El archivo resultante `k2_q4_k_m.gguf` tendrá un tamaño significativamente menor y estará listo para la inferencia en el borde.

## 4. Inferencia en Dispositivos Edge

### 4.1. NVIDIA Jetson Orin Nano (ARM64)

El Jetson Orin Nano se beneficia de la aceleración de GPU.

1.  **Instalación de `llama-cpp-python`:**
    ```bash
    # Asegúrese de que CUDA y el compilador sean compatibles
    pip3 install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/ --force-reinstall --no-cache-dir
    ```
2.  **Carga del Modelo:** El código de Amalia (en `software/ai_engine/llm_local.py`) cargará el archivo `.gguf` directamente.

### 4.2. Raspberry Pi 5 (ARM64)

El Raspberry Pi 5 se basa en la inferencia de CPU.

1.  **Instalación:** Se recomienda compilar `llama.cpp` directamente para optimizar el rendimiento del CPU.
2.  **Configuración:** Utilice el *binding* de Python para la inferencia. El rendimiento será limitado, por lo que se recomienda el modelo Phi-3 Mini cuantizado.

### 4.3. Qualcomm/Arduino (Microcontroladores)

Para microcontroladores, la inferencia de LLM se limita a modelos muy pequeños (ej. modelos de 100M de parámetros) o a la ejecución de modelos de *machine learning* tradicionales (ej. para detección de objetos) a través de **TensorFlow Lite (TFLite)**.

*   **Rol:** El microcontrolador se encarga de la ejecución de la **HAL** y el control de bajo nivel, dejando el razonamiento LLM al Jetson/Pi o a la nube (CorticalLabs NPU).

## 5. Manual de Operación Autónoma con Cloud Backup

**Ver archivo:** `autonomous_operation_manual.md`

Este manual detalla cómo el robot gestiona la conmutación entre el LLM local cuantizado (para respuesta rápida) y el **CorticalLabs NPU** (para razonamiento complejo y *Cloud Backup*).

*   **Modo Offline:** Utiliza el LLM cuantizado localmente.
*   **Modo Cloud Backup:** Utiliza el **API Gateway** para enviar solicitudes al Kimi K2 en el NPU.

---
*Este documento es parte de la documentación de producción del Proyecto Amalia Gamma (Terminator).*
