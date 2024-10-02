import boto3
import json

# Función principal para convertir PDF a JSON
def pdf_to_json(pdf_name, bucket_name, post_processed, region_name='us-east-1'):
    # Crear un cliente para S3 y Textract
    s3_client = boto3.client('s3', region_name=region_name)
    textract_client = boto3.client('textract', region_name=region_name)
    
    # Ruta del archivo en S3 URI
    document_s3_path = f's3://{bucket_name}/{pdf_name}'
    
    # Aquí se asume que pdfToJson es una función importable
    from pdfToJson import pdfToJson  
    
    # Guardar json en una variable   
    result = pdfToJson(document_s3_path, textract_client, post_processed)

    if result is None:
        raise ValueError("No se pudo procesar el archivo.")
    
    return result

# Función para guardar el resultado JSON en un archivo
def save_json(result, json_filename):
    # Guarda el resultado en un archivo JSON
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)
    print(f"Guardado {json_filename}")
