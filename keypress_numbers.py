##################################
# KeyPress_Numbers
#    Click_Numbers から継承
#    数字順にカーソル位置を移動させる必要はあるけど、
#    クリックではなく(1の位の)数値キーを押すように変更
##################################
import click_numbers
from tkinter import messagebox

class KeyPress_Numbers(click_numbers.Click_Numbers):
    focus_botton = None
    def __init__(self, col=None, row=None):
        super().__init__(col, row)
        self.root.bind('<KeyPress>', self.key_press)
        for i, button in enumerate(self.button_list):
            button.unbind('<Button>')
            button.bind('<Enter>', self.enter)
        self.root.after(100, self.messagebox)

    def messagebox(self):
        string = '[ここをクリックすると開始します]をクリックして\n'
        string += '1から数字順にマウスカーソルを移動させ\n'
        string += 'その数字の1の位の数値キーを押してください'
        messagebox.showinfo('KeyPress_Numbers', string)

    def enter(self, event):
        self.focus_botton = event.widget

    def key_press(self, event):
        if str(self.target_number % 10) == event.keysym:
            if str(self.target_number) == self.focus_botton['text']:
                self.focus_botton.config(bg='#FF8080')
                self.target_number += 1
                if self.target_number > self.MAX_COL * self.MAX_ROW:
                    self.update()
                    self.target_number = 0
                    self.label.config(text=self.label['text']+'[ここをクリックすると再開します]')

if __name__ == '__main__':

    #d = KeyPress_Numbers()
    d = KeyPress_Numbers(5,5)

    d.mainloop()
