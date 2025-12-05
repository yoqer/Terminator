"""
robot_main.py - Punto de entrada principal para el software del robot Amalia Gamma.

Este archivo simula el nodo principal de ROS 2 que orquesta los módulos.
"""

import logging
import time
from hal.hal_interface import HALInterface
from training.hybrid_trainer import HybridTrainer, TrainingScenario

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_robot():
    """Inicializa el hardware y los subsistemas del robot."""
    logging.info("--- Inicializando Amalia Gamma ---")
    
    # Detección de plataforma (simulada)
    platform = "NVIDIA Jetson Orin Nano" # En producción, esto se detectaría automáticamente
    
    # 1. Inicializar HAL (Hardware Abstraction Layer)
    hal = HALInterface(platform=platform)
    if not hal.connect():
        logging.error("Fallo al conectar con el hardware. Abortando.")
        return None
    
    # 2. Inicializar subsistemas clave
    logging.info("Inicializando subsistema de Navegación (Movilidad Avanzada del 3er Robot)...")
    logging.info("Inicializando subsistema de Visión 3D (Visión Estéreo del 3er Robot)...")
    logging.info("Inicializando subsistema de Inferencia LLM (Kimi K2 Cuantizado)...")
    
    # 3. Inicializar el sistema de entrenamiento híbrido
    trainer = HybridTrainer(hal)
    
    logging.info("--- Inicialización Completa. Amalia en modo Operación Autónoma ---")
    return hal, trainer

def autonomous_operation(hal: HALInterface, trainer: HybridTrainer):
    """Bucle principal de operación autónoma."""
    logging.info("\n--- Iniciando Bucle de Operación Autónoma ---")
    
    # Simulación de un ciclo de percepción-acción
    for i in range(5):
        logging.info(f"\n--- Ciclo de Operación {i+1} ---")
        
        # 1. Percepción
        battery_data = hal.get_sensor_data('battery_level')
        vision_data = hal.get_sensor_data('depth_camera')
        logging.info(f"Estado de la Batería: {battery_data}")
        logging.info(f"Datos de Visión 3D recibidos: {vision_data['point_cloud_size']} puntos.")
        
        # 2. Planificación y Acción (SIMA 2 - Sim-to-Real)
        if battery_data.get('level', 0) < 0.2:
            logging.warning("Batería baja. Iniciando acción de recarga.")
            sima_scenario = TrainingScenario("Recarga de Emergencia", "SIMA 2", 1)
            trainer.run_sima2_sim_to_real_cycle(sima_scenario)
        else:
            # Simulación de una tarea de alto nivel
            sima_scenario = TrainingScenario("Tarea de Manipulación", "SIMA 2", 3)
            trainer.run_sima2_sim_to_real_cycle(sima_scenario)
            
        # 3. Entrenamiento en segundo plano (Genie 3 - Entrenamiento Programable)
        if i % 2 == 0:
            trainer.run_genie3_programmable_training("Practicar la navegación en un entorno con obstáculos inesperados.")
            
        time.sleep(1) # Simulación de tiempo de procesamiento

    logging.info("\n--- Operación Autónoma Finalizada ---")

if __name__ == "__main__":
    hal, trainer = initialize_robot()
    if hal and trainer:
        autonomous_operation(hal, trainer)
        hal.disconnect()
        
    logging.info("Programa principal finalizado.")
