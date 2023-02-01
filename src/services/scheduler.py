from src.components.colegio import *
from datetime import *

asig1 = Asignatura("Moviles", 4)
asig2 = Asignatura("Servicios y procesos: VB", 7)
asig3 = Asignatura("Servicios y procesos: Python", 7)
asig4 = Asignatura("Desarrollo de Interfaces", 3)
asig5 = Asignatura("Ingles", 2)
asig6 = Asignatura("Empersa", 3)
asig7 = Asignatura("Navision", 3)
asig8 = Asignatura("Amazon", 2)
asig9 = Asignatura("Acceso a datos", 5)
asig10 = Asignatura("Big data", 2)

hor_prof1 = [["8", "14:30"], ["8","20:30"], ["8", "14:30"], ["8", "14:30"], ["8", "14:30"]]
list_prof1 = [asig7, asig8]
prof1 = Profesor(1,True, "Paco", hor_prof1, list_prof1)
hor_prof2 = [["8", "16:30"], ["8","15:25"], ["8", "15:25"], ["8", "16:30"], ["8", "15:25"]]
list_prof2 = [asig1, asig4]
prof2 = Profesor(2, False, "Guillermo", hor_prof2, list_prof2)
hor_prof3 = [["8", "14:30"], ["8","14:30"], ["8", "20:30"], ["8", "14:30"], ["8", "14:30"]]
list_prof3 = [asig3]
prof3 = Profesor(3, False, "David", hor_prof3, list_prof3)
hor_prof4 = [["8", "17:20"], ["8","14:30"], ["8", "14:30"], ["8", "14:30"], ["8", "17:20"]]
list_prof4 = [asig2]
prof4 = Profesor(4, False, "Tere", hor_prof4, list_prof4)
hor_prof5 = [["8", "18:40"], ["8","14:30"], ["8", "16:25"], ["8", "14:30"], ["8", "14:30"]]
list_prof5 = [asig5]
prof5 = Profesor(5, False, "Olga", hor_prof5, list_prof5)
hor_prof6 = [["8", "14:30"], ["8","14:30"], ["8", "14:30"], ["8", "14:30"], ["8", "19:40"]]
list_prof6 = [asig10]
prof6 = Profesor(6, False, "Luisa", hor_prof6, list_prof6)
hor_prof7 = [["8", "14:30"], ["8","14:30"], ["8", "14:30"], ["8", "21:30"], ["8", "14:30"]]
list_prof7 = [asig9]
prof7 = Profesor(7, False, "pedro", hor_prof7, list_prof7)
hor_prof8 = [["8", "21:30"], ["8","14:30"], ["8", "14:30"], ["8", "14:30"], ["8", "14:30"]]
list_prof8 = [asig6]
prof8 = Profesor(8, False, "Isabel/John", hor_prof8, list_prof8)

list_asignaturas1 = [asig1, asig2, asig3, asig4, asig5, asig6, asig7, asig8, asig9, asig10]
list_profesores1 = [prof1, prof2, prof3, prof4, prof5, prof6, prof7, prof8]
grp1 = Grupo("Dam-2b" ,list_asignaturas1, prof1, list_profesores1, "TARDE")

