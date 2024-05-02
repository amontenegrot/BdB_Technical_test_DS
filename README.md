# Data Scientist - Prueba técnica

Aquí puedes describir el objetivo de tu proyecto, la metodología que estás utilizando, y los resultados que esperas obtener.

# Installation

To install the necessary dependencies for this project, you can use pip:

```bash
pip install -r requirements.txt
```

# Uso

Explica cómo usar tu proyecto. Por ejemplo, puedes incluir ejemplos de código o instrucciones para ejecutar scripts.

# Conjunto de Datos

## Descripción General

Aquí puedes describir el conjunto de datos que estás utilizando. Explica de dónde proviene, qué representa, y cualquier característica importante que deba conocer el lector.

## Diccionario de Variables

Aquí puedes describir cada una de las variables o columnas en tu conjunto de datos. Por ejemplo:

- **ID** `(númerica)`: Identificación del cliente.
- **Edad** `(númerica)`: Edad del cliente.
- **Tipo_Trabajo** `(categórica)`: Trabajo ejercido por el cliente. *datos desconocidos*
- **Estado_Civil** `(categórica)`: Estado civil del cliente. *error tipografico* y *datos desconocidos*
- **Educacion** `(categórica)`: Nivel educativo alcanzado por el cliente. *datos desconocidos*
- **mora** `(categórica)`: Informa si el cliente se encuentra en mora. *datos desconocidos*
- **Vivienda** `(categórica)`: Informa si el cliente cuenta con vivienda propia. *datos desconocidos*
- **Consumo** `(categórica)`: Informa si el cliente presenta consumo. *datos desconocidos*
- **Contacto** `(categórica)`: Tipo de medio por el cual el cliente es contactado.
- **Mes** `(categórica)`: Mes del contacto.
- **Dia** `(categórica)`: Día del contacto.
- **Campana** `(categórica)`: Número de identificación de la campaña.
- **Dias_Ultima_Camp** `(númerica)`: Días transcurridos desde el último contacto en otra campaña. *outliers*
- **No_Contactos** `(númerica)`: Número de veces que se ha contactado al cliente.
- **Resultado_Anterior** `(categórica)`: Resultado obtenido en la campaña previa.
- **emp_var_rate** `(númerica)`: (Tasa de variación del empleo)`: Este indicador mide la estabilidad del empleo del cliente. Un valor alto puede indicar que el cliente tiene un empleo estable, lo que podría influir en su capacidad para pagar los productos del banco.
- **cons_price_idx** `(númerica)`: el índice de precios al consumidor es un indicador que mide el nivel de vida del cliente. Un valor alto puede indicar que el cliente vive en un área con un alto costo de vida. Un aumento en este índice indica inflación, lo cual puede afectar el poder adquisitivo de los clientes del banco.
- **cons_conf_idx** `(númerica)`: El índice de confianza del consumidor es un indicador que mide el grado de optimismo que los consumidores sienten sobre el estado general de la economía. Un valor más alto indica un mayor nivel de confianza, lo cual puede traducirse en mayor disposición para gastar y, por ende, mayor actividad bancaria.
- **euribor3m** `(númerica)`: La tasa Euribor a 3 meses es un indicador de la tasa de interés a la que los bancos se prestan dinero entre sí a corto plazo. Si esta tasa es baja, significa que es más barato para los bancos pedir prestado dinero, lo que podría llevar a tasas de interés más bajas para los préstamos y productos de ahorro, incentivando a las personas a pedir más préstamos o invertir en productos de ahorro. Por otro lado, si esta tasa es alta, significa que es más caro para los bancos pedir prestado dinero, lo que podría resultar en tasas de interés más altas para los préstamos y productos de ahorro, desalentando a las personas a pedir préstamos o invertir en productos de ahorro.
- **nr_employed** `(categórica)`: Identificación del agente por el cual fue contactado el cliente.
- **y** `(categórica)`: Variable objetivo que indica si el cliente ha aceptado una tarjeta de crédito.

# Contribuciones

Si estás abierto a contribuciones, aquí puedes describir cómo otros pueden contribuir a tu proyecto.

# Licencia

Incluye información sobre la licencia bajo la cual se distribuye tu proyecto.

# Contacto

Proporciona información de contacto para las personas que puedan tener preguntas o comentarios sobre tu proyecto.
