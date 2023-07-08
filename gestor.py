import os

import PyQt5
from src.func.funciones import *
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QAbstractItemView, QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsTextItem, QMenu, QSystemTrayIcon
from PyQt5.QtCore import QDate, QTimer, Qt, QTime
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtCore, QtWidgets

class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        loadUi("proyecto_tareas.ui", self)

        fecha_actual = QDate.currentDate()
        hora=QTime.currentTime()
        self.tableWidgetBuscar.hide()
        self.LabelMsj.hide()
        self.limite_caja_texto()

        self.calendarWidgetAgregar.setMinimumDate(fecha_actual)
        self.TituloAgregar.textChanged.connect(self.check_text)
        self.DescripcionAgregar.textChanged.connect(self.check_text)

        self.BotonAgregarT.setEnabled(False)
        self.DescripcionAgregar.textChanged.connect(self.cambiarBoton)
        self.TituloAgregar.textChanged.connect(self.cambiarBoton)
        self.HyMedit.setTime(hora)
        self.HyMedit.timeChanged.connect(self.cambiarHorario)
        self.calendarWidgetAgregar.clicked.connect(self.cambiarHorario)

        self.MaximizeButton.hide()
        self.MinimizeButton.clicked.connect(self.ctrl_minimize)
        self.NormalButton.clicked.connect(self.ctrl_maximize)
        self.MaximizeButton.clicked.connect(self.ctrl_normal)
        self.ExitButton.clicked.connect(lambda: self.close())

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)


        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.frame_superior.mousePressEvent = self.guardar_posicion_clic
        self.stackedWidget.setCurrentWidget(self.page)
        self.BotonAgregarT.clicked.connect(self.obtener_datos)
        self.Agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.Agregar.clicked.connect(lambda: self.LabelMsj.hide())
        self.Buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Editar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.Eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.Completar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.Completas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.Pendientes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.Todas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.Buscar.clicked.connect(self.verBuscar)
        self.Buscar.clicked.connect(self.ocultar)
        self.SelectTitulo.clicked.connect(self.tituloB)
        self.SelectPrioridad.clicked.connect(self.prioriB)
        self.SelectFechaVencimiento.clicked.connect(self.calendarB)
        self.TituloBuscar.textChanged.connect(self.check_text)

        self.Editar.clicked.connect(lambda: self.BotonEditarT.setEnabled(False))
        self.Completar.clicked.connect(self.menuCompletar)

        self.TituloBuscar.textChanged.connect(self.cambiarBotonB)
        self.SelectFechaVencimiento.clicked.connect(lambda: self.BotonBuscarT.setEnabled(True))
        self.SelectTitulo.clicked.connect(lambda: self.BotonBuscarT.setEnabled(False))
        self.DescripcionEditar.clicked.connect(lambda: self.BotonEditarT.setEnabled(False))
        self.SelectPrioridad.clicked.connect(lambda: self.BotonBuscarT.setEnabled(True))
        self.BotonBuscarT.clicked.connect(self.buscarTareas)
        self.tableWidgetBuscar.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetBuscar.setDragDropOverwriteMode(False)
        self.tableWidgetBuscar.setTextElideMode(Qt.ElideRight)
        self.Editar.clicked.connect(self.mostrarTodo)
        self.Editar.clicked.connect(self.sacarTodo)
        self.BotonEditarT.setEnabled(False)
        self.TituloEditar.clicked.connect(self.mostrarTituloEdit)
        self.DescripcionEditar.clicked.connect(self.mostrarDescriptEdit)
        self.PrioridadEditar.clicked.connect(self.mostrarPrioridadEdit)
        self.VencimientoEditar.clicked.connect(self.mostrarVenceEdit)
        self.TituloEdit.textChanged.connect(self.textoEditar)
        self.TituloEdit_2.textChanged.connect(self.textoEditar)
        self.DescripcionEdit.textChanged.connect(self.textoEditar)
        self.TituloEdit.textChanged.connect(self.check_text)
        self.TituloEdit_2.textChanged.connect(self.check_text)
        self.DescripcionEdit.textChanged.connect(self.check_text)
        self.VencimientoEditar.clicked.connect(self.habilitarBoton2)
        self.PrioridadEditar.clicked.connect(self.habilitarBoton2)
        self.BotonEditarT.clicked.connect(self.EditarTarea)
        self.Agregar.clicked.connect(lambda: self.tableWidgetBuscar.hide())
        self.Completas.clicked.connect(self.completas)
        self.Pendientes.clicked.connect(self.pendientes)
        self.TituloCompletar.textChanged.connect(self.completarT)
        self.TituloCompletar.textChanged.connect(self.check_text)

        self.BotonCompletarT.clicked.connect(self.completarLasT)
        self.TituloEliminar.textChanged.connect(self.check_text)
        self.Eliminar.clicked.connect(self.eliminarT)
        self.TituloEliminar.textChanged.connect(self.cambioTextoEliminar)
        self.BotonEliminarT.clicked.connect(self.eliminarTarea)
        self.BotonEliminarT.clicked.connect(self.comprobarTareas)
        self.BotonCompletarT.clicked.connect(self.comprobarTareas)
        self.BotonAgregarT.clicked.connect(self.comprobarTareas)
        self.BotonEditarT.clicked.connect(self.comprobarTareas)
        self.Todas.clicked.connect(self.verTodo)
        self.tableWidgetBuscar.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)


        self.graphics_view = QGraphicsView(self.frame_8)
        self.graphics_view.setGeometry(0, 0, 400, 120)

        self.scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setFixedSize(400, 120)
        self.text_item = QGraphicsTextItem()
        self.text_item.setTextWidth(400)
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.text_item.setFont(font)
        self.scene.addItem(self.text_item)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scroll_text)
        self.timer.start(40)
        self.comprobarTareas()

        self.ExitButton.clicked.connect(self.cerrarBd)
        self.notificacion()
        self.BotonAgregarT.clicked.connect(self.notificacion)

    def notificacion(self):
        res=todas()
        if res:
            e=self.actualizarTareas()
            if(e>0):
                app_path = os.path.dirname(os.path.abspath(__file__)) # ruta actual donde se ejecuta el programa
                icon = QIcon(f"""{app_path}/app.ico""")
                tray_icon = QSystemTrayIcon(icon, app)
                menu = QMenu()
                tray_icon.setContextMenu(menu)
                tray_icon.show()
                tray_icon.showMessage("Gestor de tareas", f"tienes {e} tarea/s que vence/n en un dia", QSystemTrayIcon.Information, 5000)

    def cambiarHorario(self):
        fecha=self.calendarWidgetAgregar.selectedDate()
        if fecha_actual==fecha:
            self.HyMedit.setMinimumTime(QTime.currentTime())
        else:
            self.HyMedit.setMinimumTime(QTime(0,0))

    def comprobarTareas(self):
        res = todas()
        if res:
            self.actualizarTareas()
        else:
            mensaje = 'no hay tareas'
            self.text_item.setPlainText(mensaje)  # Asignar el texto al QGraphicsTextItem creado mas arriba
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.scroll_text)

    def verTodo(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        res = todas()
        try:
            self.imprimir_tuplas(res)
        except Exception:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()

    def eliminarTarea(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        textoE = self.TituloEliminar.text()
        try:
            delete(textoE)
            self.LabelMsj.setStyleSheet('color:blue; border:0px')
            self.LabelMsj.setText('Tarea eliminada correctamente')
            self.LabelMsj.show()
            res = todas()
            self.imprimir_tuplas(res)
        except ValueError:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No se elimino la tarea porque no existe')
            self.LabelMsj.show()
        except Exception:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()
        self.TituloEliminar.setText("")

    def cambioTextoEliminar(self):
        text=self.TituloEliminar.text()
        if text:
            self.BotonEliminarT.setEnabled(True)
        else:
            self.BotonEliminarT.setEnabled(False)

    def eliminarT(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        res = todas()
        try:
            self.imprimir_tuplas(res)
        except Exception:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()
        self.BotonEliminarT.setEnabled(False)

    def verBuscar(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        try:
            res = todas()
            self.imprimir_tuplas(res)
        except Exception:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()
        self.BotonBuscarT.setEnabled(False)

    def menuCompletar(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        try:
            res = todas()
            self.imprimir_tuplas(res)
        except Exception:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()
        self.BotonCompletarT.setEnabled(False)

    def completarLasT(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        text = self.TituloCompletar.text()
        try:
            result = busqueda(text)
            if result[4]=='pendiente':
                completa=completar_tarea(text)
                self.imprimir_tuplas(completa)
                self.LabelMsj.setStyleSheet('color:blue; border:0px')
                self.LabelMsj.setText('Se mostrara la tarea a completar')
                self.LabelMsj.show()
            elif result[4]=='completa':
                self.LabelMsj.setStyleSheet('color:green; border:0px')
                self.LabelMsj.setText('La tarea ya estaba completa')
                self.LabelMsj.show()
            elif result[4]=='vencida':
                self.LabelMsj.setStyleSheet('color:green; border:0px')
                self.LabelMsj.setText('La tarea ya estaba vencida')
                self.LabelMsj.show()
        except ValueError:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No hay tareas para completar')
            self.LabelMsj.show()
        except Exception:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()
        self.TituloCompletar.setText("")

    def actualizarTareas(self):
            vencen = vencimientos()
            mensaje = mostrar_vencidas(vencen[0], vencen[1], vencen[2], vencen[3])
            self.text_item.setPlainText(mensaje[0])
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.scroll_text)
            return mensaje[1]


    def scroll_text(self):
        pos_y = self.text_item.pos().y()
        height = self.frame_8.height()
        if pos_y < -height:
            pos_y = self.frame_8.height()
        else:
            pos_y -= 1
        self.text_item.setPos(self.text_item.pos().x(), pos_y)

    def completarT(self):
        text = self.TituloCompletar.text()
        if text:
            self.BotonCompletarT.setEnabled(True)
        else:
            self.BotonCompletarT.setEnabled(False)
    def completas(self):
        result=tareas_completas()
        try:
            self.imprimir_tuplas(result)
        except ValueError:
            self.tableWidgetBuscar.clearContents()
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas completas')
            self.LabelMsj.show()

    def pendientes(self):
        result=tareas_pendientes()
        try:
            self.imprimir_tuplas(result)
        except ValueError:
            self.tableWidgetBuscar.clearContents()
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText("No existen tareas pendientes")
            self.LabelMsj.show()
    def sacarTodo(self):
        self.DescripcionEdit.hide()
        self.TituloEdit_2.hide()
        self.PrioridadEdit.hide()
        self.calendarWidgetEditar.hide()
        self.TimeEditar.hide()

    def habilitarBoton2(self):
        text = self.TituloEdit.text()
        if text:
            self.BotonEditarT.setEnabled(True)
        else:
            self.BotonEditarT.setEnabled(False)

    def mostrarTituloEdit(self):
        self.TituloEdit_2.show()
        self.PrioridadEdit.hide()
        self.DescripcionEdit.hide()
        self.calendarWidgetEditar.hide()
        self.TimeEditar.hide()
        self.BotonEditarT.setEnabled(False)

    def textoEditar(self):
        text = self.TituloEdit.text()
        desc = self.DescripcionEdit.text()
        text1 = self.TituloEdit_2.text()
        if text:
            if text1 or desc:
                self.BotonEditarT.setEnabled(True)
            else:
                self.BotonEditarT.setEnabled(False)
        else:
            self.BotonEditarT.setEnabled(False)


    def EditarTarea(self):
        self.tableWidgetBuscar.clearContents()
        self.BotonEditarT.setEnabled(False)
        try:
            if self.TituloEditar.isChecked():
                opcion = "1"
            elif self.DescripcionEditar.isChecked():
                opcion = "2"
            elif self.VencimientoEditar.isChecked():
                opcion = "3"
            elif self.PrioridadEditar.isChecked():
                opcion = "4"

            variable = self.comprobar(opcion)

            if variable == 1:
                res = todas()
                self.imprimir_tuplas(res)
                self.LabelMsj.setStyleSheet('color:red; border:0px')
                self.LabelMsj.setText('No se puede editar una tarea completa')
                self.LabelMsj.show()
                return
                # La tarea está en estado 'completa'.

            elif variable == 2:
                res = todas()
                self.imprimir_tuplas(res)
                self.LabelMsj.setStyleSheet('color:red; border:0px')
                self.LabelMsj.setText('La tarea no existe')
                self.LabelMsj.show()
                return
                # La tarea no existe.

            if variable != 1 and variable != 2:
                self.tableWidgetBuscar.clearContents()
                self.tableWidgetBuscar.show()
                res=todas()
                self.imprimir_tuplas(res)
                self.LabelMsj.setStyleSheet('color:blue; border:0px')
                self.LabelMsj.setText('La tarea se edito correctamente')
                self.LabelMsj.show()

            # la tarea se edito sin errores.

        except sqlite3.IntegrityError:
            self.tableWidgetBuscar.clearContents()
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('Ya existe una tarea con ese nombre')
            self.LabelMsj.show()
        except ValueError:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas para editar')
            self.LabelMsj.show()
        self.TituloEdit.setText("")
        self.TituloEdit_2.setText("")
        self.DescripcionEdit.setText("")

    def comprobar(self,opcion):
        titulo = self.TituloEdit.text()
        fecha = self.calendarWidgetEditar.selectedDate()
        hym = self.TimeEditar.time()
        comprobar = conexion.execute("SELECT * FROM tareas WHERE titulo=?", (titulo,))
        esto = comprobar.fetchone()
        if esto != None:
            match opcion:
                # opcion para editar el titulo
                case "1":
                    variable = self.TituloEdit_2.text()
                # opcion para editar la descripcion
                case "2":
                    variable = self.DescripcionEdit.text()
                    # opcion para editar la fecha
                case "3":
                    variable = fecha_vencimiento(fecha,hym)
                # opcion para editar la prioridad
                case "4":
                    variable = self.PrioridadEdit.currentText()
            e=editar_tarea(titulo,variable,opcion)
            return e
        else:
            return 2  # aca es donde compruebo si existe la tarea

    def mostrarDescriptEdit(self):
        self.TituloEdit_2.hide()
        self.PrioridadEdit.hide()
        self.DescripcionEdit.show()
        self.calendarWidgetEditar.hide()
        self.TimeEditar.hide()

    def mostrarVenceEdit(self):
        self.TituloEdit_2.hide()
        self.PrioridadEdit.hide()
        self.DescripcionEdit.hide()
        self.calendarWidgetEditar.show()
        self.TimeEditar.show()

    def mostrarPrioridadEdit(self):
        self.TituloEdit_2.hide()
        self.PrioridadEdit.show()
        self.DescripcionEdit.hide()
        self.calendarWidgetEditar.hide()
        self.TimeEditar.hide()

    def ocultar(self):
        self.TituloBuscar.hide()
        self.PrioridadBuscar.hide()
        self.WidgetBuscar.hide()

    def buscarTareas(self):
        self.tableWidgetBuscar.show()
        text = self.TituloBuscar.text()
        priori = self.PrioridadBuscar.currentText()
        fecha = self.WidgetBuscar.selectedDate()
        hym=PyQt5.QtCore.QTime(0, 0)
        try:
            if self.SelectTitulo.isChecked():
                resultado = buscar_tarea(text, "1")
                self.imprimir_tuplas(resultado)
            if self.SelectFechaVencimiento.isChecked():
                convert = fecha_vencimiento(fecha,hym,"2")
                resultado = buscar_tarea(convert,"2")
                self.imprimir_tuplas(resultado)
            if self.SelectPrioridad.isChecked():
                resultado = buscar_tarea(priori, "3")
                self.imprimir_tuplas(resultado)
        except ValueError:
            self.tableWidgetBuscar.clearContents()
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('La/s tarea/s no existe/n')
            self.LabelMsj.show()
        self.TituloBuscar.setText("")

    def cambiarBotonB(self):
        texto = self.TituloBuscar.text()
        if texto:
            self.BotonBuscarT.setEnabled(True)
        else:
            self.BotonBuscarT.setEnabled(False)

    def mostrarTodo(self):
        self.tableWidgetBuscar.clearContents()
        self.tableWidgetBuscar.show()
        resultado = todas()
        try:
            self.imprimir_tuplas(resultado)
        except ValueError:
            self.tableWidgetBuscar.clearContents()
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('No existen tareas')
            self.LabelMsj.show()

    def imprimir_tuplas(self, tupla):
        if tupla:
            self.LabelMsj.hide()
            self.tableWidgetBuscar.clearContents()
            self.tableWidgetBuscar.setColumnCount(5)  # Establecer el número de columnas
            if isinstance(tupla,tuple):
                self.tableWidgetBuscar.setRowCount(1)  # Establecer el número de filas
                datos = tupla  # Obtengo la única fila de la tupla
                for columna, dato in enumerate(datos):
                    item = QTableWidgetItem(str(dato))
                    self.tableWidgetBuscar.setItem(0, columna, item)
            else:
                self.tableWidgetBuscar.setRowCount(len(tupla))
                for fila, datos in enumerate(tupla):
                    for columna, dato in enumerate(datos):
                        item = QTableWidgetItem(str(dato))
                        self.tableWidgetBuscar.setItem(fila, columna, item)
            self.tableWidgetBuscar.show()
        else:
            raise ValueError

    def tituloB(self):
        self.TituloBuscar.show()
        self.PrioridadBuscar.hide()
        self.WidgetBuscar.hide()

    def prioriB(self):
        self.TituloBuscar.hide()
        self.PrioridadBuscar.show()
        self.WidgetBuscar.hide()



    def calendarB(self):
        self.TituloBuscar.hide()
        self.PrioridadBuscar.hide()
        self.WidgetBuscar.show()

    def check_text(self):
        text = self.TituloAgregar.text()
        desc = self.DescripcionAgregar.text()
        textoB = self.TituloBuscar.text()
        textoC = self.TituloCompletar.text()
        textoE = self.TituloEliminar.text()
        if not textoE:
            self.TituloEliminar.setStyleSheet("border:1px solid red")
        else:
            self.TituloEliminar.setStyleSheet("border:1px solid blue")
        if not textoC:
            self.TituloCompletar.setStyleSheet("border:1px solid red")
        else:
            self.TituloCompletar.setStyleSheet("border:1px solid blue")
        if not textoB:
            self.TituloBuscar.setStyleSheet("border:1px solid red")
        else:
            self.TituloBuscar.setStyleSheet("border:1px solid blue")
        if not text:
            self.TituloAgregar.setStyleSheet("border:1px solid red")
            if not desc:
                self.DescripcionAgregar.setStyleSheet("border:1px solid red")
            else:
                self.DescripcionAgregar.setStyleSheet("border:1px solid blue")
        else:
            self.TituloAgregar.setStyleSheet("border:1px solid blue")
            if not desc:
                self.DescripcionAgregar.setStyleSheet("border:1px solid red")
            else:
                self.TituloAgregar.setStyleSheet("border:1px solid blue")
                self.DescripcionAgregar.setStyleSheet("border:1px solid blue")


    def obtener_datos(self):
        fecha = self.calendarWidgetAgregar.selectedDate()
        text = self.TituloAgregar.text()
        desc = self.DescripcionAgregar.text()
        hym = self.HyMedit.time()
        priori = self.PrioridadAgregar.currentText()
        dias = self.DiasExtraAgregar.currentText()
        try:
            fec_venc = fecha_vencimiento(fecha, hym,"1")
            agregar_tarea(text, desc, fec_venc, priori, dias)
            self.LabelMsj.setStyleSheet('color:blue; border:0px')
            self.LabelMsj.setText('Tarea agregada con exito')
            self.LabelMsj.show()
        except sqlite3.IntegrityError:
            self.LabelMsj.setStyleSheet('color:red; border:0px')
            self.LabelMsj.setText('La tarea ya existe')
            self.LabelMsj.show()
        self.TituloAgregar.setText("")
        self.DescripcionAgregar.setText("")

    def cambiarBoton(self):
        text = self.TituloAgregar.text()
        desc = self.DescripcionAgregar.text()
        if text and desc:
            self.BotonAgregarT.setEnabled(True)
        else:
            self.BotonAgregarT.setEnabled(False)

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 10:
            self.showMaximized()
            self.NormalButton.hide()
            self.MaximizeButton.show()
        else:
            self.showNormal()
            self.NormalButton.show()
            self.MaximizeButton.hide()

    def guardar_posicion_clic(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.clickPosition = event.globalPos()
        event.accept()

    def ctrl_minimize(self):
        self.showMinimized()

    def ctrl_normal(self):
        self.showNormal()
        self.NormalButton.show()
        self.MaximizeButton.hide()

    def ctrl_maximize(self):
        self.showMaximized()
        self.NormalButton.hide()
        self.MaximizeButton.show()

    def limite_caja_texto(self):
        self.TituloAgregar.setPlaceholderText("Ingrese un titulo")
        self.TituloAgregar.setMaxLength(20)
        self.DescripcionAgregar.setPlaceholderText("Ingrese una descripcion")
        self.DescripcionAgregar.setMaxLength(40)
        self.TituloCompletar.setPlaceholderText("Ingrese titulo a completar")
        self.TituloCompletar.setMaxLength(20)
        self.TituloEliminar.setPlaceholderText("Ingrese titulo a eliminar")
        self.TituloEliminar.setMaxLength(20)
        self.TituloBuscar.setPlaceholderText("Ingrese titulo a buscar")
        self.TituloBuscar.setMaxLength(20)
        self.TituloEdit.setPlaceholderText("Ingrese titulo a editar")
        self.TituloEdit.setMaxLength(20)
        self.TituloEdit_2.setPlaceholderText("Ingrese un titulo")
        self.TituloEdit_2.setMaxLength(20)
        self.DescripcionEdit.setPlaceholderText("Ingrese una descripcion")
        self.DescripcionEdit.setMaxLength(40)

    def cerrarBd(self):
        conexion.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Gui()
    GUI.show()
    sys.exit(app.exec_())