# Programación II: Primer Proyecto / Herbosa - Pereyra
Tecnicatura universitaria en Programación UTN FRBB - Octubre 2021
- Fecha de entrega: 1 de Noviembre de 2021

### Observaciones generales:
- La entrega será a partir de un repositorio Git que crearán en una cuenta en GitHub de UNO de los integrantes.
- Deben agregar como colaborador de ese repositorio a su compañero de comisión y a mi. El proyecto se hará en comisiones de 2 alumnos.
- Debe poder verse la evolución del proyecto a través de la historia del proyecto (no puede ser un solo commit con el proyecto entero).
- Cada ejercicio tendrá incisos opcionales, estos no son obligatorios para la aprobación pero subirán la nota del proyecto.
- Implemente todos los ejercicios en un mismo programa brindando al usuario un menú para seleccionar el ejercicio que desea ejecutar.

### Expresiones Regulares
1. Implemente una expresión regular para validar matrículas argentinas
2. Diseñe una ER para validar cadenas de números naturales menores a 1900

Opcional: Investigue las funciones para validar una dada cadena a partir de una ER en el lenguaje Python. Implemente una (mini)funcionalidad utilizando alguna de ellas

### Recursión
Especificar un planteo recursivo e implementar una solución para los siguientes problemas:
1. Codificar un número entero de la siguiente manera cada dígito par sustituirlo por 1, cada dígito impar por 2. Puede pasar el número a otras representaciones para resolver el ejercicio Ejemplo: El número 46579222 deberá codificarse como 11222111.
2. Convertir una lista de listas en una sola lista que tenga todos los elementos de las listas originales. Ejemplo: Si L = [ [1, 2, 3], [4, 5, 6], [7], [8] ] la lista resultante deberá ser L2 = [1,2,3,4,5,6,7,8]
3. Decidir si dos listas de números enteros son iguales.
4. Realizar la división entera entre dos números enteros positivos A y B, (B ≠ 0). Ayuda: Pensar la división entera como sucesión de restas

Opcional: Plantear 3 problemas sobre secuencias y plantear sus respectivas soluciones recursivas. Antes
de resolverlo, escribir en el foro los enunciados pensados para evitar planteos iguales.

### Colecciones
1. Explicar en pocas palabras y utilizando diagramas las operaciones de map, filter y reduce. Proponga
ejemplos de cada uno (conceptuales, no necesariamente en código).
2. El número irracional “pi” puede calcularse a partir de la serie: Sumatoria de 0 a infinito de [4(-1)^i] / 2i + 1  Implemente un algoritmo sin usar estructuras repetitivas para calcular una aproximación de pi con N
términos.


### Formato de intercambios de datos
Diseñar un formato XML y uno JSON para intercambiar datos del sistema. Cree dos documentos para almacenar la misma información. El formato debería ser eficiente para computar lo siguiente:
1. A partir del nombre de la estación, computar la cantidad de sensores disponible y mostrar por pantalla los diferentes sensores, cada uno deberá mostrar el tipo y la variable medida
2. Calcular cuál es la estación con menos batería, es decir, la estación con menor valor promedio de voltaje.
Elija solo una representación (XML o JSON) para implementar las soluciones de 1 y 2.
Opcional: Implemente la solución utilizando la representación restante.
