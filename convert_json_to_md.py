import json
import os

def json_to_markdown(json_file, markdown_file):
    if not os.path.exists(json_file):
        print(f"Procesando archivo: {json_file}")
        
    with open(json_file, 'r', encoding='utf-8') as file:
        conversations = json.load(file)

    with open(markdown_file, 'w', encoding='utf-8') as file:
        # Iterar sobre cada conversación
        for chat_data in conversations:
            # Escribir información del chat
            file.write(f"# Conversación {chat_data['id']}\n\n")
            file.write(f"Última interacción: {chat_data['lastInteractionTimestamp']}\n\n")
            
            # Procesar cada interacción
            for interaction in chat_data['interactions']:
                # Mensaje humano
                human_message = interaction['humanMessage']
                file.write(f"## 👤 Humano\n\n{human_message['text']}\n\n")
                
                # Mensaje asistente
                assistant_message = interaction['assistantMessage']
                file.write(f"## 🤖 Asistente\n\n{assistant_message['text']}\n\n")
                
                file.write("---\n\n")
            
            # Separador entre conversaciones
            file.write("\n\n=================\n\n")

# Definición de rutas
json_file = 'C:/laragon/www/python/chat-2.json'
markdown_file = 'C:/laragon/www/python/chat-Cody.md'

try:
    json_to_markdown(json_file, markdown_file)
    print(f"¡Conversaciones convertidas exitosamente! Archivo guardado en: {markdown_file}")
except Exception as e:
    print(f"Error al procesar el archivo: {str(e)}")
