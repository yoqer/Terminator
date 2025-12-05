# /home/ubuntu/robot_software_dev/desktop_software/control_ui.py
# Interfaz de Usuario de Control Local (Simulación de Escritorio)

import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import json

# URL simulada del API Gateway de Amalia (que orquesta el MCCE)
API_GATEWAY_URL = "http://amalia.userhosting.com/api/v1"

class RobotControlUI:
    """
    Simulación de una interfaz de escritorio para interactuar con el robot y el MCCE.
    """
    def __init__(self, master):
        self.master = master
        master.title("Amalia Gamma Robot Control & Training UI")

        # --- Título ---
        tk.Label(master, text="Gestión de Entrenamiento y Control del Robot", font=("Arial", 16)).pack(pady=10)

        # --- Sección de Ingesta de Contenido (MCCE) ---
        frame_ingesta = tk.LabelFrame(master, text="1. Ingesta de Contenido para Entrenamiento (MCCE)", padx=10, pady=10)
        frame_ingesta.pack(padx=10, pady=5, fill="x")

        tk.Label(frame_ingesta, text="Ruta del Archivo:").grid(row=0, column=0, sticky="w")
        self.file_path_entry = tk.Entry(frame_ingesta, width=50)
        self.file_path_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_ingesta, text="Seleccionar Archivo", command=self.select_file).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(frame_ingesta, text="Tipo de Contenido:").grid(row=1, column=0, sticky="w")
        self.content_type_var = tk.StringVar(master)
        self.content_type_var.set("video") # default value
        content_types = ["video", "instructions", "dataset", "game_log"]
        tk.OptionMenu(frame_ingesta, self.content_type_var, *content_types).grid(row=1, column=1, sticky="w", padx=5, pady=5)

        tk.Button(frame_ingesta, text="Enviar a Análisis Autónomo (Kimi K2)", command=self.send_to_mcce).grid(row=2, column=0, columnspan=3, pady=10)

        # --- Sección de Control Directo (Simulación) ---
        frame_control = tk.LabelFrame(master, text="2. Control Directo del Robot (Simulación)", padx=10, pady=10)
        frame_control.pack(padx=10, pady=5, fill="x")

        tk.Label(frame_control, text="Comando de Alto Nivel:").grid(row=0, column=0, sticky="w")
        self.command_entry = tk.Entry(frame_control, width=50)
        self.command_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_control, text="Enviar Comando", command=self.send_command).grid(row=0, column=2, padx=5, pady=5)

        # --- Log de Estado ---
        self.log_text = tk.Text(master, height=10, width=70)
        self.log_text.pack(padx=10, pady=10)
        self.log_message("UI de Control Inicializada. Conectando con API Gateway...")

    def select_file(self):
        """Abre un diálogo para seleccionar un archivo."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def log_message(self, message):
        """Añade un mensaje al log de la UI."""
        self.log_text.insert(tk.END, f"[{tk.StringVar(self.master, value='').get()}] {message}\n")
        self.log_text.see(tk.END)

    def send_to_mcce(self):
        """Simula el envío de contenido al MCCE a través del API Gateway."""
        file_path = self.file_path_entry.get()
        content_type = self.content_type_var.get()
        
        if not file_path:
            messagebox.showerror("Error", "Por favor, selecciona un archivo.")
            return

        self.log_message(f"Enviando {content_type} ({file_path}) al MCCE para análisis...")
        
        # Simulación de la llamada API
        try:
            # En un entorno real, esto subiría el archivo y llamaría a la API
            # Aquí solo simulamos la respuesta exitosa
            response = {
                "status": "success",
                "message": "Contenido enviado. Kimi K2 está analizando y generando el escenario de entrenamiento virtual (Britetrainer)."
            }
            self.log_message(f"API Response: {response['message']}")
        except Exception as e:
            self.log_message(f"Error de conexión con API Gateway: {e}")

    def send_command(self):
        """Simula el envío de un comando de alto nivel al robot."""
        command = self.command_entry.get()
        if not command:
            messagebox.showerror("Error", "Por favor, introduce un comando.")
            return

        self.log_message(f"Enviando comando de alto nivel: '{command}'")
        
        # Simulación de la llamada API
        try:
            # En un entorno real, esto llamaría al API Gateway para la planificación de tareas
            response = {
                "status": "success",
                "message": f"Comando '{command}' recibido. Kimi K2 planifica la secuencia de acción."
            }
            self.log_message(f"Robot Status: {response['message']}")
        except Exception as e:
            self.log_message(f"Error de conexión con API Gateway: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotControlUI(root)
    # Nota: En el sandbox no se puede ejecutar la UI gráfica, esto es solo la estructura del código.
    # root.mainloop()
    print("Estructura de la UI de Control Local generada en control_ui.py")
