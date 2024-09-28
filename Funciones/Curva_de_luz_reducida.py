import os
from pathlib import Path
import plotly.express as px

def curva_de_luz_reducida(nombre_cometa, curva_de_luz_procesada_df):
    labels = {'obs_date':'Observation Date','magnitud_reducida':'Apparent total magnitude processed', 'obs_method_key' : 'Observation Method'}
    titulo = f'Reduced lightcurve of {nombre_cometa}'

    carpeta_cometa = Path('Graficas', nombre_cometa.replace('/', '_'))
    ruta_archivos_graficas = f'{carpeta_cometa}/{titulo.replace('/', '_')}.png'
    
    if not os.path.exists(carpeta_cometa):
        Path.mkdir(carpeta_cometa)

    fig = px.scatter(curva_de_luz_procesada_df, x='obs_date', y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    fig.write_image(ruta_archivos_graficas)
    # fig.show()
    print('✅ Creada: curva de luz reducida creada.')

    if __name__ == '__main__':
        curva_de_luz_reducida()