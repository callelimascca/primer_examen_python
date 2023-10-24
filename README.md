# Primer Examen de Python
### Pasos para el desarrollo del examen
### 1. instalacion de entorno virtual y modulos
1. primero hacemos `fork` del repositorio del proyecto
2. clonar el examen desde nuestro repositorio
   ```bash
   git clone url/ejemplo
   ```
3. accedemos al repositorio clonado
   ```bash
   cd nombreRepo
   ```
4. abrimos un area de trabajo a partir de la carpeta clonada en nuestro visual studio code.
5. una vez en el area de trabajo con la carpeta del examen abrimos nueva terminal y creamos un entorno virtual
   ```bash
   python -m venv venv
   ```
   ##### Observacio: esto creara un entorno virtula venv
6. activamos nuestro entorno virtual
    ##### bash: ejemplo
   ```bash
   source venv/Script/activate
   ```
   ##### Power Shell: ejemplo
   ```bash
   .\venv\Script\Activate.ps1
   ```
7. instalar pytest
   ```bash
   pip install pytest
   ```
### 2. pasos para la solucion de los ejercios
1. nos ubicamos en la siguiente direccion `src/main.py`
   
   ![Alt text](image.png)
2. dentro del archivo encontraremos los ejericion con la siguiente estructura
   ##### ejemplo ejercicio
   ```python
   # primero ira el enuncia del ejercicio

   #1.la funcion devera devolver la resta de dos numeros pasos por parametro

   #luego esta la funcion creada
   def resta(a,b):
      pass # aqui tendremos que reemplazar pass por nuestra respuesta

   ```
   ##### ejemplo de solucion 1
   ```python
   #1.la funcion devera devolver la resta de dos numeros pasados por parametro
   def resta(a,b):
      resta=a-b
      return resta

   ```
   ##### ejemplo de solucion 2
   ```python
   #1.la funcion devera devolver la resta de dos numeros pasados por parametro
   def resta(a,b):
      return a-b

   ```
3. una vez realizada la solucion se debera comprobara que pase el test abrimos nuestra terminal y ejecutamos el siguiente comando
   ```python
   pytest -v
   ```
   esta nos mostrara informacion sobre los ejercicios correctos e incorrectos por consola los correctos se mostraran en verde y los incorrectos en rojo

4. finalmente haremos `push` a nuestro repositorio.

##=======================================================
 def actualizar_negocio(self, id, clave,valor):
        ol=valor
        negocio_actualizar=list(filter(lambda obj:obj[clave]==id,negocios))[0].update({clave:valor}) 
        return 'se actualizo'

    def borrar(self, ruc):
        re=list(filter(lambda el:el['ruc']!=ruc,negocios))
        return re
    def registrar_negocio(self):
        nuevo_id=len(negocios)+1
        negocio_nuevo={
        'id':nuevo_id,
        'ruc':self.ruc,
        'nombre':self.nombre,
        'categoria':self.categoria,
        'horario_atencion':self.horario_atencion,
        'gerente':self.gerente
    }
        registro_negocio=negocios.append(negocio_nuevo)
        return 'producto registrado exitosamente'

    def actualizar_horario(self, id, clave, valor):
        negocios[id-1][clave]=valor
        #actu_hora=list(filter(lambda obj:obj[clave]==dato,negocios))[0].update({clave:valor}) 
        return 'se actualizo el horario'

a=Tiendas(123456789,'panesito','abarrotes,bodega,restaurante',{'dia':'9am-11am','tarde':'5pm-9pm'},'maria')
#print(a.gerente(negocios,'Lourdes'))
#print(a.tienda_ctg('bodega'))
#print(a.ruc_nombre())
#print(a.mostrar_negocio(negocios,'Lulu'))
#print(a.mostrar_tiendas())
#print(a.categorias_tienda(negocios))

# print(a.eliminar_negocio(1))
#print(a.actualizar_negocio('Lulu','nombre','gatuno'))
# print(a.mostrar_negocio(2))
#print(a.borrar(2365897412))

# print(a.registrar_negocio())
# print(a.mostrar_negocio(11))
print(a.actualizar_horario(1,'horario_atencion',{'dia':'7am-12pm','tarde':'3pm-9pm'}))
print(a.mostrar_negocio(2))
# tarea
## otro metodo para crear un nuevo producto
## otro metodo para actu8alizar el horario de atencion
   
