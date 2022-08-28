from PyQt5 import QtTest


def setProgress(bar):#funcion que va a llenar la barra de progreso, sera individual asi que se tiene que mandar como parametro a cada barra
    progress =0
    while bar.value() != 100:#mientras que el valor de la barra no sea 100
        
        bar.setValue(progress)#seteamos el progreso
        QtTest.QTest.qWait(500)#esperamos unos segundos para que sea visual la carga
        progress+=5#incrementamos el valor de la variable para que vaya incrementando

def setProgressInterface(widget):
    widget.startButton.setEnabled(False)#deshabilitamos el boton para que no interfiera en el procesamiento
    widget.bar_1.setValue(0)#igualamos las barras a 0 por si se requiere volver a ejecutar el programa limpiar
    widget.bar_2.setValue(0)
    widget.bar_3.setValue(0)
    widget.bar_4.setValue(0)
    widget.bar_5.setValue(0)
    setProgress(widget.bar_1)#llamamos a la funcion y mandamos cada una de las barras
    setProgress(widget.bar_2)#mientras no se acabe una la otra no iniciará
    setProgress(widget.bar_3)
    setProgress(widget.bar_4)
    setProgress(widget.bar_5)
    