# Modelo 
## Uso de IDs autoincrementales como PK
Aunque el RUT del cliente o la Patente del vehículo son únicos, es una mejor práctica usar un ID numérico autoincremental como Clave Primaria. Si el cliente cambia de RUT por un error de digitación, o la patente cambia de formato, la integridad de las relaciones en la base de datos no se rompe.

## Dónde va la Clave Foránea (Regla del 1:N)
En una relación de "Uno a Muchos" (1:N), la Clave Foránea siempre se ubica en la entidad que tiene la cardinalidad "Muchos" (N). Por eso, Vehiculo lleva el cliente_id y Servicio lleva el vehiculo_id.

## Por qué se creó la quinta entidad
Las bases de datos relacionales no pueden almacenar relaciones "Muchos a Muchos" (N:M) de forma directa. Para resolverlo, se debe crear una tabla intermedia que contenga las claves foráneas de ambas tablas. (Nota: Cuando implementemos esto en Django, el framework creará esta tabla intermedia automáticamente usando el campo ManyToManyField)
