import funciones as fn


if __name__=="__main__":
    dificultad=int(input("""
Por favor seleccione la dificultad que prefiere para el juego:
1. facil
2. Media
3. dificil 
"""))
    print("-"*7+"CAMPO DE JUEGO"+"-"*7)
    campo=fn.iniciar_campo()
    turnos=9
    while turnos>0:
        if turnos%2==1:
            if fn.final(campo):
                break
            else:
                print("\nTURNO J1")
                mov_usuario=input("""
                    Por favor indicar la letra en donde planea colocar su 
                      ficha 
                      """)
                campo=fn.ubicarEnCampo(campo,mov_usuario)
                print(campo)
                turnos-=1
                next
        elif turnos%2==0:
            if fn.final(campo):
                break
            else:
                print("\nTURNO CPU")
                #bm,v=fn.mejor_mov(campo)
                if dificultad==1:
                    v, bm=fn.min_value(campo,1)
                    campo=fn.mover(campo,bm,"CPU")
                    print(campo)
                    turnos-=1
                    next
                elif dificultad==2:
                    v, bm=fn.min_value(campo,3)
                    campo=fn.mover(campo,bm,"CPU")
                    print(campo)
                    turnos-=1
                    next
                else:
                    v, bm=fn.min_value(campo,7)
                    campo=fn.mover(campo,bm,"CPU")
                    print(campo)
                    turnos-=1
                    next
        else:
            break
    ganador=fn.ganador(campo)
    print(f"Fin del juego, el resultado es {ganador}")