def generar(_grupos:list[Grupo]) -> list[list[list[Hora_horario]]]:
    """
        Genera un horario para un solo grupo
    """

    # print("hola y david si ves esto significa q ahora te toca currar cual hdp mucha suerte con cariño david del pasado :)")

    rtn:list[list[list[Hora_horario]]] = []

    for grupos in _grupos:
        h_restantes:list[int] = []
        cont:int = 0
        num_clases:int = 0

        # Crea un array con las horas restantes de cada profesor
        for pro in grupos.Profesores():
            if len(pro.Asignaturas()) > 1:
                for asig in pro.Asignaturas():
                    cont += asig.HorasSemanales()
                h_restantes.append(cont)
                cont = 0
            else:
                h_restantes.append(pro.Asignaturas()[0].HorasSemanales())

        print(h_restantes)

        # Asigna la primera hora dependiendo del turno
        if grupos.Horario() == "TARDE":
            primera_hora = time(14,30)
            
        elif grupos.Horario() == "MAÑANA":
            primera_hora = time(8)
            

       # Le da una hora a cada clase del horario y le asigna el grupo al que pertenece
        horario:list = [[Hora_horario() for x in range(7)] for j in range(5)]
        for i in range(5):
            for j in range(7):
                horario[i][j].Grupo(grupos)
                t = primera_hora.hour
                t = t+j+1
                if grupos.Horario() == 'TARDE':
                    horario[i][j].Tiempo(time(t,30))
                elif grupos.Horario() == 'MAÑANA':
                    horario[i][j].Tiempo(time(t))
                # print(horario[i][j].Tiempo())
        
        prf_h:list[list[str]] = [["0" for i in range(7)]for j in range(5)]
        prf_hg:list[list[str]] = [["0" for i in range(7)]for j in range(5)]

        # Crea el un array con los horarios de los profesores que ya estan asignados en otros grupos
        if rtn != []:
            for horario_grupo in rtn:
                if horario_grupo[0][0].Grupo().Horario() == grupos.Horario():
                    for i in range(5):
                        for j in range(7):
                            if horario_grupo[i][j].Profesor() != None:
                                if str(horario_grupo[i][j].Profesor().Id()) not in prf_hg[i][j].split('-'):
                                    prf_hg[i][j] += '-' + str(horario_grupo[i][j].Profesor().Id())
                            

               
        print(prf_hg) 

        # Crea el horario de disponibilidad de los profesores en el horario actual comparandola con el de la funcion de arriba
        for i in range(5):
            for j in range(7):
                chiv = False
                for profe in grupos.Profesores():
                    if int(profe.Horario()[i][1].split(':')[0]) >= horario[i][j].Tiempo().hour:
                        if prf_hg[i][j] != '0':
                            if str(profe.Id()) not in prf_hg[i][j].split('-'):
                                prf_h[i][j] += '-' + str(profe.Id())
                        else:
                            prf_h[i][j] += '-' + str(profe.Id())    

        # Elimina los 0 de las clases en las que hay algun profesor    
        for i in range(5):
            for j in range(7):
                if len(prf_h[i][j]) != 1:
                    prf_h[i][j] = prf_h[i][j][1:]

        print(prf_h)

        # //Asigna clase a los profesores con 2 coincidencias  esta puede llegar a ser toda la funcion   
        coinc_p:list[Profesor] = []
        coinc_hr:list[int] = []
        aux_p:Profesor = ''
        aux_hr:int = 0
        aux = 0
        cont3 = 0
        chiv = True
        flug = True
        cont = 0

        while chiv:
            chiv = False
            if flug == True:
                cont += 1
            else:
                cont = 1
            flug = True
            for i in range(5):
                for j in range(7):
                    if len(prf_h[i][j].split('-'))-1 == cont:
                        flug = False
                        coinc_hr = []
                        coinc_p = []
                        for pro in grupos.Profesores():
                            for p in prf_h[i][j].split('-'):
                                if p != '':
                                    if int(p) == pro.Id():
                                        coinc_p.append(pro)
                                        coinc_hr.append(cont3)          
                            cont3 += 1
                        cont3 = 0
                        if coinc_hr[0] != None:
                            aux_hr = h_restantes[coinc_hr[0]]
                            aux_p = coinc_p[0]
                            aux = coinc_hr[0]
                            for t in range(len(coinc_p)):
                                if aux_hr < h_restantes[coinc_hr[t]]:
                                    aux_hr = h_restantes[coinc_hr[t]]
                                    aux_p = coinc_p[t]
                                    aux = coinc_hr[t]
                            horario[i][j].Profesor(aux_p)
                            h_restantes[aux] -= 1
                            ind = '-' + str(horario[i][j].Profesor().Id())
                            prf_h[i][j] = str(aux_p.Id())
                            if h_restantes[aux] == 0:
                                for i in range(5):
                                    for j in range(7):
                                        prf_h[i][j] = prf_h[i][j].replace(ind,'')
                                        if prf_h[i][j] == '':
                                            prf_h[i][j] = '0'

            for h in h_restantes:
                if h != 0:
                    chiv = True

                            

                
        
        # //Te imprime el horario (Profesores)
        arrd = []
        arr = []

        for i in range(5):
            for j in range(7):
                if horario[i][j].Profesor() == None:
                    arr.append("None")
                else:
                    arr.append(horario[i][j].Profesor().Nombre())
            arrd.append(arr)
            arr = []
        for ar in arrd:
            print(ar)  

        print(h_restantes)
        print(prf_h)

        # //Crea un array con el numero de horas semanales que se deben dar cada asignatura
        asignaturas_hr:list[int] =  []

        for asignatura in grupos.Asignaturas():
                asignaturas_hr.append(asignatura.HorasSemanales())
        
        print(asignaturas_hr)

        # //Le asigna una asignatura a cada hora del horario
        for i in range(5):
            for j in range(7):
                if horario[i][j].Profesor() != None:
                    if len(horario[i][j].Profesor().Asignaturas()) > 1:
                        for t in range(len(grupos.Asignaturas())):
                            if grupos.Asignaturas()[t] in horario[i][j].Profesor().Asignaturas() and asignaturas_hr[t] > 0:
                                if horario[i][j].Nombre() == None:
                                    horario[i][j].Nombre(grupos.Asignaturas()[t])
                                    asignaturas_hr[t] -= 1
                    else:
                        horario[i][j].Nombre(horario[i][j].Profesor().Asignaturas()[0])
                


        # //Te imprime el horario (Asignaturas)
        arrd = []
        arr = []

        for i in range(5):
            for j in range(7):
                if horario[i][j].Nombre() == None:
                    arr.append("None")
                else:
                    arr.append(horario[i][j].Nombre().Nombre())
            arrd.append(arr)
            arr = []
        for ar in arrd:
            print(ar)            

        rtn.append(horario)

    return rtn


    # //Les añade a las clases del horario un profesor en el caso de que solo pueda el a esa hora
    rounds = 0
    chiv = True
    while (chiv):
        cont = 0
        cont2 = 0
        chiv = False

        for i in range(5):
            for j in range(7):
                if len(prf_h[i][j].split('-'))-1 == 1:
                    for pro in grupos.Profesores():
                        if prf_h[i][j].split('-')[1] == str(pro.Id()):
                            horario[i][j].Profesor(pro)
                            h_restantes[cont] -= 1
                        cont += 1
                    cont = 0
        
        rounds += 1
        # print(rounds)

        # //Comprueba si no quedan horas restantes
        for h in h_restantes:
            if h != 0:
                chiv = True

        
        # //Te quita el profesor si ya tiene clase asignada en esa hora
        for i in range(5):
            for j in range(7):
                if horario[i][j].Profesor() != None:
                    ind = '-' + str(horario[i][j].Profesor().Id())
                    prf_h[i][j] = prf_h[i][j].replace(ind,'')

        # //Te quita el profesor si las horas restantes son 0
        for pro in grupos.Profesores():
            if h_restantes[cont2] == 0:
                for i in range(5):
                    for j in range(7):
                        ind = '-' + str(pro.Id())
                        prf_h[i][j] = prf_h[i][j].replace(ind,'')
            cont2 += 1

          
         

    

    
    # //Te imprime el horario
    # arrd = []
    # arr = []

    # for i in range(5):
    #     for j in range(7):
    #         if horario[i][j].Profesor() == None:
    #              arr.append("None")
    #         else:
    #             arr.append(horario[i][j].Profesor().Nombre())
    #     arrd.append(arr)
    #     arr = []

    # for ar in arrd:
    #     print(ar)  

    # //Te quita el profesor si las horas restantes son 0
    # cont = 0
    # ind:str = ''
    # for pro in grupos.Profesores():
    #     if h_restantes[cont] == 0:
    #         for i in range(5):
    #             for j in range(7):
    #                 ind = '-' + str(pro.Id())
    #                 prf_h[i][j] = prf_h[i][j].replace(ind,'')
    #     cont += 1
             
    # //Te quita el profesor si ya tiene clase asignada en esa hora
    # for i in range(5):
    #         for j in range(7):
    #             if horario[i][j].Profesor() != None:
    #                 ind = '-' + str(horario[i][j].Profesor().Id())
    #                 prf_h[i][j] = prf_h[i][j].replace(ind,'')

    
    
                    
                    

     


    

    
    

