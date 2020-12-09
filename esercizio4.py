risposta=(input("Di quale poligono vuoi calcolare l'area? (triangolo, rettangolo, cerchio, quadrato) "))
if risposta == "quadrato":
    print("Hai scelto il quadrato, inserire i dati:")
    lato_quadrato=int(input("Inserire la lunghezza del lato del quadrato di cui vuoi calcolare l'area: "))
    area_quadrato=lato_quadrato*lato_quadrato
    print("L'area del quadrato è ", area_quadrato)
elif risposta == "rettangolo":
    print("Hai scelto il rettangolo, inserire i dati:")
    base_rettangolo=int(input("Inserire la lunghezza della base del rettangolo di cui vuoi calcolare l'area: "))
    altezza_rettangolo=int(input("Ora inserire la lunghezza dell'altezza di quest'ultimo: "))
    area_rettangolo=(base_rettangolo*altezza_rettangolo)/2
    print("L'area del rettangolo è ", area_rettangolo)
elif risposta == "triangolo":
    print("Hai scelto il triangolo, inserire i dati:")
    base_triangolo=int(input("Inserire la lunghezza della base del triangolo di cui vuoi calcolare l'area: "))
    altezza_triangolo=int(input("Inserire la lunghezza della base di quest'ultimo: "))
    area_triangolo=(base_triangolo*altezza_triangolo)/2
    print("L'area del triangolo è ", area_triangolo)
elif risposta == "cerchio":
    print("Hai scelto il cerchio, inserire i dati:")
    raggio_cerchio=int(input("Inserire il raggio del cerchio di cui si vuole calcolare l'area: "))
    area_cerchio=(raggio_cerchio*2)*3.14
    print("L'area del cerchio è ", area_cerchio)

























