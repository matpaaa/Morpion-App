from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivy.core.window import Window
import numpy as np
from random import randint


Window.size = (300,500)

KV = """
MDFloatLayout:
    MDRectangleFlatButton:
        id: button1
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.18,"center_y":.75}
        size_hint: .3,.2
        on_press: app.press1()
    MDRectangleFlatButton:
        id: button2
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.5,"center_y":.75}
        size_hint: .3,.2
        on_press: app.press2()
    MDRectangleFlatButton:
        id: button3
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.82,"center_y":.75}
        size_hint: .3,.2
        on_press: app.press3()
        
    MDRectangleFlatButton:
        id: button4
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.18,"center_y":.54}
        size_hint: .3,.2
        on_press: app.press4()
    MDRectangleFlatButton:
        id: button5
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.5,"center_y":.54}
        size_hint: .3,.2
        on_press: app.press5()
    MDRectangleFlatButton:
        id: button6
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.82,"center_y":.54}
        size_hint: .3,.2
        on_press: app.press6()
        
    MDRectangleFlatButton:
        id: button7
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.18,"center_y":.33}
        size_hint: .3,.2
        on_press: app.press7()
    MDRectangleFlatButton:
        id: button8
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.5,"center_y":.33}
        size_hint: .3,.2
        on_press: app.press8()
    MDRectangleFlatButton:
        id: button9
        text: ""
        bold: True
        font_style: "H3"
        pos_hint: {"center_x":.82,"center_y":.33}
        size_hint: .3,.2
        on_press: app.press9()
        
    MDLabel:
        id: label
        pos_hint: {"center_y":.92}
        halign: "center"
        bold: True
        font_style: "H5"
        text: ""
        
    MDRectangleFlatButton:
        pos_hint: {"center_x":.5,"center_y":.15}
        text: "Reset"
        size_hint: .35,.05
        on_press: app.reset()
"""


class MainApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.matrice = np.array([[0,0,0],[0,0,0],[0,0,0]])


        self.app = Builder.load_string(KV)
        self.screen.add_widget(self.app)

        return self.screen

    def reset(self):
        self.matrice = np.array([[0,0,0],[0,0,0],[0,0,0]])
        self.app.ids.label.text = ""
        self.app.ids.button1.text = ""
        self.app.ids.button2.text = ""
        self.app.ids.button3.text = ""
        self.app.ids.button4.text = ""
        self.app.ids.button5.text = ""
        self.app.ids.button6.text = ""
        self.app.ids.button7.text = ""
        self.app.ids.button8.text = ""
        self.app.ids.button9.text = ""

    def algo0(self,raws,cols):
        self.raws = raws
        self.cols = cols

        for i in range(3):
            if self.matrice[i,0] == 1 and self.matrice[i,1] == 1:
                if self.matrice[i,2] == 1:
                    self.app.ids.label.text = "Le 0 a gagné"
                    return
            if self.matrice[0,i] == 1 and self.matrice[1,i] == 1:
                if self.matrice[2,i] == 1:
                    self.app.ids.label.text = "Le 0 a gagné"
                    return
        if self.matrice[0,0] == 1 and self.matrice[1,1] == 1:
            if self.matrice[2,2] == 1:
                self.app.ids.label.text = "Le 0 a gagné"
                return
        if self.matrice[2,0] == 1 and self.matrice[1,1] == 1:
            if self.matrice[0,2] == 1:
                self.app.ids.label.text = "Le 0 a gagné"
                return

        resultat = self.matrice[0, 0] + self.matrice[0, 1] + self.matrice[0, 2] + self.matrice[1, 0] + self.matrice[
            1, 1] + self.matrice[1, 2] + self.matrice[2, 0] + self.matrice[2, 1] + self.matrice[2, 2]
        if resultat == 13:
            self.app.ids.label.text = "Egalité"
            return

        for i in range(2):
            if self.matrice[i, 0] == 2 and self.matrice[i, 1] == 2:
                if self.matrice[i, 2] == 0:
                    self.matrice[i, 2] = 2
                    if i == 0:
                        self.app.ids.button3.text = "X"
                    if i == 1:
                        self.app.ids.button6.text = "X"
                    if i == 2:
                        self.app.ids.button9.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return
            if self.matrice[i, 2] == 2 and self.matrice[i, 1] == 2:
                if self.matrice[i, 0] == 0:
                    self.matrice[i, 0] = 2
                    if i == 0:
                        self.app.ids.button1.text = "X"
                    if i == 1:
                        self.app.ids.button4.text = "X"
                    if i == 2:
                        self.app.ids.button7.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return

            if self.matrice[i, 0] == 2 and self.matrice[i, 2] == 2:
                if self.matrice[i, 1] == 0:
                    self.matrice[i, 1] = 2
                    if i == 0:
                        self.app.ids.button2.text = "X"
                    if i == 1:
                        self.app.ids.button5.text = "X"
                    if i == 2:
                        self.app.ids.button8.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return

            for i in range(2):
                if self.matrice[0, i] == 2 and self.matrice[1, i] == 2:
                    if self.matrice[2, i] == 0:
                        self.matrice[2, i] = 2
                        if i == 0:
                            self.app.ids.button7.text = "X"
                        if i == 1:
                            self.app.ids.button8.text = "X"
                        if i == 2:
                            self.app.ids.button9.text = "X"
                        self.app.ids.label.text = "Le X a gagné"
                        return
                if self.matrice[2, i] == 2 and self.matrice[1, i] == 2:
                    if self.matrice[0, i] == 0:
                        self.matrice[0, i] = 2
                        if i == 0:
                            self.app.ids.button1.text = "X"
                        if i == 1:
                            self.app.ids.button2.text = "X"
                        if i == 2:
                            self.app.ids.button3.text = "X"
                        self.app.ids.label.text = "Le X a gagné"
                        return
                if self.matrice[0, i] == 2 and self.matrice[2, i] == 2:
                    if self.matrice[1, i] == 0:
                        self.matrice[1, i] = 2
                        if i == 0:
                            self.app.ids.button4.text = "X"
                        if i == 1:
                            self.app.ids.button5.text = "X"
                        if i == 2:
                            self.app.ids.button6.text = "X"
                        self.app.ids.label.text = "Le X a gagné"
                        return

            if self.matrice[0, 0] == 2 and self.matrice[1, 1] == 2:
                if self.matrice[2, 2] == 0:
                    self.matrice[2, 2] = 2
                    self.app.ids.button9.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return
            if self.matrice[0, 0] == 2 and self.matrice[2, 2] == 2:
                if self.matrice[1, 1] == 0:
                    self.matrice[1, 1] = 2
                    self.app.ids.button5.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return
            if self.matrice[1, 1] == 2 and self.matrice[2, 2] == 2:
                if self.matrice[0, 0] == 0:
                    self.matrice[0, 0] = 2
                    self.app.ids.button1.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return

            if self.matrice[2, 0] == 2 and self.matrice[1, 1] == 2:
                if self.matrice[0, 2] == 0:
                    self.matrice[0, 2] = 2
                    self.app.ids.button3.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return
            if self.matrice[2, 0] == 2 and self.matrice[0, 2] == 2:
                if self.matrice[1, 1] == 0:
                    self.matrice[1, 1] = 2
                    self.app.ids.button5.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return
            if self.matrice[1, 1] == 2 and self.matrice[0, 2] == 2:
                if self.matrice[2, 0] == 0:
                    self.matrice[2, 0] = 2
                    self.app.ids.button7.text = "X"
                    self.app.ids.label.text = "Le X a gagné"
                    return
        self.algo1()

    def algo1(self):
        if self.matrice[2,0] == 1 and self.matrice[1,1] == 1:
            if self.matrice[0,2] == 0:
                self.matrice[0,2] = 2
                self.app.ids.button3.text = "X"
                return
        if self.matrice[2,0] == 1 and self.matrice[0,0] == 1:
            if self.matrice[1,1] == 0:
                self.matrice[1,1] = 2
                self.app.ids.button4.text = "X"
                return
        for i in range(2):
            if self.matrice[i,0] == 1 and self.matrice[i,1] == 1:
                if self.matrice[i,2] == 0:
                    self.matrice[i,2] = 2
                    if i == 0:
                        self.app.ids.button3.text = "X"
                    if i == 1:
                        self.app.ids.button6.text = "X"
                    if i == 2:
                        self.app.ids.button9.text = "X"
                    return
            if self.matrice[i,2] == 1 and self.matrice[i,1] == 1:
                if self.matrice[i,0] == 0:
                    self.matrice[i,0] = 2
                    if i == 0:
                        self.app.ids.button1.text = "X"
                    if i == 1:
                        self.app.ids.button4.text = "X"
                    if i == 2:
                        self.app.ids.button7.text = "X"
                    return

            if self.matrice[i,0] == 1 and self.matrice[i,2] == 1:
                if self.matrice[i,1] == 0:
                    self.matrice[i,1] = 2
                    if i == 0:
                        self.app.ids.button2.text = "X"
                    if i == 1:
                        self.app.ids.button5.text = "X"
                    if i == 2:
                        self.app.ids.button8.text = "X"
                    return
            if self.matrice[2,0] == 1 and self.matrice[2,2]:
                if self.matrice[2,1] == 0:
                    self.matrice[2,1] = 2
                    self.app.ids.button8.text = "X"
                    return
            if self.matrice[0,2] == 1 and self.matrice[2,2]:
                if self.matrice[1,2] == 0:
                    self.matrice[1,2] = 2
                    self.app.ids.button6.text = "X"
                    return

        for i in range(2):
            if self.matrice[0,i] == 1 and self.matrice[1,i] == 1:
                if self.matrice[2,i] == 0:
                    self.matrice[2,i] = 2
                    if i == 0:
                        self.app.ids.button7.text = "X"
                    if i == 1:
                        self.app.ids.button8.text = "X"
                    if i == 2:
                        self.app.ids.button9.text = "X"
                    return
            if self.matrice[2,i] == 1 and self.matrice[1,i] == 1:
                if self.matrice[0,i] == 0:
                    self.matrice[0,i] = 2
                    if i == 0:
                        self.app.ids.button1.text = "X"
                    if i == 1:
                        self.app.ids.button2.text = "X"
                    if i == 2:
                        self.app.ids.button3.text = "X"
                    return
            if self.matrice[0,i] == 1 and self.matrice[2,i] == 1:
                if self.matrice[1,i] == 0:
                    self.matrice[1,i] = 2
                    if i == 0:
                        self.app.ids.button4.text = "X"
                    if i == 1:
                        self.app.ids.button5.text = "X"
                    if i == 2:
                        self.app.ids.button6.text = "X"
                    return

        if self.matrice[0,0] == 1 and self.matrice[1,1] == 1:
            if self.matrice[2,2] == 0:
                self.matrice[2,2] = 2
                self.app.ids.button9.text = "X"
                return
        if self.matrice[0,0] == 1 and self.matrice[2,2] == 1:
            if self.matrice[1,1] == 0:
                self.matrice[1,1] = 2
                self.app.ids.button5.text = "X"
                return
        if self.matrice[1,1] == 1 and self.matrice[2,2] == 1:
            if self.matrice[0,0] == 0:
                self.matrice[0,0] = 2
                self.app.ids.button1.text = "X"
                return

        if self.matrice[2,0] == 1 and self.matrice[1,1] == 1:
            if self.matrice[0,2] == 0:
                self.matrice[0,2] = 2
                self.app.ids.button3.text = "X"
                return
        if self.matrice[2,0] == 1 and self.matrice[0,2] == 1:
            if self.matrice[1,1] == 0:
                self.matrice[1,1] = 2
                self.app.ids.button5.text = "X"
                return
        if self.matrice[1,1] == 1 and self.matrice[0,2] == 1:
            if self.matrice[2,0] == 0:
                self.matrice[2,0] = 2
                self.app.ids.button7.text = "X"
                return
        self.algo2()

    def algo2(self):
        for i in [0,2]:
            if self.matrice[i,i] == 1:
                if self.matrice[1,1] == 0:
                    self.matrice[1, 1] = 2
                    self.app.ids.button5.text = "X"
                    return
        if self.matrice[2,0] == 1 or self.matrice[0,2] == 1:
            if self.matrice[1,1] == 0:
                self.matrice[1,1] = 2
                self.app.ids.button5.text = "X"
                return
        if self.matrice[1,1] == 1:
            x = randint(0,5)
            if x == 0:
                self.matrice[2,2] = 2
                self.app.ids.button9.text = "X"
                return
            if x == 1:
                self.matrice[0,2] = 2
                self.app.ids.button3.text = "X"
                return
            if x == 2:
                self.matrice[2,0] = 2
                self.app.ids.button7.text = "X"
                return
            if x == 3:
                self.matrice[0,0] = 2
                self.app.ids.button1.text = "X"
                return

        while True:
            y = randint(0,4)
            if y == 0:
                if self.raws-1 >= 0:
                    if self.matrice[self.raws-1,self.cols] == 0:
                        self.matrice[self.raws-1,self.cols] = 2
                        self.algo2_suite(self.raws-1,self.cols)
                        break
            if y == 1:
                if self.raws+1 <= 2:
                    if self.matrice[self.raws+1,self.cols] == 0:
                        self.matrice[self.raws+1,self.cols] = 2
                        self.algo2_suite(self.raws+1,self.cols)
                        break
            if y == 2:
                if self.cols-1 >= 0:
                    if self.matrice[self.raws,self.cols-1] == 0:
                        self.matrice[self.raws,self.cols-1] = 2
                        self.algo2_suite(self.raws,self.cols-1)
                        break
            if y == 3:
                if self.cols+1 <= 2:
                    if self.matrice[self.raws,self.cols+1] == 0:
                        self.matrice[self.raws,self.cols+1] = 2
                        self.algo2_suite(self.raws,self.cols+1)
                        break
        return
    def algo2_suite(self,raws,cols):
        self.raws = raws
        self.cols = cols
        if self.raws == 0 and self.cols == 0:
            self.app.ids.button1.text = "X"
        if self.raws == 0 and self.cols == 1:
            self.app.ids.button2.text = "X"
        if self.raws == 0 and self.cols == 2:
            self.app.ids.button3.text = "X"
        if self.raws == 1 and self.cols == 0:
            self.app.ids.button4.text = "X"
        if self.raws == 1 and self.cols == 1:
            self.app.ids.button5.text = "X"
        if self.raws == 1 and self.cols == 2:
            self.app.ids.button6.text = "X"
        if self.raws == 2 and self.cols == 0:
            self.app.ids.button7.text = "X"
        if self.raws == 2 and self.cols == 1:
            self.app.ids.button8.text = "X"
        if self.raws == 2 and self.cols == 2:
            self.app.ids.button9.text = "X"

    def press1(self):
        if self.matrice[0,0] == 0:
            self.matrice[0,0] = 1
            self.app.ids.button1.text = "O"
            self.algo0(0,0)
    def press2(self):
        if self.matrice[0,1] == 0:
            self.matrice[0,1] = 1
            self.app.ids.button2.text = "O"
            self.algo0(0,1)
    def press3(self):
        if self.matrice[0,2] == 0:
            self.matrice[0,2] = 1
            self.app.ids.button3.text = "O"
            self.algo0(0,2)
    def press4(self):
        if self.matrice[1,0] == 0:
            self.matrice[1,0] = 1
            self.app.ids.button4.text = "O"
            self.algo0(1,0)
    def press5(self):
        if self.matrice[1,1] == 0:
            self.matrice[1,1] = 1
            self.app.ids.button5.text = "O"
            self.algo0(1,1)
    def press6(self):
        if self.matrice[1,2] == 0:
            self.matrice[1,2] = 1
            self.app.ids.button6.text = "O"
            self.algo0(1,2)
    def press7(self):
        if self.matrice[2,0] == 0:
            self.matrice[2,0] = 1
            self.app.ids.button7.text = "O"
            self.algo0(2,0)
    def press8(self):
        if self.matrice[2,1] == 0:
            self.matrice[2,1] = 1
            self.app.ids.button8.text = "O"
            self.algo0(2,1)
    def press9(self):
        if self.matrice[2,2] == 0:
            self.matrice[2,2] = 1
            self.app.ids.button9.text = "O"
            self.algo0(2,2)


MainApp().run()