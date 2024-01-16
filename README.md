# Homicidios por siniestros viales en la Ciudad Autónoma de Buenos Aires

## Introuccion

Proyecto que simula el rol de Data Analist que forma parte del equipo de analistas que lleva a cabo una consultoria para el Observatorio de Movilidad y Seguridad Vial (OMSV), el centro de estuddios que se encuentra bajo la orbita de la Secretaria de Transporte del Gobierno de la Ciudad Autonoma de Buenos Aires(CABA) 

Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y que pueden tener diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden tener consecuencias que van desde daños materiales hasta lesiones graves o fatales para los involucrados.

La Ciudad Autónoma de Buenos Aires, que se ubica en la provincia de Buenos Aires en Argentina, no es la excepción a esta problemática, sino que los siniestros viales son una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden tener un impacto significativo en la seguridad de los residentes y visitantes de la ciudad, así como en la infraestructura vial y los servicios de emergencia.

Actualmente, según el censo poblacional realizado en el año 2022, la población de CABA es de 3,120,612 de habitantes en una superficie de 200 km cuadrados
, lo que implica una densidad de aproximadamente 15,603 hab/ km cuadrado. Sumado a esto, el Julio de 2023 se registraron 12,437,735 de vehículos transitando por los peajes de las autopistas de acceso a CABA. Por lo que la prevención de siniestros viales y la implementación de políticas efectivas son esenciales para abordar este problema de manera adecuada.

## Datos

Para este proyecto se trabajó con la Bases de Víctimas Fatales en Siniestros Viales que se encuentra en formato de Excel y contiene dos pestañas de datos:

HECHOS: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.
VICTIMAS: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho.
En este documento se detallan todas las definiciones manejadas en los datos y en el desarrollo de este proyecto. Por otra parte, en este link se encuentran los datos utilizados en el análisis.

## ETL y EDA

En primer lugar, se realizó un proceso de extracción, transformación y carga de los datos (ETL), tanto de "HECHOS" como "VÍCTIMAS", donde se estandarizaron nombres de las variables, se analizaron nulos y duplicados de los registros, se eliminaron columnas redundantes o con muchos valores faltantes, entre otras tareas. Una vez finalizado este proceso para los dos conjuntos de datos de "Homicidios" se procedió a unir los dos conjuntos en uno solo denominado df_homicidios.

