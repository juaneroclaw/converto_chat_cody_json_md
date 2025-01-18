# Explicación del Convertidor JSON a Markdown

## Descripción General
Este script Python está diseñado para convertir archivos JSON en formato Markdown (.md).

## Componentes Principales

### Importaciones
- `json`: Para manejar archivos JSON
- `os`: Para operaciones con el sistema de archivos

### Función Principal
`json_to_markdown(json_file, markdown_file)`
- Parámetro 1: Ruta del archivo JSON de entrada
- Parámetro 2: Ruta del archivo Markdown de salida

### Funcionalidad
1. Verifica la existencia del archivo JSON
2. Lee el contenido del archivo JSON
3. Crea un archivo Markdown
4. Convierte la estructura JSON en formato Markdown
5. Escribe los datos formateados en el archivo .md

## Estructura del Markdown Generado
- Título de la conversación con ID
- Timestamp de la última interacción

## Para ejecutar la conversión, puedes usar este comando:

`python convert_json_to_md.py`