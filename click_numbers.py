##################################
# click_numbers
##################################
import tkinter as tk
import random
import time

class Click_Numbers:
    ##################################
    # メンバー変数定義
    ##################################

    # 計測時間表示の更新時間指定(ms)
    INTERVAL_TIME = 33

    # クリック対象の番号 (0の場合は停止中を示します)
    target_number = 0
    # ボタンウィジットを格納するためのリスト
    button_list = []

    start_time = 0

    def __init__(self, col = None, row = None):
        
        # ウィンドウの設定
        self.root = tk.Tk()
        self.root.geometry('800x600')
        
        # 列数/行数の指定
        self.MAX_COL = 3 if col == None else col
        self.MAX_ROW = 3 if row == None else row

        # 番号用のリスト(このリストをシャッフルして使用します)
        self.number_list = list(range(self.MAX_COL * self.MAX_ROW))

        # 画面上部にラベルを配置(開始ボタンと計測表示を行います)
        self.label = tk.Label(self.root, text = '[ここをクリックすると開始します]', font = ('',20))
        self.label.pack()
        self.label.bind('<ButtonPress>', self.click_start)

        # 画面下部にフレームを配置
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill='both')

        #伸縮したときの行と列の割合を指定(すべて1に設定しているので同じ大きさの配置となります)
        for col in range(self.MAX_COL):
            frame.columnconfigure(col, weight=1)
        for row in range(self.MAX_ROW):
            frame.rowconfigure(row, weight=1)

        # フレーム内に指定された行列でボタンを配置
        for col in range(self.MAX_COL):
            for row in range(self.MAX_ROW):
                number = col * self.MAX_ROW + row
                button = tk.Button(frame, text = str(number + 1), font = ("",20), relief='solid')
                button.grid(row = row, column = col, sticky=tk.NSEW)
                button.bind('<Button>', self.click_number)
                self.button_list.append(button)

    def mainloop(self):
        # メインイベントループ開始
        self.root.mainloop()

    ##################################
    # 関数名：click_start
    # 概　要：計測開始ボタンをクリックしたときの処理
    # 引　数：event イベント情報(というのが必要らしい)
    # 戻り値：なし
    # 内　容：対象番号を1にセット
    #         番号をシャッフル
    #         シャッフルした番号をボタンに反映、このとき背景色の初期化も行う
    #         開始時間を保存
    #         計測時間更新(開始直後なので、0秒を表示)
    #         一定時間後、計測更新関数を呼び出すように設定
    ##################################
    def click_start(self, event):
        #処理が遅いPCだと固まる場合があるので1秒以内に再スタートした場合はスキップ
        if 0 < time.time() - self.start_time < 1:
            return

        # クリック対象の番号 (0の場合は停止中を示します)
        self.target_number = 1

        random.shuffle(self.number_list) # 番号用リストをシャッフル
        for i, button in enumerate(self.button_list):
            button.config(bg='SystemButtonFace')
            button.config(text=str(self.number_list[i]+1))
        self.start_time = time.time()
        self.update()
        self.root.after(self.INTERVAL_TIME, self.update)

    ##################################
    # 関数名：update
    # 概　要：計測中の更新処理
    # 引　数：なし
    # 戻り値：なし
    # 詳　細：計測中(target_numberが0以外)の場合以下を実行
    #             経過時間を表示
    #             一定時間経過後に再度この関数を呼び出す設定をする
    ##################################
    def update(self):
        if self.target_number != 0:
            pass_time = time.time() - self.start_time
            self.label.configure(text='{:4.2f}'.format(pass_time))
            self.root.after(self.INTERVAL_TIME, self.update)

    ##################################
    # 関数名：click_number
    # 概　要：数値ボタンをクリックしたときの処理
    # 引　数：event イベント情報(というのが必要らしい)
    # 　　　　button クリックしたボタンウィジット
    # 戻り値：なし
    # 内　容：クリックしたボタンの番号が対象と一致していた場合以下を実行
    # 　　　      ボタンの背景色を薄い赤色に変更
    # 　　　      対象の番号を1進める
    # 　　　      対象の番号がボタン数を超えた場合(最後のボタンをクリックした場合)以下を実行
    # 　　　          計測時間表示(ここで時間が固定される)
    # 　　　          対象番号を0(停止中の扱い)にセット
    # 　　　          計測時間ラベルに再開する方法について追記
    ##################################
    def click_number(self, event):
        if str(self.target_number) == event.widget['text']:
            event.widget.config(bg='#FF8080')
            self.target_number += 1
            if self.target_number > self.MAX_COL * self.MAX_ROW:
                self.update()
                self.target_number = 0
                self.label.config(text=self.label['text']+'[ここをクリックすると再開します]')

##################################
# ここからメイン処理
##################################

if __name__ == '__main__':

    d = Click_Numbers()
    #d = Click_Numbers(5,5)

    d.mainloop()
