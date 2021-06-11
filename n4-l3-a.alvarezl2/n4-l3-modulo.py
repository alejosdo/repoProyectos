import pandas as pd
from matplotlib import pyplot as pplot


def cargar_df(nombre_archivo: str):
    df = pd.read_csv(nombre_archivo)
    return df


def absolute_value(val):
    return round(val*(df_MinusCV.ValorMilesDolar.sum()/100), 2)


def absolute_value0(val):
    return round(val*(df_2016.ValorMilesDolar.sum()/100), 2)


def absolute_value1(val):
    return round(val*(df_2017.ValorMilesDolar.sum()/100), 2)

def absolute_value2(val):
    return round(val*(df_2018.ValorMilesDolar.sum()/100), 2)


def exportar_resumen_exp():
    salida = df.Anio.unique()
    with open('reporte.txt', 'w', encoding = "utf-8") as f:
        f.write('Reporte de exportaciones por año por Departamento\n')
        linea = f.write("-" * 60 + "\n")
        linea = f.write("-" * 60 + "\n")
        for anio in salida:
            df_temp = df[df.Anio == anio]
            f.write('Año: '+str(anio)+'\n')
            linea = f.write("-" * 60 + "\n")
            f.write( str(df_temp.groupby('DepartamentoOrigen').ValorMilesDolar.sum()) +"\n")
            linea = f.write("-" * 60 + "\n")
        f.close()

#Primer punto
df = cargar_df('exportaciones.csv')
#Segundo punto
df.groupby('Producto').ValorMilesDolar.sum().plot.pie(y='Producto',legend=True)
pplot.gcf().canvas.set_window_title("Segundo punto")
pplot.show()
#Tercer punto
df_MinusCV = df[(df.Producto != "Cavendish Valery")]
df_MinusCV.groupby('Producto').ValorMilesDolar.sum().plot.pie(y='Producto',legend=True, autopct=absolute_value, title = "minus Cavendish")
pplot.gcf().canvas.set_window_title("Tercer punto")
pplot.show()
#Tercer punto, 2016
df_2016 = df[(df.Anio == 2016)]
df_2016.groupby('Producto').ValorMilesDolar.sum().plot.pie(y='Anio',legend=True, autopct=absolute_value0, title = 2016)
pplot.gcf().canvas.set_window_title("Tercer punto, 2016")
pplot.show()
#Tercer punto, 2017
df_2017 = df[(df.Anio == 2017)]
df_2017.groupby('Producto').ValorMilesDolar.sum().plot.pie(y='Anio',legend=True, autopct=absolute_value1, title = 2017)
pplot.gcf().canvas.set_window_title("Tercer punto, 2017")
pplot.show()
#Tercer punto, 2018
df_2018 = df[(df.Anio == 2018)]
df_2018.groupby('Producto').ValorMilesDolar.sum().plot.pie(y='Anio',legend=True, autopct=absolute_value2, title = 2018)
pplot.gcf().canvas.set_window_title("Tercer punto, 2018")
pplot.show()
exportar_resumen_exp()
#Cuarto punto
df.groupby('Anio').ValorMilesDolar.sum().plot(kind = "bar", y='ValorMilesDolar',legend=True, color = ["cyan", "red", "black","green","blue"])
pplot.gcf().canvas.set_window_title("Cuarto punto")
pplot.show()
#Quinto punto, parte 1
fig, ax =pplot.subplots()
data=df.groupby('PaisDestino')[['Cantidad']].sum().nlargest(5,'Cantidad',keep='first')
ax.barh(data.index,data['Cantidad'], color = ["cyan", "red", "black","green","blue"])
pplot.title('Los Países que más importan banano:')
pplot.ylabel("Kilos importados")
pplot.xlabel("País")
pplot.gcf().canvas.set_window_title("Quinto punto, parte 1")
pplot.show()
#Quinto punto, parte 2
fig, ax =pplot.subplots()
data=df.groupby('PaisDestino')[['Cantidad']].sum().nsmallest(5,'Cantidad',keep='first')
ax.barh(data.index,data['Cantidad'], color=["cyan", "red", "black","green","blue"])
pplot.title('Los países que menos importan banano:')
pplot.ylabel("Kilos importados")
pplot.xlabel("País")
pplot.gcf().canvas.set_window_title("Quinto punto, parte 2")
pplot.show()