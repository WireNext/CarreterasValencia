import requests
import json

# URL del GeoJSON original
url = "https://geoportal.valencia.es/server/rest/services/OPENDATA/Trafico/MapServer/192/query?where=1=1&outFields=*&f=geojson"

# Descargar datos
response = requests.get(url)
data = response.json()

# Colores por estado
colores = {
    0: "#00FF00",  # verde
    5: "#00FF00",
    1: "#FFA500",  # naranja
    3: "#000000",  # negro
}

# Añadir estilo a cada feature
for feature in data['features']:
    estado = feature['properties'].get('estado')
    color = colores.get(estado, "#808080")  # Gris si no existe

    feature['properties']['_umap_options'] = {
        "color": color,
        "weight": 3,
        "opacity": 1
    }

# Guardar el nuevo GeoJSON
with open('trafico_valencia_umap.geojson', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("GeoJSON generado: trafico_valencia_umap.geojson")
