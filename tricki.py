import funciones as fn


if __name__=="__main__":
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
                bm,v=fn.mejor_mov(campo)
                campo=fn.mover(campo,bm,"CPU")
                print(campo)
                turnos-=1
                next
        else:
            break
    ganador=fn.ganador(campo)
    print(f"Fin del juego, el resultado es {ganador}")
