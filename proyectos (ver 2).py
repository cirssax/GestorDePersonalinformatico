# -*- coding: cp1252 -*-
import os
#Funcion para mostrar el reporte por cada rol
def ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar):
    if aciertos == 5: #Caso de cumplir todas las opciones
        print("\t\t CAPACITADO EN SU TOTALIDAD")
    else:
        if Hab == False: #Caso en que no posee las habilidades
            print("\t\t RECHAZADO")
            print("\t\t no posee las habilidades necesarias")
        else:
            if aciertos >= 3:
                if len(NecesidadesMejorar) > 0:
                    print("\t\t REVISAR LAS NECESIDADES")
                    print("\t\t evaluar si se pueden mejorar las necesidades")
                    print(NecesidadesMejorar)

                if len(CompetenciasMejorar) > 0:
                    print("\t\t REVISAR COMPETENCIAS")
                    print("\t\t evaluar si se pueden mejorar las competencias")
                    print(CompetenciasMejorar)
                    print("\n")
            else:
                print("\t\t RECHAZADO")
                print("\t\t tiene muy baja acertividad de campos")



salida = True
while salida==True:
    #MENU PRINCIPAL
    os.system ("cls")
    print("---BIENVENDIO AL GESTOR DE PERSONAL INFORMATICO---\n")
    print("          Porfavor ingrese una opcion")
    print(" __________________________________________________")
    print("|    Ver los parametros para algun rol     |   1   |")
    print("|__________________________________________|_______|")
    print("|    Ingresar parametros para mostrar      |       |")
    print("|    posibles roles a los que pueda        |   2   |")
    print("|    aspirar la persona                    |       |")
    print("|__________________________________________|_______|")
    print("|    Salir                                 |   0   |")
    print("|__________________________________________|_______|")
    print("\n")
    op = int(input("Seleccione una opcion: "))
    if op == 1:
        #VISUALIZAR LO NECESARIO PARA CADA ROL QUE ESTA DEFINIDO
        
        os.system ("cls")
        salida2 = True
        while salida2 == True:
            os.system ("cls")
            print("         Seleccione el rol que desea visualizar         ")
            print(" ________________________________________________________")
            print("|                    ROLES ESTRATEGICOS                  |")
            print("|________________________________________________________|")
            print("|    Gerente General ...............................  1  |")
            print("|    Gerente de Finanzas ...........................  2  |")
            print("|    Gerente de Recursos Humanos ...................  3  |")
            print("|    Gerente de TI .................................  4  |")
            print("|    Gerente de Marketing ..........................  5  |")
            print("|    Secretario General ............................  6  |")
            print("|________________________________________________________|")
            print("|                       ROLES TACTICOS                   |")
            print("|________________________________________________________|")
            print("|    Director de informacion .......................  7  |")
            print("|    Director de operaciones .......................  8  |")
            print("|    Gerente de produccion .........................  9  |")
            print("|    Director tecnico ..............................  10 |")
            print("|    Director comercial ............................  11 |")
            print("|    Director de seguridad .........................  12 |")
            print("|________________________________________________________|")
            print("|                    ROLES OPERACIONALES                 |")
            print("|________________________________________________________|")
            print("|    Secretario(a) del Gerente General .............  13 |")
            print("|    Secretario(a) del Gerente de Finanzas .........  14 |")
            print("|    Recepcionista .................................  15 |")
            print("|    Asistente .....................................  16 |")
            print("|    Vendedor ......................................  17 |")
            print("|    Auxiliar de servicios .........................  18 |")
            print("|________________________________________________________|")
            print("|    VOLVER AL MENU PRINCIPAL                         0  |")
            print("|________________________________________________________|")
            print("\n")
            op2 = int(input("Seleccione el que desea visualizar: "))
            if op2 == 1: #gerente general
                os.system ("cls")
                print("\tROL: GERENTE GENERAL")
                print("\tDESCRIPCION: es la persona encargada de maxima autoridad de la organizacion")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Competitivo          70 - 90")
                print("\t\t Autorealizacion      80 - 100")
                print("\t\t Lograr influir       90 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Analisis             90 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Estrategico          90 - 100")
                print("\t\t Autonomo             80 - 100\n")

                print("\t4 - Historia Biografica")
                print("\t\t Sin carencias\n")

                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social   75 - 100")
                
                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 2: #gerente de finanzas
                os.system ("cls")
                print("\tROL: GERENTE DE FINANZAS")
                print("\tDESCRIPCION: es aquel que esta a cargo de la gestion financiera de la organizacion. Responsable de: planificacion, ejecucion e informacion financiera.")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Competitivo           70 - 90")
                print("\t\t Poder                 80 - 90")
                print("\t\t Lograr influir        80 - 100")
                print("\t\t Supervision           75 - 100\n")
            
                print("\t2 - Competencias")
                print("\t\t Pronosticos           80 - 100\n")
                                    
                print("\t3 - Habilidades")
                print("\t\t Estudioso             65 - 100")
                print("\t\t Analitico             70 - 100\n")
                    
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales  50 - 100\n")
                 
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social    75 - 100")

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 3: #gerente de RRHH
                os.system ("cls")
                print("\tROL: GERENTE DE RECURSOS HUMANOS")
                print("\tDESCRIPCION: es el que gestiona lo relacionado con el equipo humano de una organizacion, asi como tambien las operaciones de sus relaciones")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Competitivo              80 - 100")
                print("\t\t Poder                    75 - 100")
                print("\t\t Social                   80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Comunicarse oralmente    80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Carismatico              80 - 100")
                print("\t\t Comunicador              80 - 100")
                print("\t\t Contextual               70 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencia emocional       50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social       75 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 4: #gerente de TI
                os.system ("cls")
                print("\tROL: GERENTE DE TI")
                print("\tDESCRIPCION: es aquel que se concentra en asuntos tecnologicos y cientificos.")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Competitivo                           80 - 100")
                print("\t\t Poder                                 75 - 100")
                print("\t\t Lograr influir                        80 - 100")
                print("\t\t Responsabilidad                       75 - 100")
                print("\t\t Seguridad                             80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Manejo de tecnologias especificas     80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Desarrollador                         80 - 100")
                print("\t\t Estrategico                           80 - 100")
                print("\t\t Estudioso                             75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales                  50 - 100\n")
               
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social                    75 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 5: #gerente de marketing
                os.system ("cls")
                print("\tROL: GERENTE DE MARKETING")
                print("\tDESCRIPCION: es el maximo a cargo dentro del area comercial, depende de manera directa al gerente genera")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Competitivo              80 - 100")
                print("\t\t Lograr influir           75 - 100")
                print("\t\t Seguridad                80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Analisis                 75 - 100\n")

                print("\t3 - Habilidades")
                print("\t\t Estudiso                 75 - 100")
                print("\t\t Emprendedor              80 - 100")
                print("\t\t Analitico                75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales     50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social       75 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 6: #secretario general
                os.system ("cls")
                print("\tROL: SECRETARIO GENERAL")
                print("\tDESCRIPCION: identifica al cargo que le sigue al Gerente General dentro de una organizacion")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Competitivo              80 - 100")
                print("\t\t Autorrealizacion         75 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Observar                 85 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Equilibrado              80 - 100")
                print("\t\t Carismatico              75 - 100")
                print("\t\t Analitico                75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales     50 - 100\n")
                    
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social       75 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 7: #dir de informacion
                os.system ("cls")
                print("\tROL: DIRECTOR DE INFORMACION")
                print("\tDESCRIPCION: es aquel que posee capacidades administrativas y tecnicas, consiste en emparejar los sistemas de informacion con los planes de la compaï¿½ia, elaborar y administrar los presupuestos y coordinar los equipos tecnicos")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Politicas de la empresa          60 - 100")
                print("\t\t Desafios                         60 - 90\n")
                
                print("\t2 - Competencias")
                print("\t\t Manejo de tenologias espeficas   80 - 100")
                print("\t\t Analisis                         60 - 90\n")
                
                print("\t3 - Habilidades")
                print("\t\t Estudioso                        60 - 100")
                print("\t\t Analitico                        60 - 100")
                print("\t\t Desarrollador                    75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias emocionales            50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social               50 - 90")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 8: #dir de operaciones
                os.system ("cls")
                print("\tROL: DIRECTOR DE OPERACIONES")
                print("\tDESCRIPCION: responsable del control de actividades diarias de la corporacion y el manejo de operaciones. Reporta directamente al gerente general")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                 60 - 90")
                print("\t\t Desafios                   60 - 90\n")
                
                print("\t2 - Competencias")
                print("\t\t Obediencia                 75 - 100")
                print("\t\t Observar                   80 - 100")
                print("\t\t Escuchar                   80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Estrategico                60 - 100")
                print("\t\t Analitico                  50 - 90\n")
                    
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales       50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social         50 - 90")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 9: #gerente de produccion
                os.system ("cls")
                print("\tROL: GERENTE DE PRODUCCION")
                print("\tDESCRIPCION: es aquel que investiga, selecciona e impulsa el desarrollo de los productos en la organizacion")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Progreso                   60 - 90")
                print("\t\t Condiciones de trabajo     50 - 90\n")
                
                print("\t2 - Competencias")
                print("\t\t Observar                   75 - 100")
                print("\t\t Escuchar                   75 - 100")
                print("\t\t Analisis                   60 - 90\n")
                
                print("\t3 - Habilidades")
                print("\t\t Analitico                  60 - 90\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales       50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social         50 - 90")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 10: #dir tecnico
                os.system ("cls")
                print("\tROL: DIRECTOR TECNICO")
                print("\tDESCRIPCION: en general es una persona tecnica superior en una organizacion, tiene el mas alto nivel dentro de un campo tecnico especifico")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Supervision                            75 - 100")
                print("\t\t Desarrollo                             80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Manejo de tecnologias especificas      80 - 100")
                print("\t\t Analisis                               75 - 90")
                
                print("\t3 - Habilidades")
                print("\t\t Analitico                              75 - 90\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias emocionales                  50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social                     50 - 90")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 11: #dir de comercial
                os.system ("cls")
                print("\tROL: DIRECTOR COMERCIAL")
                print("\tDESCRIPCION: es aquel que se encarga de evaluar los elementos tecnicos propuestos por el gerente de marketing")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Progreso                     75 - 100")
                print("\t\t Responsabilidad              75 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Observar                     80 - 100")
                print("\t\t Escuchar                     80 - 100")
                print("\t\t Comunicarse oralmente        80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Analitico                    60 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales         50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Estabilidad social           50 - 90")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 12: #dir de seguridad
                os.system ("cls")
                print("\tROL: DIRECTOR DE SEGURIDAD")
                print("\tDESCRIPCION: es el responsable del area de seguridad del area de la empresa, tanto en lo publico como en lo privado")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Seguridad                       80 - 100")
                print("\t\t Responsabilidad                 80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Motricidad                      75 - 95")
                print("\t\t Seguir prescripciones para")
                print("\t\t hacer una rutina de trabajo     80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Analitico                       80 - 100")
                print("\t\t Empatico                        75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencia material               50 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria              50 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 13: #secretario(a) del gerente general
                os.system ("cls")
                print("\tROL: SECREATIOR(A) DEL GERENTE GENERAL")
                print("\tDESCRIPCION: es la persona que ejercera como asistente del Gerente General, solo especifico para este rol dentro de la organizacion")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                             60 - 90")
                print("\t\t Responsabilidad                        85 - 100")
                print("\t\t Sueldo                                 75 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Lectura                                85 - 100")
                print("\t\t Compresion de textos                   85 - 100")
                print("\t\t Obediencia                             80 - 100")
                print("\t\t Compromiso                             80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Disciplinado                           75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales y/o emocionales   75 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria                     50 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 14: #secretario(a) del gerente de finanzas
                os.system ("cls")
                print("\tROL: SECRETARIO(A) DEL GERENTE DE FINANZAS")
                print("\tDESCRIPCION: es la persona que ejercera como asistente del Gerente de Finanzas, solo especifico para este rol dentro de la organizacion")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                             60 - 90")
                print("\t\t Responsabilidad                        85 - 100")
                print("\t\t Sueldo                                 75 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Lectura                                85 - 100")
                print("\t\t Compresion de textos                   85 - 100")
                print("\t\t Obediencia                             80 - 100")
                print("\t\t Compromiso                             80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Disciplinado                           75 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales y/o emocionales   75 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria                     50 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 15: #recepcionista
                os.system ("cls")
                print("\tOL: RECEPCIONISTA")
                print("\tDESCRIPCION: es el profesional que atiende a los clientes")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                             60 - 90")
                print("\t\t Sociales                               75 - 100")
                print("\t\t Afiliacion                             80 - 100")
                print("\t\t Sueldo                                 80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Comunicarse oralmente                  85 - 100")
                print("\t\t Observar                               85 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Disciplinado                           80 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales y/o emocionales   75 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria                     50 - 100")
                print("\t\t Estabilidad social                     60 - 100")
                

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                    
            elif op2 == 16: #asistente
                os.system ("cls")
                print("\tROL: ASISTENTE")
                print("\tDESCRIPCION: es aquel que realiza las tareas diarias personales dentro de una organizacion")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                             60 - 90")
                print("\t\t Afiliacion                             85 - 100")
                print("\t\t Sueldo                                 80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Seguir prescripciones para")
                print("\t\t hacer una rutina de trabajo            80 - 100")
                print("\t\t Obediencia                             80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Disciplinado                           80 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales y/o emocionales   75 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria                     50 - 100")
                print("\t\t Estabilidad social                     60 - 100")

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 17: #vendedor
                os.system ("cls")
                print("\tROL: VENDEDOR")
                print("\tDESCRIPCION: es aquel que se encarga de comercializar los productos o servicios")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                             60 - 90")
                print("\t\t Afiliacion                             60 - 90")
                print("\t\t Sueldo                                 60 - 90\n")
                
                print("\t2 - Competencias")
                print("\t\t Comunicarse oralmente                  85 - 100")
                print("\t\t Observar                               85 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Disciplinado                           80 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales y/o emocionales   75 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria                     50 - 100")

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 18: #auxiliar de servicios
                os.system ("cls")
                print("\tROL: AUXILIAR DE SERVICIOS")
                print("\tDESCRIPCION: es aquel que proporciona el apoyo en un determinado")
                print("\n")
                print("\tParametros: ")
                print("\t1 - Necesidades")
                print("\t\t Destacarse                             60 - 90")
                print("\t\t Sueldo                                 80 - 100")
                print("\t\t Autorrealizacion                       80 - 100")
                print("\t\t Afan por tener relaciones")
                print("\t\t amigables y estrchas                   80 - 100\n")
                
                print("\t2 - Competencias")
                print("\t\t Obediencia                             80 - 100\n")
                
                print("\t3 - Habilidades")
                print("\t\t Disciplinado                           80 - 100\n")
                
                print("\t4 - Historia Biografica")
                print("\t\t Carencias materiales y/o emocionales   75 - 100\n")
                
                print("\t5 - Factores Ambientales")
                print("\t\t Sociedad solidaria                     50 - 100")

                print("\n")
                print("0: volver al menu principal    1: visualizar otro rol")
                op3 = int(input("A donde desea ir: "))
                if op3 == 0:
                    salida2 = False
                
            elif op2 == 0: #salir al menu principal
                os.system ("cls")
                salida2 = False
                
            else: #opcion erronea
                os.system ("cls")
                print("Ingrese una opcion valida")
                print("\n")
                raw_input("pulse enter para voler")

    elif op == 2:
        os.system ("cls")   

        #Necesidades
        Competitivo = int(input("Si usteden su area encuentra a alguien"
                             "\nque es mejor, se esfuerza por superarlo?\n" 
                             "\n\ta) Siempre" #100
                             "\n\tb) Tal vez, dependera de cuan buena es la otra persona" #55
                             "\n\tc) No" #10
                             "\n\td) Solo si este implica un aumento de sueldo" #70
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Autorrealizacion = int(input("\n\nComo ha reaccionado usted ante el logro"
                             "\no fracaso en alguna meta propuesta?\n"
                             "\n\ta) Si la logro, es bueno y genial;" #50
                             "\n\t   pero si no simplemente dejo de lado eso"
                             "\n\tb) Si la logro me da lo mismo y si no tambien me da lo mismo" #20
                             "\n\tc) Si la logro genial, sino la logro intento de otra manera" #80
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        LograrInfluir = int(input("Si usted tiene una idea para un trabajo. Como se la hace"
                             "\nllegar a su superior?\n"
                             "\n\ta) Prefiero no comentarle ya que puede ser una idea erronea" #10
                             "\n\tb) Se la comento" #50
                             "\n\tc) Se la comento y ademas le doy las justificaciones de por"
                             "\n\t   que puede ser una buena idea" #80
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Poder = int(input("Usted prefiere estar a cargo de un proyecto o trabajar en este?\n"
                             "\n\ta) Si, prefiero estar a cargo pero despues de adquirir experiencia" #85
                             "\n\tb) No, ya que no estoy capacidado para eso" #40
                             "\n\tc) Si prefiero inmediatamente estar a cargo de un proyecto." 
                             "\n\t   pero no tengo experiencia en esa labor" #60
                             "\n\td) Si prefiero inmediatamente estar a cargo de un proyecto." 
                             "\n\t   t Tiene experiencia en esa labor? SI NO" #90
                             "\n\te) No es mi preferencia, pero no me molestaria estar a cargo de un proyecto" #60
                             "\n\n\nRespuesta: "))
        os.system ("cls") 
        
        Supervision = int(input("En un proyecto x. Como controla que se esten llevando a cabo las fases del proyecto?"
                             "\n\ta) No las controlo, simplemente quiero que salgan" # 30
                             "\n\tb) Prefiero planificar bien e intentar cumplir"
                             "\n\t   dicha planificacion" #70
                             "\n\tc) Evaluo la parte superficial del proyecto" #30
                             "\n\td) No planifico, pero igual superviso el proyecto" #60
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Social = int(input("Prefiere trabajar en grupo o solo?"
                             "\n\ta) Grupo" #80
                             "\n\tb) Solo" #25
                             "\n\tc) En gupos pequenos" #60 
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Responsabilidad = int(input("Si usted observa que se atrasara en la fase de un proyecto" 
                            "\nQue hace?\n"
                             "\n\ta) Apuro las actividades para que pueda salir en el tiempo" ##30
                             "\n\tb) Informo del retraso en la entrega a mi superior" #75
                             "\n\tc) Omito y anazno en lo que siguiente mientras dejo" #30
                             "\n\t   en paralelo lo que falta de lo que esta pendiente"
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Seguridad = int(input("En un proyecto x si hay un area que observa que no posee un" 
                             "\nconocimiento adecuado. Que hace?"
                             "\n\ta) Consulto con una persona que sea competente en el area" #65
                             "\n\tb) Trato de solucionarlo, yo primero, si no puedo busco una" #80
                             "\n\t   persona competente "
                             "\n\tc) Lo soluciono yo lo antes posible" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        PoliticasEmpresa = int(input("Pregunta: En un proyecto se define una metodologia de acuerdo"
                             "\na la empresa, uste siente que puede hacerlo mejor que lo definido. Que hace?"
                             "\n\ta) Trabajo con mi metodologia de trabajo" #30
                             "\n\tb) Trabajo con la definida por la emmpresa" #75
                             "\n\tc) Hago una mezcla de ambas metodologias" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Desafios = int(input("Prefiere ingresar a un proyecto que esta iniciado o" 
                             "\npartir trabajando en uno que parte desde cero?"
                             "\n\ta) Iniciado" #40
                             "\n\tb) Desde cero" #80
                             "\n\tc) Recientemente iniciado" #50
                             "\n\td) Me es indeferente, soy capaz en ambas areas" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Destacarse = int(input("Lucharia por ser el primero en tener una solucion?"
                             "\n\ta)  Si" #85
                             "\n\tb)  No" #30
                             "\n\tc)  Prefiero verificar primero si es correcta la solucion"
                             "\n\t    que tenga" #50
                             "\n\td)  Mientras alguien encuentre la solucion primero, por mi, bien" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Progreso = int(input("Pregunta: Cuando observa que el proyecto que tiene a cargo avanza de acuerdo"
                             "\na lo planificado. Usted sigue trabajando a ese ritmo tranquilamente e informa"
                             "\na su jefe del cumplimiento parcial del proyecto o no?"
                             "\n\ta)Informo a mi superior del cumplimiento parcial del trabajo" #30
                             "\n\tb)Informo cuando haya terminado toda la fase que se este realizando" #80
                             "\n\tc)Informo solo si me lo piden" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        CondicionesTrabajo = int(input("Prefiere tener mejor equipamiento o mejor" 
                             "\narea de trabajo?"
                             "\n\ta) Me gustaria las dos por igual" #75
                             "\n\tb) Prefiero el equipamento" #40
                             "\n\tc) Prefiero mejor area de trabajo" #70 
                             "\n\nRespuesta: "))
        os.system ("cls")
        
        Desarrollo = int(input("Pregunta: Cuando esta trabajando en un proyecto x y lo termina, antes de presentarlo"
                             "\nlo revisa parcialmente o completamente o simplemente no lo revisa?"
                             "\n\ta) Lo reviso por completo" #80
                             "\n\tb) No lo reviso ya que sé que esta correcto" #50
                             "\n\tc) Reviso solo lo relevante" #40
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Sueldo = int(input("Alguna pretencion de sueldo?"
                             "\n\ta) Si, \"x\" monto (mayor que el del mercado)" #85
                             "\n\tb) No, me guio por el valor del mercado" #60
                             "\n\tc) Si, donde \"x\" es mucho menor sueldo base del mercado" #30
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Sociales = int(input("Pregunta: Prefiere trabajar en grupo o solo?" #no se si eta existe en el otro lado, pero creo que no
                             "\n\ta) Si" #75
                             "\n\tb) No" #40
                             "\n\tc) Me da Igual" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Afiliacion = int(input("Pregunta: Si en algun momento usted realiza un proyecto muy bueno"
                             "\nle gustaria un reconocimiento por parte de la empresa?"
                             "\n\ta) Si, seria lo ideal" #75
                             "\n\tb) Me da exactamente igual" #30
                             "\n\tc) Prefiero que no" #10
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        RelacionesAmigables = int(input("Prefiere tener armonia en su grupo de trabajo o le da igual?\n"
                             "\n\ta) Prefiero tener armonia" #80
                             "\n\tb) Me da igual mientras salga el proyecto adelante" #50
                             "\n\tc) No"#20           
                             "\n\nRespuesta: "))
        os.system ("cls") 

        #Competencias
        Analisis = int(input("Como abordaria usted un problema?\n"
                             "\n\ta) Lo abordaria de todos los casos posibles" #85
                             "\n\tb) Observaria lo que realizo la persona anterior a mi" #60
                             "\n\tc) Se lo delegaria a otra persona" #30
                             "\n\td) Haria un esquema con una posible solucion y lo" 
                             "\n\t   desarollaria lo mas rapido posible" #45
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Pronosticos = int(input("Cuando termina un proyecto se desliga completamente de este?\n"
                             "\n\ta) Si, ya que esta terminado" #30
                             "\n\tb) No, puesto que puede surgir nuevas mejoras en el proceso" #75
                             "\n\tc) No, pero prefiero que si hay nuevos cambios, se" 
                             "\n\t   responsabilice otra persona." #50
                             "\n\nRespuesta: "))
        os.system ("cls") 

        ComuniacionOral = int(input("Cuando tiene que dar alguna instruccion a su equipo de trabajo" 
                            "\nPrefiere hacerselas llegar por escrito (memo o correo electronico)"
                            "o en una reunion?\n"
                             "\n\ta) Por escrito" #30
                             "\n\tb) En una Reunion" #75
                             "\n\tc) De ambas formas" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 

        ManejoTecnologias = int(input("Conoce sobre las nuevas tecnologias que estan surgiendo en su area?\n"
                             "\n\ta) Si; pero no he tenido tiempo de aprenderlas en detalle"  #70
                             "\n\tb) No" #30
                             "\n\tc) Si y las se manejar" #85
                             "\n\nRespuesta: "))
        os.system ("cls")

        Observar = int(input("Cuando revisa un proyecto. Que aspectos evalua?\n"
                             "\n\ta) Trato de evaluar todo el funcionamiento del sistema, en lo posible todo" #80
                             "\n\tb) Evaluo lo mas relevante, o lo que podria ser mas probable de error" #60
                             "\n\tc) Evaluo lo que mas probablemente tenga fallos" #60 
                             "\n\td) No reviso, ya que en cada fase se hicieron las pruebas correspondientes" #30
                             "\n\nRespuesta: "))
        os.system ("cls") 

        Obediencia = int(input("Cuando se le asigna una fase de un proyecto. Como la cumple?\n"
                             "\n\ta) La cumplo a cabalidad de acuerdo a lo estipulado" #75
                             "\n\tb) La cumplo de acuerdo a lo estipulado y trato de ver un valor aniadido" #80
                             "\n\tc) Prefiero preguntar a mi jefe directamente" #50
                             "\n\td) Le pregunto a otras personas" #30
                             "\n\nRespuesta: "))
        os.system ("cls") 

        Escuchar = int(input("Cuando se la da una instruccion y no la entiende de manera clara,"
                             "\nprefiere preguntar a su jefe o preguntar a otras personas?\n"
                             "\n\ta) Prefiero preguntar a mi jefe directamente" #70
                             "\n\tb) Le pregunto a otras personas" #50
                             "\n\tc) Le pregunto a otras personas y ademas despues confirmo con mi jefe" #85
                             "\n\td)"
                             "\n\nRespuesta: "))
        os.system ("cls") 

        Motricidad = int(input("Para un determinado proyecto se requieren muchos detalles, que son muy minimos"
                             "\ny que el mas minimo error implica que usted sea sansionado, desearia tomar dicho"
                             "\nproyecto?"
                             "\n\ta) Si" #60
                             "\n\tb) Prefiero que no" #30
                             "\n\tc) Tendria que evaluar de que trata el proyecto" #75
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        SeguirPrescripciones = int(input("Pregunta: Supongase usted que la empresa tiene una metodologia de trabajo"
                             "\nx y usted piensa de forma diferente. Que hace?"
                             "\n\ta) Propongo un cambio a mi superior" #50
                             "\n\tb) Trabajo con mi metodologia" #30
                             "\n\tc) Hago una mezcla de ambas metodologias" #60
                             "\n\td) Nada" #80
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Lectura = int(input("Â¿Al momento de facilitarle las intrucciones de la fase del"
                            "\nproyecto que esta a cargo, las lee solo o con su grupo de trabajo?\n"
                             "\n\ta) Solo" #50
                             "\n\tb) Con mi grupo de trabajo" #60
                             "\n\tc) Solo y despues con mi grupo de trabajo" #80
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        CompresionTxt = int(input("Si a usted le lleva una descripcion de lo que tiene que hacer," 
                            "\nlee el titulo y con eso sabe mas o menos de que trata." 
                            "\nSigue leyendo?"
                             "\n\ta) Si " #85
                             "\n\tb) No " #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Compromiso = int(input("Como cumple usted la fase del proyecto que se le asigna?"
                             "\n\ta) La cumplo por completo" #75
                             "\n\tb) La cumplo y trato de evaluar de aniadir alun valor extra" #85
                             "\n\nRespuesta: "))
        os.system ("cls") 
        

        #Habilidades
        Estrategico = int(input("Planifica y despues ejecuta?"
                             "\n\ta) Si" #60
                             "\n\tb) No" #20
                             "\n\tc) Hago un diagrama menor de lo que hay que hacer y luego implemento" #30
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Autonomo = int(input("Prefiere trabajar en grupo o en equipo?"
                             "\n\ta) Grupo" #40 
                             "\n\tb) Solo " #75
                             "\n\tc) Me es indeferente" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Estudioso = int(input("Cuando sale una nueva tecnologia en su area. Que hace?"
                             "\n\ta) La investigo" #60
                             "\n\tb) No me preocupo" #20
                             "\n\tc) La investigo y aprendo" #88
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Analitico = int(input("Cuando se enfrenta a dos problemas. Que hace?"
                             "\n\ta) Evaluo cual posee solucion mas rapida para"
                             "\n\t   dar solucion a ese primero." #85
                             "\n\tb) Se los delego a otra persona." #40
                             "\n\tc) Veo cual de las dos tiene fecha limite mas cercana," 
                             "\n\t   hago la que esta mas cerca de su fecha limite" #60
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Carismatico = int(input("Le gusta salir de manera ocasional a reuniones" 
                             "\ncon amigos o amigas, ya sea de trabajo o no lo sean?"
                             "\n\ta) Si" #80
                             "\n\tb) Si, pero con amigos mios no de trabajo." #75
                             "\n\tc) No" #30
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Comunicador = int(input("Cuando se le asigna una fase de un proyecto. Que hace" 
                             "\ncon su grupo de trabajo?"
                             "\n\ta) Me junto y explico paso a paso la fase a realizar"  #85
                             "\n\tb) Les dejo a c/u en su escritorio lo que le corresponde hacer" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Contextual = int(input("Si en algun momento usted olvida algun elemento (cualqueiera sea)." 
                             "\nComo realiza usted para volver a recordar dicho elemento?"
                             "\n\ta) Consulto con la persona que me haya dado la instruccion" #75
                             "\n\tb) Trato de recordarlo a toda costa, si no trato de"  
                             "\n\t   deducirlo en base a lo que tengo" #55
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Desarrollador = int(input("En un proyecto x. Usted prefiere ayudar a gestionar el proyecto" 
                             "\ndesde \"afuera\" o desde \"dentro\"?"
                             "\n\ta) Prefiero gestionar al personal que estara trabajando el proyecto" #30
                             "\n\tb) Prefiero estar incerto lo mas posible en el proyecto" #75
                             "\n\tc) Me gusta estar trabajando desde andentro en el proyecto; pero" 
                             "\n\t   igual me gusta estar en la parte administrativa" #80
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Emprendedor = int(input("Pregunta: Si a usted se le da la oportunidad de ascender. Que hace?"
                             "\n\ta) Acepto inmediatamente" #50
                             "\n\tb) Veo si tengo las competencias necesarias" #80
                             "\n\tc) Prefiero esperar un tiempo antes de aceptar" #50
                             "\n\td) Acetpo, pero primero deseo estar un tiempo de prueba" #68
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Equilibrado = int(input("Pregunta: Supongase que hay una discusion fuerte al interior de su grupo"
                                "\nde trabajo lo cual fragmenta un poco la relacion entre sus companieros."
                                "\nQue hace usted frente a esa situacion?"
                             "\n\ta) Nada, mientras hagan sus fases necesarias para el proyecto" #30
                             "\n\tb) Si empiezan a bajar el rendimiento, reviso que pasa" #60
                             "\n\tc) Trato de reunirme con ambas partes para buscar una solucion" #88
                             "\n\td) Converso con mi superior para buscar una solucion acorde" #70
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Empatico = int(input("Si un companero de trabajo falta. Que hace usted?"
                             "\n\ta) Si es de mi area trato de comunicarme con el" #75
                             "\n\tb) Independiente de quien sea me comunico con el" #88
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        Disciplinado = int(input("En un proyecto x usted se encuentra a cargo de una" 
                             "\narea. Como la organiza y vela para que se cumplan las cosas?"
                             "\n\ta) Organizo mediante una determinada planificacion y estara" 
                             "\n\t   constantemente supervisando que se cumplan los hitos" 
                             "\n\t   de dicha planificacion" #85
                             "\n\tb) Prefiero ir haciendo el camino a medida que se avanza, algo "
                             "\n\t   similar a lo que sucede con las metodologias agiles" #60
                             "\n\tc) Hago un cronograma e informo a los integrantes de mi equipo" #50
                             "\n\nRespuesta: "))
        os.system ("cls") 
        

        #Historia Biografica
        
        CarEmocional = int(input("Cuando era pequeno. Vivia con ambos padres?"
                             "\n\ta) Si" #40
                             "\n\tb) No" #88
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        CarMaterial = int (input("Cuando era pequeno. Vivia con ambos padres?"
                             "\n\ta) Era arrendada" #88
                             "\n\tb) Viviamos en casa propia" #40
                             "\n\nRespuesta: "))
        os.system ("cls") 

        if CarEmocional < 50 and CarMaterial < 50:
            SinCarencias = 75
        else:
            SinCarencias = 30

        #Ambientales
        SocSolidaria = int(input("Usted en el transcurso de sus estudios" 
                             "\nComo describiria el entorno social que lo envolvia en general?"
                             "\n\ta) En general como un grupo ostil, que era demasiado cometitivo y nada amigable" #20
                             "\n\tb) Lograba congeniar con los que era similes a mi; pero con los que no resultaba simplemente no intentaba" #60
                             "\n\tc) En general fue muy flexible y solidaria" #75
                             "\n\nRespuesta: "))
        os.system ("cls") 
        
        EstabSoc = int(input("En cuantos domicilios ha vivido usted?"
                             "\n\ta) Mas de 5 " #40
                             "\n\tb) Menos de 5" #70
                             "\n\tc) Aun vive con sus padres" #75
                             "\n\nRespuesta: "))
        os.system ("cls") 

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True
        Comp = True
        Nece = True

        cantidad = 0

        #Analisis del rol del GERENTE GENERAL
        #Necesidades
        if Competitivo >= 90 and Autorrealizacion >= 80 and Autorrealizacion and LograrInfluir >= 90:
            aciertos = aciertos + 1
        else:
            #Analisis de falta de pts para necesidades
            if Competitivo >= 50 and Competitivo <90:
                aux = 90 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de cometitividad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de competitividad esta muy por debajo\n"

            if Autorrealizacion >= 50 and Autorrealizacion < 80:
                aux = 80 - Autorrealizacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de autorrealziacion\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de autorrealizacion esta muy por debajo\n"

            if LograrInfluir >= 50 and LograrInfluir <90:
                aux = 90 - LograrInfluir
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de influenciar\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de lograr influir esta muy por debajo\n"

        #Competencias
        if Analisis >= 90:
            aciertos = aciertos + 1   
        else:
            #Analisis de falta de pts para competencias
            if Analisis >= 50 and Analisis < 90:
                aux = 90 - Analisis
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts para la capacidad de analisis\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de analisis esta muy por debajo\n"

        #Habilidades
        if Estrategico >= 90 and Autonomo >= 80:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if SinCarencias >= 50:
            aciertos = aciertos + 1

        #Factores ambientales
        if EstabSoc >= 75:
            aciertos = aciertos + 1
            
        #REPORTE del rol del GERENTE GENERAL
        print("\t\tROL: GERENTE GENERAL")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")
        

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DEL GERENTE DE FINANAZAS
        #Necesidades
        if (Competitivo >= 70 and Competitivo <= 90) and Poder >= 80 and LograrInfluir >= 80 and Supervision >= 75:
            aciertos = aciertos + 1 
        else: #en el caso que estan fuera de los intervalos
            if Competitivo >= 50 and Competitivo <70:
                aux = 70 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de competitividad\n"
            elif Competitivo > 90:
                aux = 100 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de competitividad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de competitividad esta muy por debajo\n"
                
            if Poder >= 50 and Poder <80:
                aux = 80 - Poder
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de poder\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de poder esta muy por debajo\n"

            if LograrInfluir >= 50 and LograrInfluir <80:
                aux = 80 - LograrInfluir
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de lograr influir\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de lograr influir esta muy por debajo\n"

            if Supervision >= 50 and Supervision <75:
                aux = 75 - Supervision
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de supervision\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de supervision esta muy por debajo\n"

        #Competencias
        if Pronosticos >= 80:
            aciertos = aciertos + 1
        else: #Caso en que no esta en los intervalos
            if Pronosticos >= 50:
                aux = 80 - Pronosticos
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de pronostico\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de pronosticos esta muy por debajo\n"

        #Habilidades
        if Estudioso >= 65 and Analitico >= 70:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False
        #Historia Biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1
        #Factor medio ambiental
        if EstabSoc >= 75:
            aciertos = aciertos + 1

        #REPORTE
        print("\t\tROL: GERENTE DE FINANZAS")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE GERENTE DE RRHH
        #Necesidades
        if Competitivo >= 80 and Poder >= 75 and Social >= 80:
            aciertos = aciertos + 1
        else:
            if Competitivo >= 50 and Competitivo < 80:
                aux = 80 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de competitividad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de competitividad esta muy por debajo\n"

            if Poder >= 50 and Poder <75:
                aux = 75 - Poder
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de poder\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de poder esta muy por debajo\n"

            if Social >= 50 and Social < 80:
                aux = 80 - Social
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de social\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de socializar esta muy por debajo\n"

        #Competencias
        if ComuniacionOral >= 80:
            aciertos = aciertos + 1
        else:
            if ComuniacionOral >= 50:
                aux = 80 - ComuniacionOral
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de comunicacion oral\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de comuniacion oral esta muy por debajo\n"

        #Habilidades
        if Carismatico >= 80 and Comunicador >= 80 and Contextual >= 70:
            Hab = True
            aciertos = aciertos + 1
        else:
            Hab = False     

        #Historia biografica
        if CarEmocional >= 50:
            aciertos = aciertos + 1

        #Factor medio ambiental
        if EstabSoc >= 75:
            aciertos = aciertos + 1

        #REPORTE
        print("\t\tROL: GERENTE DE RECURSOS HUMANOS")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE GERENTE DE TI
        #Necesidades
        if Competitivo >= 80 and Poder >= 75 and LograrInfluir >= 80 and Responsabilidad >= 75 and Seguridad >= 80:
            aciertos = aciertos +1
        else:
            if Competitivo >= 50 and Competitivo < 80:
                aux = 80 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de competitividad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de competitividad esta muy por debajo\n"

            if Poder >= 50 and Poder < 75:
                aux = 75 - Poder
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de poder\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de poder esta muy por debajo\n"

            if LograrInfluir >= 50 and LograrInfluir < 80:
                aux = 80 - LograrInfluir
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de lograr influir\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de lograr influir esta muy por debajo\n"

            if Responsabilidad >= 50 and Responsabilidad < 75:
                aux = 75 - Responsabilidad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de responsabilidad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de responsabilidad esta muy por debajo\n"

            if Seguridad >= 50 and Seguridad < 80:
                aux = 80 - Seguridad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de seguridad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de seguridad esta muy por debajo\n"

        #Competencias
        if ManejoTecnologias >= 80:
            aciertos = aciertos + 1
        else:
            if ManejoTecnologias >= 50:
                aux = 80 - ManejoTecnologias
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia en menejo de tecologias especificas\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de manejo de tecnologias especificas esta muy por debajo\n"

        #Habilidades
        if Desarrollador >= 80 and Estrategico >= 80 and Estudioso >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1

        #Factores ambientales
        if EstabSoc >= 75:
            aciertos = aciertos + 1

        #REPORTE
        print("\t\tROL: GERENTE DE TI")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE GERENTE DE MARKETING
        #Necesidades
        if Competitivo >= 80 and LograrInfluir >= 75 and Seguridad >= 80:
            aciertos = aciertos + 1
        else:
            if Competitivo >= 50 and Competitivo < 80:
                aux = 80 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de competitividad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de competitividad esta muy por debajo\n"

            if LograrInfluir >= 50 and LograrInfluir < 75:
                aux = 75 - LograrInfluir
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de lograr influir\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de lograr influir esta muy por debajo\n"

            if Seguridad >= 50 and Seguridad < 80:
                aux = 80 - Seguridad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de seguridad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de seguridad esta muy por debajo\n"

        #Competencias
        if Analisis >= 75:
            aciertos = aciertos + 1
        else:
            if Analisis >= 50:
                aux = 50 - Analisis
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de analisis\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de analisis esta muy por debajo\n"

        #Habilidades
        if Estudioso >= 75 and Emprendedor >= 80 and Analitico >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia Biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1

        #Factores ambientas
        if EstabSoc >= 75:
            aciertos = aciertos + 1

        #REPORTE
        print("\t\tROL: GERENTE DE MARKETING")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True
        

        #ANALISI DEL ROL DE SECRETARIO(A) GENERAL
        #Necesidades
        if Competitivo >= 80 and Autorrealizacion >= 75:
            aciertos = aciertos + 1
        else:
            if Competitivo >= 50 and Competitivo < 80:
                aux = 80 - Competitivo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de competitividad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de competitividad esta muy por debajo\n"

            if Autorrealizacion >= 50 and Autorrealizacion < 75:
                aux = 75 - Autorrealziacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de autorrealizacion\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de autorrealizacion esta muy por debajo\n"

        #Competencias
        if Observar >= 85:
            aciertos = aciertos + 1
        else:
            if Observar >= 50:
                aux = 85 - Observar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de observacion\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de obervar esta muy por debajo\n"

        #Habilidades
        if Equilibrado >= 80 and Carismatico >= 75 and Analitico >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False
            
        #Historia biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1
        #Factor ambiental
        if EstabSoc >= 75:
            aciertos = aciertos + 1

        #REPORTE
        print("\t\tROL: SECRETARIO(A) GENERAL")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar=""
        CompetenciasMejorar=""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE DIR DE INFORMACION
        #Necesidades
        if PoliticasEmpresa >= 60 and (Desafios >= 60 and Desafios <= 90):
            aciertos = aciertos + 1
        else:
            if PoliticasEmpresa >= 40 and PoliticasEmpresa <= 60:
                aux = 60 - PoliticasEmpresa
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de politicas de la empresa\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de politicas de la empresa esta muy por debajo\n"

            if Desafios >= 40 and Desafios <= 60:
                aux = 60 - Desafios
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de desafios\n"
            elif Desafios >60:
                aux = 100 - Desafios
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de desafios\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de desafios esta muy por debajo\n"
                
        #Competencias
        if Pronosticos >= 80:
            aciertos = aciertos + 1
        else:
            if Pronosticos >= 50:
                aux = 80 - Pronosticos
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de pronosticos\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de pronosticos esta muy por debajo\n"

        #Habilidades
        if Estudioso >= 65 and Analitico >= 70:
           aciertos = aciertos + 1
           Hab = True
        else:
           Hab = False

        #Historia Biografica
        if CarMaterial >= 50:
           aciertos = aciertos + 1

        #Factores ambientales
        if EstabSoc >= 75:
           aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: DIRECTOR DE INFORMACION")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE DIR DE OPERACIONES
        #Necesidades
        if (Destacarse >= 60 and Destacarse <= 90) and (Desafios >= 60 and Desafios <= 90):
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse < 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destacarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Desafios >= 40 and Desafios < 60:
                aux = 60 - Desafios
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de desafios\n"
            elif Desafios > 90:
                aux = 100 - Desafios
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de desafios\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de desafios esta muy por debajo\n"

        #Competencias
        if Obediencia >= 75 and Observar >= 80 and Escuchar >= 80:
            aciertos = aciertos + 1
        else:
            if Obediencia >= 50 and Obediencia < 75:
                aux = 75 - Obediencia
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de obedienci\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de obediencia esta muy por debajo\n"

            if Observar >= 50 and Observar < 80:
                aux = 80 - Observar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de observacion\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de observar esta muy por debajo\n"

            if Escuchar >= 50 and Escuchar < 80:
                aux = 80 - Escuchar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de escucha\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de escucha esta muy por debajo\n"

        #Habilidades
        if Estrategico >= 60 and (Analitico >= 50):
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia Biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1

        #Factores Ambientales
        if EstabSoc >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: DIRECTOR DE OPERACIONES")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE GERENTE DE PRODUCCION
        #Necesidades
        if (Progreso >= 60 and Progreso <= 90) and (CondicionesTrabajo >= 50 and CondicionesTrabajo <= 90):
            aciertos = aciertos + 1
        else:
            if Progreso >= 40 and Progreso < 60:
                aux = 60 - Progreso
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de progreso\n"
            elif Progreso > 90:
                aux = 100 - Progreso
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de progreso\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de progreso esta muy por debajo\n"

            if CondicionesTrabajo >= 35 and CondicionesTrabajo < 50:
                aux = 50 - CondicionesTrabajo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de condiciones de trabajo\n"
            elif CondicionesTrabajo > 90:
                aux = 100 - CondicionesTrabajo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de condiciones de trabajo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de condiciones de trabajo esta muy por debajo\n"

        #Competencias
        if Observar >= 75 and Escuchar >= 75 and (Analisis >= 60 and Analisis <= 90):
            aciertos = aciertos + 1
        else:
            if Observar >= 50 and Observar < 75:
                aux = 75 - Observar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de observacion\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de observacion esta muy por debajo\n"

            if Escuchar >= 50 and Escuchar < 75:
                aux = 75 - Escuchar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de escucha\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de escucha esta muy por debajo\n"

            if Analisis >= 40 and Analisis < 60:
                aux = 60 - Analisis
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de analisis\n"
            elif Analisis > 90:
                aux = 100 - Analisis
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le sobran "+str(aux)+" pts de competencia de analisis\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de analisis esta muy por debajo\n"
        #Habilidades
        if Analitico >= 60 and Analitico <= 90:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia Biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1

        #Factores Ambientales
        if EstabSoc >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: GERENTE DE PRODUCCION")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE DIR TECNICO
        #Necesidades
        if Supervision >= 75 and Desarrollo >= 80:
            aciertos = aciertos + 1
        else:
            if Supervision >= 50 and Supervision < 75:
                aux = 75 - Supervision
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de supervision\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de supervision esta muy por debajo\n"

            if Desarrollo >= 50 and Desarrollo < 80:
                aux = 80 - Desarrollo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de desarrollo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de desarrollo esta muy por debajo\n"
        #Capacidades
        if  ManejoTecnologias >= 80 and (Analisis >= 75 and Analisis <=90):
            aciertos = aciertos + 1
        else:
            if ManejoTecnologias >= 50 and ManejoTecnologias < 80:
                aux = 80 - ManejoTecnologias
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de manejo de tecnologias especificas\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de manejo de tecnologias especificas esta muy por debajo\n"

            if Analisis >= 50 and Analisis < 75:
                aux = 75 - Analisis
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de analisis\n"
            elif Analisis > 90:
                aux = 100 - Analisis
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de analisis\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de analisis esta muy por debajo\n"

        #Habilidades
        if Analitico >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia Biografica
        if CarEmocional >= 50:
            aciertos = aciertos + 1

        #Factores ambientales
        if EstabSoc >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: DIRECTOR TECNICO")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE DIR COMERCIAL
        #Necesidades
        if Progreso >= 75 and Responsabilidad >= 75:
            aciertos = aciertos + 1
        else:
            if Progreso >= 50 and Progreso < 75:
                aux = 75 - Progreso
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de progreso\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de progreso esta muy por debajo\n"

            if Responsabilidad >= 50 and Responsabilidad <75:
                aux = 75 - Responsabilidad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de responsabilidad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de responsabilidad esta muy por debajo\n"

        #Capacidades
        if  Observar >= 80 and Escuchar >= 80 and ComuniacionOral >= 80:
            aciertos = aciertos + 1
        else:
            if Observar >= 50 and Observar < 80:
                aux = 80 - Observar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La faltan "+str(aux)+" pts de necesidad de observar\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de observar esta muy por debajo\n"

            if Escuchar >= 50 and Escuchar < 80:
                aux = 80 - Escuchar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La faltan "+str(aux)+" pts de necesidad de escuchar\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de escuchar esta muy por debajo\n"

            if ComuniacionOral >= 50 and ComuniacionOral < 80:
                aux = 80 - ComuniacionOral
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La faltan "+str(aux)+" pts de necesidad de comunicacion oral\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de comunicacion oral esta muy por debajo\n"

        #Habilidades
        if Analitico >= 60:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1

        #Factores ambientales
        if EstabSoc >= 50 :
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: DIRECTOR COMERCIAL")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE DIR DE SEGURIDAD
        #Necesidades
        if Seguridad >= 80 and Responsabilidad >= 80:
            aciertos = aciertos + 1
        else:
            if Seguridad >= 50 and Seguridad < 80:
                aux = 80 - Seguridad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de seguridad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de seguridad esta muy por debajo\n"

            if Responsabilidad >= 50 and Responsabilidad < 80:
                aux = 80 - Responsabilidad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de responsabilidad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de responsabilidad esta muy por debajo\n"

        #Capacidades
        if (Motricidad >= 75 and Motricidad <= 95) and SeguirPrescripciones >= 80:
            aciertos = aciertos + 1
        else:
            if Motricidad >= 50 and Motricidad < 75:
                aux = 75 - Motricidad
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le fantan "+str(aux)+" pts a la capacidad de motricidad\n"
            elif Motricidad > 75:
                aux = 100 - Motricidad
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le sobran " + str(aux) + " pts a la capacidad de motricidad\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de motricidad esta muy por debajo\n"

        #Habilidades
        if Analitico >= 80 and Empatico >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 50:
            aciertos = aciertos + 1

        #Factores ambientales
        if SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: DIRECTOR DE SEGURIDAD")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE SECRETARIO(A) DE GERENTE GENERAL
        #Necesidades
        if (Destacarse >= 60 and Destacarse <= 90) and Responsabilidad >= 80 and Sueldo >= 75:
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse < 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Responsabilidad >= 50 and Responsabilidad <80:
                aux = 80 - Responsabilidad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de responsabilidad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de responsabilidad esta muy por debajo\n"

            if Sueldo >= 50 and Sueldo < 75:
                aux = 75 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de sueldo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de sueldo esta muy por debajo\n"

        #Capacidades
        if Lectura >= 85 and CompresionTxt >= 85 and Obediencia >= 80 and Compromiso >= 80:
            aciertos = aciertos + 1
        else:
            if Lectura >= 50 and Lectura < 85:
                aux = 85 - Lectura
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de lectura\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de lectura esta muy por debajo\n"

            if CompresionTxt >= 50 and CompresionTxt < 85:
                aux = 85 - CompresionTxt
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de compresion de textos\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de compresion de textos esta muy por debajo\n"

            if Obediencia >= 50 and Obediencia <80:
                aux = 80 - Obediencia
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de obediencia\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de obediencia esta muy por debajo\n"

            if Compromiso >= 50 and Compromiso <80:
                aux = 80 - Compromiso
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de compromiso\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de compromiso esta muy por debajo\n"

        #Habilidades
        if Disciplinado >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 75 or CarEmocional >= 75:
            aciertos = aciertos + 1

        #Factores ambientales
        if SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: SECRETARIO(A) DEL GERENTE GENERAL")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE SECRETARIO(A) DEL GERENTE DE FINANZAS
        #Necesidades
        if (Destacarse >= 60 and Destacarse <= 90) and Responsabilidad >= 80 and Sueldo >= 75:
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse < 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Responsabilidad >= 50 and Responsabilidad <80:
                aux = 80 - Responsabilidad
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de responsabilidad\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de responsabilidad esta muy por debajo\n"

            if Sueldo >= 50 and Sueldo < 75:
                aux = 75 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de sueldo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de sueldo esta muy por debajo\n"

        #Capacidades
        if Lectura >= 85 and CompresionTxt >= 85 and Obediencia >= 80 and Compromiso >= 80:
            aciertos = aciertos + 1
        else:
            if Lectura >= 50 and Lectura < 85:
                aux = 85 - Lectura
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de lectura\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de lectura esta muy por debajo\n"

            if CompresionTxt >= 50 and CompresionTxt < 85:
                aux = 85 - CompresionTxt
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de compresion de textos\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de compresion de textos esta muy por debajo\n"

            if Obediencia >= 50 and Obediencia <80:
                aux = 80 - Obediencia
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de obediencia\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de obediencia esta muy por debajo\n"

            if Compromiso >= 50 and Compromiso <80:
                aux = 80 - Compromiso
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de compromiso\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de compromiso esta muy por debajo\n"

        #Habilidades
        if Disciplinado >= 75:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 75 or CarEmocional >= 75:
            aciertos = aciertos + 1

        #Factores ambientales
        if SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: SECRETARIO(A) DE GERENTE DE FINANZAS")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE RECEPCIONISTA
        #Necesidades
        if (Destacarse >= 60 and Destacarse <= 90) and Social >= 75 and Afiliacion >= 80 and Sueldo >= 80:
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse < 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destacarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Social >= 50 and Social < 75:
                aux = 75 - Social
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad social\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad social esta muy por debajo\n"

            if Afiliacion >= 50 and Afiliacion < 80:
                aux = 80 - Afiliacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de afiliacion\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de afiliacion esta muy por debajo\n"

            if Sueldo >= 50 and Sueldo < 80:
                aux = 80 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de sueldo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de sueldo esta muy por debajo\n"

        #Competencias
        if ComuniacionOral >= 85 and Observar >= 85:
            aciertos = aciertos + 1
        else:
            if ComuniacionOral >= 50 and ComuniacionOral < 85:
                aux = 85 - ComuniacionOral
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de comuniacion oral\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La necesidad de comuniacion oral esta muy por debajo\n"

            if Observar >= 50 and Observar < 85:
                aux = 85 - Observar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de observar\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La necesidad de observar esta muy por debajo\n"

        #Habilidades
        if Disciplinado >= 80:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 75 or CarEmocional >= 75:
            aciertos = aciertos + 1

        #Factores ambientales
        if EstabSoc >= 60 and SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: RECEPCIONISTA")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE ASISTENTE
        #Necesidades
        aux = 0
        if (Destacarse >= 60 and Destacarse <= 90) and Afiliacion >= 85 and Sueldo >= 80:
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse < 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destacarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Afiliacion >= 50 and Afiliacion < 85:
                aux = 85 - Afiliacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de afiliacion\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de afiliacion esta muy por debajo\n"

            if Sueldo >= 50 and Sueldo < 80:
                aux = 80 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de sueldo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de sueldo esta muy por debajo\n"

        #Capacidades
        aux = 0
        if (SeguirPrescripciones >= 60 and SeguirPrescripciones <= 90) and Obediencia >= 80:
            aciertos = aciertos + 1
        else:
            if SeguirPrescripciones >= 40 and SeguirPrescripciones < 60:
                aux = 60 - SeguirPrescripciones
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de capacidad de seguir prescripciones para hacer una rutina de trabajo\n"
            elif SeguirPrescripciones > 90:
                aux = 100 - SeguirPrescripciones
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le sobran "+str(aux)+" pts de capacidad de seguir prescripciones para hacer una rutina de trabajo\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de seguir prescripciones para hacer una rutina de trabajo esta muy por debajo\n"

            if Obediencia >= 50 and Obediencia < 80:
                aux = 80 - Obediencia
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de capacidad de obediencia\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La faltan "+str(aux)+" pts de capacidad de obediencia\n"

        #Habilidades
        if Disciplinado >= 80:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 75 or CarEmocional >= 75:
            aciertos = aciertos + 1

        #Factores ambientales
        if SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: ASISTENTE")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE VENDEDOR
        #Necesidades
        if (Destacarse >= 60 and Destacarse <= 90) and (Afiliacion >= 60 and Afiliacion <= 90) and (Sueldo >= 60 and Sueldo <= 90):
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse <= 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destacarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Afiliacion >= 40 and Afiliacion <= 60:
                aux = 60 - Afiliacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de afiliacion\n"
            elif Destacarse > 90:
                aux = 100 - Afiliacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de afiliacion\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de afiliacion esta muy por debajo\n"

            if Sueldo >= 40 and Sueldo <= 60:
                aux = 60 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de sueldo\n"
            elif Sueldo > 90:
                aux = 100 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de sueldo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de sueldo esta muy por debajo\n"

        #Competencias
        if ComuniacionOral >= 85 and Observar >= 85:
            aciertos = aciertos + 1
        else:
            if ComuniacionOral >= 50 and ComuniacionOral < 85:
                aux = 85 - ComuniacionOral
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de comunicacion oral\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de comunicacion oral esta muy por debajo\n"

            if Observar >= 50 and Observar < 85:
                aux = 85 - Observar
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de observar\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La capacidad de observar esta muy por debajo\n"


        #Habilidades
        if Disciplinado >= 80:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 75 or CarEmocional >= 75:
            aciertos = aciertos + 1

        #Factores ambientales
        if SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: VENDEDOR")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        NecesidadesMejorar = ""
        CompetenciasMejorar = ""
        aciertos = 0

        Hab = True

        #ANALISIS DEL ROL DE AUXILIAR DE SERVICIOS
        #Necesidades
        if (Destacarse >= 60 and Destacarse <= 90) and Sueldo >= 80 and Autorrealizacion >= 80 and RelacionesAmigables >= 80:
            aciertos = aciertos + 1
        else:
            if Destacarse >= 40 and Destacarse < 60:
                aux = 60 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de destacarse\n"
            elif Destacarse > 90:
                aux = 100 - Destacarse
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le sobran "+str(aux)+" pts de necesidad de destacarse\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de destacarse esta muy por debajo\n"

            if Sueldo >= 50 and Sueldo < 80:
                aux = 80 - Sueldo
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de sueldo\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de sueldo esta muy por debajo\n"

            if Autorrealizacion >= 50 and Autorrealizacion < 80:
                aux = 80 - Autorrealizacion
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de autorrealizacion\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de autorrealizacion esta muy por debajo\n"

            if RelacionesAmigables >= 50 and RelacionesAmigables < 80:
                aux = 80 - RelacionesAmigables
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -Le faltan "+str(aux)+" pts de necesidad de afan por tener relaciones amigables y estrechas\n"
            else:
                NecesidadesMejorar = NecesidadesMejorar + "\t\t -La necesidad de afan por tener relaciones amigables y estrechas esta muy por debajo\n"

        #Competencias
        if Obediencia >= 80:
            aciertos = aciertos + 1
        else:
            if Obediencia >= 50:
                aux = 80 - Obediencia
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -Le faltan "+str(aux)+" pts de competencia de obediencia\n"
            else:
                CompetenciasMejorar = CompetenciasMejorar + "\t\t -La competencia de obediencia esta muy por debajo\n"

        #Habilidades
        if Disciplinado >= 80:
            aciertos = aciertos + 1
            Hab = True
        else:
            Hab = False

        #Historia biografica
        if CarMaterial >= 75 or CarEmocional >= 75:
            aciertos = aciertos + 1

        #Factores ambientales
        if SocSolidaria >= 50:
            aciertos = aciertos + 1

        # REPORTE
        print("\t\tROL: AUXILIAR DE SERVICIOS")
        ReporteRol(aciertos, Hab, NecesidadesMejorar, CompetenciasMejorar)
        print("\n\n")

        raw_input("pulse enter para voler al menu")

    elif op == 0:
        os.system ("cls")
        print("--- El programa se Cerrara ---")
        print("\n")
        raw_input("pulse enter para cerrar")
        salida = False
    else:
        os.system ("cls")
        print("--- Ingrese una opcion valida ---")
        print("\n")
        raw_input("pulse enter para volver al menu")
    
os.system('cls')