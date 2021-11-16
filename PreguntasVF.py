# ## Verdadero o falso con argumentos

# ### 1.  Una función recursiva resuelve un problema resolviendo una parte mas pequeña del mismo problema 

#Verdadero
#Una función recursiva se llama a sí misma varias veces hasta resolver el problema. 
#Y cada vez que esta se llama reduce el problema grande en partes mas pequeñas hasta poder resolver el problema completo.


# ### 2.  Los modelos computacionales nos ayudan a analizar la complejidad de los algoritmos, ya que nos proveen de las especificaciones de la computadora en la cual estos se ejecutarían idealmente

#Verdadero
#Los algoritmos computacionales pueden funcionar mejor o peor en base a varios factores, como pointer machine, etc.


# ### 3.  La búsqueda en un árbol binario de búsqueda es siempre mas rápida que la búsqueda lineal en un arreglo

#Falso
#Depende de la situación, en casos donde tnemos que ordenas un número reducido de elementos, es más rápida la búsqueda
#lineal en un arreglo.


# ### 4. Un algoritmo de complejidad O(nlog(n)) es mas rápido que un algoritmo de complejidad O(n) 


#Falso. 
#La complejidad Ω(n) tiene una tasa de crecimiento menor a la de Ω(n*log(n)), 
#por lo que un algoritmo de complejidad Ω(n) va a ser más rapido que un algoritmo de complejidad  Ω(n*log(n))


#### 5.  Un algoritmo de complejidad Ω(nlog(n)) es mas rápido que un algoritmo de complejidad Ω(n)



#Falso, la complejidad O(n) tiene una tasa de crecimiento menor a la de O(n*log(n)),
#por lo que un algoritmo de complejidad O(n) va a ser más rapido que un algoritmo de complejidad  O(n*log(n))


# ## Problemas de programación
# #### Todo el código debe ser en Python. Si se requiere escribir funciones que hagan búsqueda o ordenamiento (search, sort), programe las funciones usando los conceptos aprendidos en clase. No use las funciones que Python provee para hacer esto. 

# ### 6. Dada una lista enlazada que represente un número. Por ejemplo, 123 es representado por la lista 1->2->3 si la lista es simple o con doble enlace si es doble. Escriba un programa que haga lo siguiente:
# 
# 1. Reciba dos números A y B como input
# 
# 2. Transforme estos números a listas enlazadas como la definida arriba
# 
# 3. Implemente la resta de los números descritos por esas listas enlazadas. El resultado (A-B) debe ser almacenado en una lista enlazada.
# 
# 4. Imprima el resultado concatenando el valor de los nodos de la lista enlazada resultante
# 
# Nota: asuma que el número A es mayor que B
