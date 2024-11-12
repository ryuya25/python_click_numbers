##################################
# Click_Numbers_Alternately
#    Click_Numbers から継承
#    数値をクリックするとき右クリック/左クリックを交互にしないといけないように変更
##################################
import click_numbers
from tkinter import messagebox

class Click_Numbers_Alternately(click_numbers.Click_Numbers):
    def __init__(self, col=None, row=None):
        super().__init__(col, row)
        string = '[ここをクリックすると開始します]をクリックして\n'
        string += '1から数字順にクリックしてください\n'
        string += 'ただし、クリックボタンは左右交互にクリックしてください'
        messagebox.showinfo('', string)

    def click_number(self, event):
        #奇数のときは、event.num=1(左クリック)以外は無視
        if self.target_number % 2 == 1:
            if event.num != 1:
                return
        #偶数のときは、event.num=3(右クリック)以外は無視
        if self.target_number % 2 == 0:
            if event.num != 3:
                return
        super().click_number(event)

if __name__ == '__main__':

    d = Click_Numbers_Alternately()
    #d = Click_Numbers_Alternately(5,5)

    d.mainloop()
