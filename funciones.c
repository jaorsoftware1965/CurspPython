// Funciones.c
// Archivo a generar dll y usa en python
/*
 * comandos de compilación:
 * 
 * gcc -c -FPIC funciones.c
 * gcc -shared funciones.o -o funciones.dll
 * 
 * */

// Variable Global
int tam = 6; 

/* función para obtener promedio de un vector de enteros */
float promedio(int x[])
{
 int i;
 float promedio=0;
 
 for(i=0; i < tam; i++)
 {
  promedio += x[i];
 }
 
 return promedio/tam;
}