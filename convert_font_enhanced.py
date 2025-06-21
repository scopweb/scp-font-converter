#!/usr/bin/env python3
"""
Enhanced Font Converter using FontTools
Supports: TTF → WOFF, TTF → WOFF2, WOFF → WOFF2, OTF → WOFF2
"""

from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter
import sys
import os
import json
from pathlib import Path

def get_font_info(font_path):
    """Extrae información básica de la fuente"""
    try:
        font = TTFont(font_path)
        
        # Obtener nombre de la fuente
        name_table = font['name']
        font_name = "Unknown"
        font_family = "Unknown"
        
        for record in name_table.names:
            if record.nameID == 1:  # Font Family
                font_family = record.toUnicode()
            elif record.nameID == 4:  # Full Font Name
                font_name = record.toUnicode()
        
        # Obtener número de glifos
        glyph_count = len(font.getGlyphSet())
        
        # Obtener formato original
        if 'CFF ' in font:
            original_format = "OTF"
        else:
            original_format = "TTF"
            
        font.close()
        
        return {
            "name": font_name,
            "family": font_family,
            "glyphs": glyph_count,
            "format": original_format
        }
    except Exception as e:
        return {"error": str(e)}

def convert_font(input_path, output_path, target_format, options=None):
    """
    Convierte fuente a formato especificado
    
    Args:
        input_path: Ruta del archivo fuente
        output_path: Ruta de salida
        target_format: 'woff' o 'woff2'
        options: Diccionario con opciones adicionales
    """
    try:
        # Cargar fuente
        font = TTFont(input_path)
        
        # Aplicar subset si se especifica
        if options and options.get('subset'):
            subsetter = Subsetter()
            subsetter.options.desubroutinize = True
            subsetter.options.remove_hinting = options.get('remove_hinting', False)
            
            # Caracteres a mantener (opcional)
            chars = options.get('characters')
            if chars:
                subsetter.populate(text=chars)
            else:
                # Mantener caracteres básicos latinos
                subsetter.populate(unicodes=range(0x20, 0x7F))
            
            subsetter.subset(font)
        
        # Configurar formato de salida
        if target_format.lower() == 'woff':
            font.flavor = 'woff'
        elif target_format.lower() == 'woff2':
            font.flavor = 'woff2'
        else:
            raise ValueError(f"Formato no soportado: {target_format}")
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Guardar fuente
        font.save(output_path)
        font.close()
        
        # Obtener tamaños de archivo
        input_size = os.path.getsize(input_path)
        output_size = os.path.getsize(output_path)
        compression_ratio = ((input_size - output_size) / input_size) * 100
        
        return {
            "success": True,
            "input_size": input_size,
            "output_size": output_size,
            "compression": f"{compression_ratio:.1f}%",
            "output_file": os.path.basename(output_path)
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def main():
    if len(sys.argv) < 4:
        print("Uso: python convert_font_enhanced.py <input> <output> <format> [options]")
        print("Formatos: woff, woff2")
        print("Opciones (JSON): '{\"subset\": true, \"remove_hinting\": false}'")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    target_format = sys.argv[3]
    
    # Opciones adicionales (opcional)
    options = {}
    if len(sys.argv) > 4:
        try:
            options = json.loads(sys.argv[4])
        except:
            pass
    
    # Verificar archivo de entrada
    if not os.path.exists(input_path):
        print(json.dumps({"success": False, "error": "Archivo de entrada no encontrado"}))
        sys.exit(1)
    
    # Obtener información de la fuente
    font_info = get_font_info(input_path)
    
    # Convertir fuente
    result = convert_font(input_path, output_path, target_format, options)
    
    # Combinar resultados
    result.update({"font_info": font_info})
    
    # Imprimir resultado como JSON
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()