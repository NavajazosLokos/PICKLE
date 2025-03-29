PICKLE
Esta libreria en python se utiliza para guardar y restaurar archivos en binario es muy
util para conservar datos entre ejecuciones sin tener que volver a generarlo o
procesarlos. tambien sirve para procesar y transmitir datos entre procesos o redes.

Programa sencillo para guardar archivos binarios.

![image](https://github.com/user-attachments/assets/de6ae6b7-265f-44c0-8055-e083ccca4c0b)


se puede ver que que se usa en el codigo guarda los datos en un archivo binario
llamado datos.pkl con wb que se refiere que se creara y se inscriba en binario la
instrucción de pickle.dump hace el proceso para guardarlo en el archivo datos.pkl,
tambien en el mismo programa se abre para leer el archivo, se usa pickle.load para
cargar el archivo binario y decodificarlo
guardando la lista en la variable cargado y mostrandolo, es una función sencilla para
guardar archivos pero otra función que tiene es en este programa.

![image](https://github.com/user-attachments/assets/bb419fb4-b68f-44c7-baa4-0b83a4a96970)

Un ejemplo de la conocida funcion de checkpoint ya que cuando se genera el
programa checa si hay un estado o un archivo existente como no hay empieza su
proceso de sumar 1 al contador y cambiar el estado de inicio a proceso si es menor
que 5 en el contador seguirá en proceso.

Cada que se inicie el programa en vez crear otra lista estado cargará el que se hizo
al inciar el programa por primera vez imrpimiendo el contado en 1 y siguiendo en
proceso, cambiara el estado en proceso a finalizado cuando el contador llegue a 5
como se puede ver en la imagen.

![image](https://github.com/user-attachments/assets/be9427f4-db4b-4786-8978-a85243e11f42)

muy bueno para guardar cada cierto tiempo la ejecución del programa para cuando
haya un contratiempo o una falla que pueda afectar la perdida del proceso del
programa. esto hara que la perdida sea lo mas mínima posible y no total del
programa volviendo al estado del programa que se guardo por ultima vez
