from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt




class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton('Rysuj i pokaż współrzędne punktu P', self)
        self.button2 = QPushButton('Wyczyść pola', self)
        self.button3 = QPushButton('Zapisz współrzędne', self)
        self.clrChoose=QPushButton('Wybierz Kolor', self)
        self.xlabel = QLabel("X", self)
        self.xEdit = QLineEdit()
        self.ylabel = QLabel("Y", self)
        self.yEdit = QLineEdit()
        self.x2label = QLabel("X2", self)
        self.x2Edit = QLineEdit()
        self.y2label = QLabel("Y2", self)
        self.y2Edit = QLineEdit()
        self.x3label = QLabel("X3", self)
        self.x3Edit = QLineEdit()
        self.y3label = QLabel("Y3", self)
        self.y3Edit = QLineEdit()
        self.x4label = QLabel("X4", self)
        self.x4Edit = QLineEdit()
        self.y4label = QLabel("Y4", self)
        self.y4Edit = QLineEdit()
        self.Xplabel0 = QLabel("Xp", self)
        self.Xplabel = QLabel()
        self.Yplabel0 = QLabel("Yp", self)
        self.Yplabel = QLabel()
        self.ostatnilabel = QLabel() 
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        
        
        # ladne ustawienie i wysrodkowanie
        layout =  QGridLayout(self)
        
        layout.addWidget(self.xlabel, 1, 0)
        layout.addWidget(self.xEdit, 1, 1)
        layout.addWidget(self.ylabel, 2, 0)
        layout.addWidget(self.yEdit, 2, 1)
        layout.addWidget(self.x2label, 1, 2)
        layout.addWidget(self.x2Edit, 1, 3)
        layout.addWidget(self.y2label, 2, 2)
        layout.addWidget(self.y2Edit, 2, 3)
        layout.addWidget(self.x3label, 1, 4)
        layout.addWidget(self.x3Edit, 1, 5)
        layout.addWidget(self.y3label, 2, 4)
        layout.addWidget(self.y3Edit, 2, 5)
        layout.addWidget(self.x4label, 1, 6)
        layout.addWidget(self.x4Edit, 1, 7)
        layout.addWidget(self.y4label, 2, 6)
        layout.addWidget(self.y4Edit, 2, 7)
        
     
		
        layout.addWidget(self.button, 3, 1, 1, -1)
        layout.addWidget(self.canvas, 4, 1, 1, -1)
        layout.addWidget(self.clrChoose, 5, 1, 1, -1)
        layout.addWidget(self.button3, 6, 4, 1, -1)
        layout.addWidget(self.Xplabel0, 7, 0)
        layout.addWidget(self.Xplabel, 7, 1)
        layout.addWidget(self.Yplabel0, 7, 2)
        layout.addWidget(self.Yplabel, 7, 3)
        layout.addWidget(self.button2, 7, 4, 1, -1)
        layout.addWidget(self.ostatnilabel, 8, 1, 1, -1)
        
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        #self.button2.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        #połączenie czyszczenia danych
        self.button2.clicked.connect(self.czyszczonko)
        #połączenie zapisu 
        self.button3.clicked.connect(self.zapis)
        
    def checkValues(self, lineE):
        if lineE.text().lstrip('-').replace('.','').isdigit():
            return float(lineE.text())
        else:
            return None
     
    def czyszczonko(self):    #czyszczenie okienek
        self.xEdit.clear()
        self.yEdit.clear()
        self.x2Edit.clear()
        self.y2Edit.clear()
        self.x3Edit.clear()
        self.y3Edit.clear()
        self.x4Edit.clear()
        self.y4Edit.clear()
        self.Xplabel.clear()
        self.Yplabel.clear()
        self.ostatnilabel.clear()
        
         
        
    
        
    def rysuj(self, clr='r'):
        x = self.checkValues(self.xEdit)
        y = self.checkValues(self.yEdit)
        x2 = self.checkValues(self.x2Edit)
        y2 = self.checkValues(self.y2Edit)
        x3 = self.checkValues(self.x3Edit)
        y3 = self.checkValues(self.y3Edit)
        x4 = self.checkValues(self.x4Edit)
        y4 = self.checkValues(self.y4Edit)
        dab= x2-x  
        dac= x3-x 
        dcd= x4-x3 
        Dac= y3-y
        Dab= y2-y 
        Dcd= y4-y3        
        z = dab*Dcd-Dab*dcd
        if z!= 0:
            t1 = (dac*Dcd-Dac*dcd)/z
            t2 = (dac*Dab-Dac*dab)/z
            if t1>=0 and t1<=1 and t2>=0 and t2<=1:
                xp = x + t1*dab
                yp = y + t1*Dab
                a = "{0:.3f}".format(xp)
                b = "{0:.3f}".format(yp)
                self.Xplabel.setText(str(a))
                self.Yplabel.setText(str(b))
                self.ostatnilabel.setText(str("Punkt P znajduje się na przecięciu odcinków")) 
            elif 0 <= t1 <=1:
                xp = x + t1*dab
                yp = y + t1*Dab
                a = "{0:.3f}".format(xp)
                b = "{0:.3f}".format(yp)
                self.Xplabel.setText(str(a))
                self.Yplabel.setText(str(b))
                self.ostatnilabel.setText(str("Punkt P znajduje się na przedłużeniu drugiego odcinka"))
                
            elif 0 <= t2 <=1:
                xp = x + t1*dab
                yp = y + t1*Dab
                a = "{0:.3f}".format(xp)
                b = "{0:.3f}".format(yp)
                self.Xplabel.setText(str(a))
                self.Yplabel.setText(str(b))
                self.ostatnilabel.setText(str("Punkt P znajduje się na przedłużeniu pierwszego odcinka"))
            
            else:
                xp = x + t1*dab
                yp = y + t1*Dab
                a = "{0:.3f}".format(xp)
                b = "{0:.3f}".format(yp)
                self.Xplabel.setText(str(a))
                self.Yplabel.setText(str(b))
                self.ostatnilabel.setText(str("Punkt P znajduje się na przedłużeniu obu odcinków"))
        elif z==0:
                self.ostatnilabel.setText(str("Odcinki są równoległe - brak punktu P")) 
              
                
       
        
        #rysowanie wykresu
        if x !=None and y != None:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, 'o', color='black') #rysowanie punktów
            ax.plot(x2, y2, 'o', color='black')
            ax.plot(x3, y3, 'o', color='black')
            ax.plot(x4, y4, 'o', color='black')
            ax.plot((x,x2), (y,y2), color='green')  #rysowanie linii
            ax.plot((x3,x4), (y3,y4), color='blue')
            if z==0: 
                ax.text(x, y, " Punkt 1 [" + str(x) + ", " + str(y) + "]", fontsize = 10, color = "black")   #przypisanie odpowiednich etykiet to punktów na wykresie
                ax.text(x2, y2, " Punkt 2 [" + str(x2) + ", " + str(y2) + "]" , fontsize = 10, color = "black")
                ax.text(x3, y3, " Punkt 3 [" + str(x3) + ", " + str(y3) + "]" , fontsize = 10, color = "black")
                ax.text(x4, y4, " Punkt 4 [" + str(x4) + ", " + str(y4) + "]" , fontsize = 10, color = "black")
            else:
                ax.plot(xp, yp, 'o', color=clr)
                #ax.plot(xp, yp, 'o', color=clr)
                ax.plot((x,xp), (y,yp), linestyle='--', dashes=(1,5), color='grey')       #łączenie z punktem przecięcia na przedłużeniach
                ax.plot((x2,xp), (y2,yp), linestyle='--', dashes=(1,5), color='grey')
                ax.plot((x3,xp), (y3,yp), linestyle='--', dashes=(1,5), color='grey')
                ax.plot((x4,xp), (y4,yp), linestyle='--', dashes=(1,5), color='grey')
                ax.text(x, y, " Punkt X Y [" + str(x) + ", " + str(y) + "]", fontsize = 10, color = "black")   #przypisanie odpowiednich etykiet to punktów na wykresie
                ax.text(x2, y2, " Punkt X2 Y2 [" + str(x2) + ", " + str(y2) + "]" , fontsize = 10, color = "black")
                ax.text(x3, y3, " Punkt X3 Y3 [" + str(x3) + ", " + str(y3) + "]" , fontsize = 10, color = "black")
                ax.text(x4, y4, " Punkt X4 Y4 [" + str(x4) + ", " + str(y4) + "]" , fontsize = 10, color = "black")
                ax.text(xp, yp, " Punkt XP YP [" + str(a) + ", " + str(b) + "]" , fontsize = 10, color = "red")
        
        
        
            
            self.canvas.draw()
            if z==0:                        #wyswietlenie współrzędnych punktu P na konsoli
                Xp = (str('NIE ISTNIEJE'))
                Yp = (str('NIE ISTNIEJE'))
            else:
                Xp = "{0:.3f}".format(xp)
                Yp = "{0:.3f}".format(yp)
                    
                
        
            self.Xplabel.setText(str(Xp))
            self.Yplabel.setText(str(Yp))
            
        else: 
            msg_err = QMessageBox() 
            msg_err.setWindowTitle("Komunikat") 
            msg_err.setStandardButtons(QMessageBox.Ok) 
            msg_err.setText("Podane współrzędne są niepotrzebne")
            msg_err.exec_()
            self.figure.clear() 
            self.canvas.draw()
    
    
    def zapis(self): 
        self.f=open('proj1.txt' ,'w') 
        self.f.write(45*'-'+'\n')
        self.f.write('|{:^10}|{:^10}|{:^10}|{:^11}|'.format('X','Y','X2','Y2')+'\n')
        self.f.write("\n| {:6.3f}   | {:6.3f}   | {:6.3f}   | {:6.3f}    |".format(self.checkValues(self.xEdit), self.checkValues(self.yEdit), self.checkValues(self.x2Edit), self.checkValues(self.y2Edit),)+'\n')
        self.f.write(45*'-'+'\n')   
        self.f.write('|{:^10}|{:^10}|{:^10}|{:^11}|'.format('X3','Y3','X4','Y4')+'\n')
        self.f.write("\n| {:6.3f}   | {:6.3f}   | {:6.3f}   | {:6.3f}    |".format(self.checkValues(self.x3Edit), self.checkValues(self.y3Edit), self.checkValues(self.x4Edit), self.checkValues(self.y4Edit),)+'\n')
        self.f.write(23*'-'+'\n')
        self.f.write('|{:^10}|{:^10}|'.format('Xp','Yp')+'\n')
        self.f.write("\n| {:6.3f}   | {:6.3f}   |".format(self.checkValues(self.Xplabel), self.checkValues(self.Yplabel),)+'\n')
        self.f.close()   
        
    def handleButton(self):
        self.rysuj()
        
    
    
         

    def clrChooseF(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.rysuj(color.name())
        else:
            pass
if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    window = Window()
    window.show()
    sys.exit(app.exec_())