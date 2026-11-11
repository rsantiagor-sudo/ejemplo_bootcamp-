#Una empresa necesita calcular la liquidación
#mensual de un empleado. Solicita el valor del salario diario y los días trabajados en el mes. Calcula el
#salario bruto, resta un 4% para pensión y un 4% para salud sobre el bruto, e imprime el neto a pagar.

# TRABAJAMOS CON UN SOLO EMPLEADO, Y CALCULAMOS SU SALARIO PRIMERAMENTE PARA EXTRAER SU LIQUIDACION.

"""CALCULAMOS"""

print();

print("NOMINA BASICA DE UN EMPLEADO");
print("-"*50);
salario_del_empleado = float(input("INGRESE EL VALOR DE SU SALARIO DIARIO: "));
dias_laborados = int(input("INGRESE LOS DIAS TRABAJADOS EN LA EMPRESA: "));
print();

salario_bruto = float(salario_del_empleado * dias_laborados);

pension_del_empleado = salario_bruto * 4/100;
salud_del_empleado = salario_bruto * 4/100;
salario_neto_del_empleado = salario_bruto - pension_del_empleado - salud_del_empleado;
print("-"*60);

print(f"EL VALOR DE SU SALARIO DIARIO ES DE:    ${salario_del_empleado:,.0f}");
print(f"LOS DIAS QUE HA TRABAJADO SON:          {dias_laborados} DIAS");

print(f"SALARIO BRUTO:                          ${salario_bruto:,.0f}");
print(f"PENSION DEL EMPLEADO ES:                ${pension_del_empleado:,.0f}");
print(f"SALUD DEL EMPLEADO ES:                  ${salud_del_empleado:,.0f}");

print();
print(f"LA LIQUIDICION MENSUAL DEL EMPLEADO ES: $ {salario_neto_del_empleado:,.0f}");

print();


