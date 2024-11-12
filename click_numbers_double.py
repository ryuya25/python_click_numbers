##################################
# Click_Numbers_Double
#    Click_Numbers から継承
#    クリックをダブルクリックに変更
##################################
import click_numbers
from tkinter import messagebox

class Click_Numbers_Double(click_numbers.Click_Numbers):
    
    def __init__(self, col=None, row=None):
        super().__init__(col, row)
        for i, button in enumerate(self.button_list):
            button.unbind('<Button>')
            button.bind('<Double-Button>', self.click_number)
        string = '[ここをクリックすると開始します]をクリックして\n'
        string += '1から数字順にダブルクリックしてください'
        messagebox.showinfo('', string)

if __name__ == '__main__':

    d = Click_Numbers_Double()
    #d = Click_Numbers_Double(5,5)

    d.mainloop()
