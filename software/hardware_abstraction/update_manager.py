# /home/ubuntu/robot_software_dev/hardware_abstraction/update_manager.py
# Sistema de Actualización Agnostico al Chip (OTA/USB)

from typing import Dict, Any
from hal_interface import get_hal_instance, HardwareAbstractionLayer

class UpdateManager:
    """
    Gestiona el proceso de actualización de software/firmware de forma agnóstica al chip.
    """
    def __init__(self, chip_type: str):
        try:
            self.hal: HardwareAbstractionLayer = get_hal_instance(chip_type)
            print(f"UpdateManager inicializado para chip: {self.hal.get_chip_info()}")
        except ValueError as e:
            print(f"Error de inicialización: {e}")
            self.hal = None

    def check_for_updates(self, current_version: str) -> Dict[str, Any]:
        """
        Simula la comprobación de actualizaciones en el servidor de la nube.
        """
        print(f"Comprobando actualizaciones para {self.hal.get_chip_info()} (Versión actual: {current_version})...")
        
        # Simulación de la respuesta del servidor de la nube (API Gateway)
        if self.hal.get_chip_info() == "Jetson Orin Nano" and current_version < "v2.1":
            return {
                "update_available": True,
                "version": "v2.1",
                "update_type": "software_image",
                "download_url": "http://amalia.cloud/updates/ros_v2.1.tar.gz"
            }
        elif self.hal.get_chip_info() == "Arduino Due" and current_version < "v1.5":
            return {
                "update_available": True,
                "version": "v1.5",
                "update_type": "firmware_hex",
                "download_url": "http://amalia.cloud/updates/firmware_v1.5.hex"
            }
        else:
            return {"update_available": False, "message": "Sistema actualizado."}

    def download_update(self, url: str, filename: str) -> str:
        """
        Simula la descarga del archivo de actualización.
        """
        print(f"Descargando actualización desde {url}...")
        # En un entorno real, se usaría 'requests' para descargar.
        local_path = f"/tmp/{filename}"
        print(f"Descarga completada. Archivo guardado en {local_path}")
        return local_path

    def apply_update(self, current_version: str) -> bool:
        """
        Ejecuta el proceso de actualización utilizando la HAL.
        """
        if not self.hal:
            print("No se pudo inicializar la HAL. Abortando actualización.")
            return False

        update_info = self.check_for_updates(current_version)

        if update_info["update_available"]:
            print(f"Actualización {update_info['version']} disponible. Tipo: {update_info['update_type']}")
            
            # 1. Descargar
            filename = f"{self.hal.get_chip_info().replace(' ', '_')}_{update_info['version']}.update"
            update_path = self.download_update(update_info["download_url"], filename)
            
            # 2. Aplicar actualización a través de la HAL
            success = self.hal.update_firmware(update_path)
            
            if success:
                print(f"Actualización a la versión {update_info['version']} completada con éxito.")
                return True
            else:
                print("Error al aplicar la actualización.")
                return False
        else:
            print(update_info["message"])
            return True

# Ejemplo de uso
if __name__ == "__main__":
    # Caso 1: Jetson Orin Nano (necesita actualización)
    jetson_updater = UpdateManager("Jetson Orin Nano")
    jetson_updater.apply_update("v2.0")

    print("\n" + "=" * 30 + "\n")

    # Caso 2: Arduino Due (necesita actualización)
    arduino_updater = UpdateManager("Arduino Due")
    arduino_updater.apply_update("v1.0")

    print("\n" + "=" * 30 + "\n")

    # Caso 3: Chip desconocido (fallo)
    try:
        unknown_updater = UpdateManager("Qualcomm Snapdragon Robotics RB5")
    except ValueError as e:
        print(f"Prueba de fallo: {e}")
