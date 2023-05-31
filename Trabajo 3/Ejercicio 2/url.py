import re
def verificar_url(url):
    patron = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9-]+)?(\?[a-zA-Z0-9-]+(=[a-zA-Z0-9-]+)?(&[a-zA-Z0-9-]+(=[a-zA-Z0-9-]+)?)*)?$'

    if re.match(patron, url):
        print(f'La URL "{url}" es válida.')
    else:
        print(f'La URL "{url}" no es válida.')
ruta_archivo = 'ejemplo.txt'
try:
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            url = linea.strip()
            verificar_url(url)
except FileNotFoundError:
    print(f'No se pudo encontrar el archivo "{ruta_archivo}".')
except Exception as e:
    print(f'Ocurrió un error: {str(e)}')
