# Librerías
import plotly.express as px

# Funciones
from Funciones.Crear_carpetas import crear_carpetas

def curva_de_luz_reducida(nombre_cometa, curva_de_luz_procesada_df, tipo_de_grafica):
    labels = {'obs_date':'Observation Date','magnitud_reducida':'Apparent total magnitude reduced', 'obs_method_key' : 'Observation Method'}
    titulo = f'Reduced lightcurve of {nombre_cometa}'

    ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo, tipo_de_grafica)

    fig = px.scatter(curva_de_luz_procesada_df, x='obs_date', y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    fig.write_image(ruta_archivos_graficas)
    # fig.show()
    
    print('✅ Creada: curva de luz reducida creada.')

    if __name__ == '__main__':
        curva_de_luz_reducida()