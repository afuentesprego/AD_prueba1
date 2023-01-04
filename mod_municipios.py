# Procesado de fichero de datos municipales
# 2023 Alberto Fuentes

# LIBRERIAS
# =======================================================================

# Librerías de tratamiento de datos
import pandas as pd
import numpy as np

# Librerías gráficos
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Librerías preprocesado y análisis
# >> conda install -c conda-forge pingouin
#import statsmodels.api as sm
#import pingouin as pg 
#from scipy import stats
#from scipy.stats import pearsonr 

# Configuración matplotlib
plt.style.use('ggplot')

# Ignoramos warnings
import warnings
warnings.filterwarnings('ignore')


# LECTURA DE DATOS
# =======================================================================

# importamos fichero
df = pd.read_excel('Fichas_Municipales_2021.xlsx')

# Mostramos las columnas
print(df.columns.ravel())


# GRAFICOS
# =======================================================================


fig, axs = plt.subplots(1,2,figsize=(6,4))

# Scatterplot poblacion vs parque turismos
axs[0].scatter(x=df.poblacion_total,y=df.parque_turismos,alpha=0.8)
axs[0].set_xlabel('Poblacion total')
axs[0].set_ylabel('Parque turismos')

print('Correlación Pearson: ', df['poblacion_total'].corr(df['parque_turismos'],method='pearson'))

# Histograma antigüedad media
axs[1].hist(x=df.antig_media_turismos,bins=20,color="#3182bd",alpha=0.5)
axs[1].set_title('Histograma antigüedad media')
axs[1].set_xlabel('Antiguedad media')
axs[1].set_ylabel('Cuenta')

plt.tight_layout
plt.show()