[ETL](https://github.com/N-Ange/PI_DA-Homicidios-CABA/blob/main/Jupyter/01_ETL.ipynb) 

En segundo lugar, se procedió a realizar un análisis exploratorio exahustivo (EDA), con la finalidad de encontrar patrones que permitan generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales.
[EDA](https://github.com/N-Ange/PI_DA-Homicidios-CABA/blob/main/Jupyter/02_EDA.ipynb)

## Analisis de Datos

Lo primero que se analizó fue variable temporal, para entender la distribución de los homicidios en distintas escalas temporales. La distribución anual de la cantidad de víctimas fatales es de alrededor del 60% para los primeros 3 años del conjunto de datos, con una disminución marcada para el 2020 como consecuencia de la cuarentena por COVID 19. El comportamiento a lo largo del año, es decir, la variación mensual, si bien para todo el conjunto de datos es marcada, con un pico de víctimas en Diciembre, esta tendencia no se observa tan claramente entre los distintos años. Este resultado de la mayor cantidad de víctimas en Diciembre está influenciada por la flexibilización de las medidas tomadas por la cuarentena.

Luego, bajando en la escala temporal, se ve que el 70% de las victimas perdieron la vida en entre lunes y viernes, lo que haría pensar que se debe al traslado diario al trabajo, pero en la distribución semanal no se observan diferencias significativas entre los distintos días. Es decir, la cantidad de víctimas un sábado o un domingo, para todo el conjunto de datos, es aproximadamente el mismo.

Si se analizan las franjas horarias, las mayores víctimas, que representa el 12% de las víctimas, se presentaron en el horario entre las 6 a 8 de la mañana, lo que también hace pensar en el horario de ingreso a los trabajos. Pero si se analiza esta franja en particular, se observa que el 55% de estas víctimas resultaron de hechos ocurridos durante el fin de semana.

Lo siguiente que se hizo fue analizar el perfil de la víctima. En primero lugar se ve que el 77% de las víctimas son masculinas. Casi el 50% de las víctimas se encuentran en un rango etario entre los 25 a 25 años de edad, de los cuales entre el 84% de ellos son masculinos.

Si se observa que rol de la víctima, es decir la posición relativa que ocupaba al momento del hecho, el 48% era conductor. En particular, este 48% se distribuye en un 77% de víctimas que se movilizaban en moto y 19% en auto. En relación a la cantidad de víctimas según el medio de transporte al momento del hecho, el 42% de las víctimas son conductores de moto, de los cuales el 88% de los conductores de moto son masculino.

Asimismo, si se analiza la responsabilidad en el hecho, es decir, el vehículo que ocupaba quien resultó acusado, en el 29% de los casos fue el auto, pero en el 75% son responsabilidad de vehículos como auto, colectivos y camiones.

Por último, se buscaron patrones en la distribución espacial de los hechos. Lo que se destaca de este análisis, es que en todas las comunas de CABA se presenta como factor común los accidentes en las avenidas, que son vías arteriales de calzada ancha, de por lo menos 13 metros. El 62% de las víctimas perdió la vida en avenidas. En particular, en el 82% ocurrió en el cruce de las avenidas con otra calle. Esta es un comportamiento que se mantiene entre los distintos años. En cuanto al rol de la víctima al momento del hecho, en las distintas comunas varía entre moto y peatón.

## Kpi 

* *Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior*

Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Se define como Tasa de homicidios en siniestros viales al número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico, en este caso se toman 6 meses.

Como Población Total se calculó la población para el año 2021 a partir de los censos poblacionales del año 2010 y 2022.

En este caso, para el año 2021, la Tasa de homicidios en siniestros viales fue de 1.77 lo que significa que, durante los primeros 6 meses del año 2021, hubo aproximadamente 1.77 homicidios en accidentes de tránsito por cada 100,000 habitantes. Ahora, el objetivo planteado es reducir esta tasa para el siguiente semestre de 2021 en un 10%, esto es 1.60. Cuando se calcula el KPI para este período se obtiene que la Tasa de homicidios en siniestros viales fue de 1.35, lo que significa que para el segundo semestre de 2021 se cumple con el objetivo propuesto.



* *Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior*

Como se vio en el análisis exploratorio, el 42% de las víctimas mortales se transportaban en moto al momento del hecho. Por lo que se consideró importante proponer el monitoreo de la cantidad de accidentes mortales en este tipo de conductor. Para ello se define a la Cantidad de accidentes mortales de motociclistas como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal.

* *Reducir un 10% la cantidad de accidentes mortales en cruces en el ultimo año, en CABA, respecto al año anterior*

El 75% de las victimas son en cruces de calles, por lo que se es importante analizar los factoreres que llevan a cabo esto, por lo tanto se analizo el total de las victimas en cruces en determinado tiempo.


Entre los años 2016 a 2021 se registraron 716 víctimas fatales en accidentes de tránsito. El 70% de las víctimas se registraron durante la semana. Diciembre es el mes que resulta con el máximo de fallecimientos en el período analizado.

El 77% de las víctimas fatales fueron de sexo masculino, de los cuales mas del 60% tenía entre 16 y 44 años de edad. En relación al tipo de usuario, el 42% fueron motociclistas. El 61% de los homicidios ocurrió en algún punto de las avenidas de CABA, el 75% de los hechos ocurrieron en cruces de calles.

Finalmente, para el segundo semestre del año 2021, se cumplió con el objetivo de bajar la tasa de homicidios en siniestros viales, pero no se cumplieron los objetivos de reducir la cantidad de accidentes mortales en motociclistas ni en cruces para el año 2021 respecto del año 2020.(Esto ultimo puede ser influido por la pandemia de Covid-19)

En función de lo anterior, se hacen las siguientes recomendaciones:

* Continuar monitoreando los objetivos propuestos acompañados de campañas puntuales, en especial a conductores de motos y usuarios de las avenidas.
* Reforzar las campañas de seguridad vial entre los días viernes a lunes, intensificando particularmente en el mes de Diciembre.
* Puntualizar campañas de conducción segura en avenidas y cruces de calles.
* Dirigir las campañas de seguridad hacia el sexo masculino, especialmente en cuanto a conducción en moto, para un rango etario entre los 15 a 44 años.


### Enlaces utiles:
Link a mi perfil de [Linkedin](https://www.linkedin.com/in/nadirangelini/)