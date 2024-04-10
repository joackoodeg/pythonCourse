def arithmetic_arranger(problems, show_answers=False):
    # Inicializar las filas para cada problema
    top_row = ""
    bottom_row = ""
    dash_line = ""
    result_row = ""
    
    # Verificar que no haya más de 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        # Separar los operandos y el operador
        num1, operator, num2 = problem.split()
        
        # Verificar si el operador es válido
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Verificar si los operandos son dígitos
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.' 

        # Calcular el ancho necesario para el problema
        width = max(len(num1), len(num2)) + 2
        
        # Construir cada fila del problema
        top_row += num1.rjust(width) + "    "
        bottom_row += operator + num2.rjust(width - 1) + "    "
        dash_line += "-" * width + "    "
        
        # Calcular el resultado y construir la fila correspondiente
        if operator == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))
        result_row += result.rjust(width) + "    "
    
    # Eliminar el espacio adicional al final
    top_row = top_row.rstrip()
    bottom_row = bottom_row.rstrip()
    dash_line = dash_line.rstrip()
    result_row = result_row.rstrip()
    
    # Concatenar todas las filas
    if show_answers:
        arranged_problems = top_row + "\n" + bottom_row + "\n" + dash_line + "\n" + result_row
    else:
        arranged_problems = top_row + "\n" + bottom_row + "\n" + dash_line
    
    return arranged_problems

# Ejemplo de uso
problems = ["3801 - 2", "123 + 49"]
print(arithmetic_arranger(problems))
print("  3801      123\n-    2    +  49\n------    -----")