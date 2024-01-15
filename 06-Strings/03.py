cadena = input("Ingrese algo con mas de 5 caracteres ");

largo = len(cadena)

## La variable largo me ubica en el ultimo lugar de la cadena. Como len() no es inclusivo
## debo utilizarlo para irme hasta el ultimo caracter del string
## de la misma forma, debo restar 3 a largo para mostrar lops ultimos tres
## pues, de nuevo, no es inclusivo
ultimos_tres = largo - 3

print(cadena[ultimos_tres:largo])
