from typing import Callable, Tuple

from emotions import Emotion, Emotions
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def create_gui(on_submit: Callable[[str],Tuple[str, Emotion]]):
    def submit():
        input_text = input_box.get(0.,tk.END)
        text, emotion = on_submit(input_text)

        img = Image.open(emotion.img_path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk
        input_label.config(text=text)

    # メインウィンドウを作成
    root = tk.Tk()
    root.title("日本語")

    # 入力テキストを表示するラベルを作成
    input_label = tk.Label(root, text="", wraplength=250)
    input_label.pack()

    # 画像を表示するラベルを作成
    img = Image.open(Emotions.default.img_path)
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img_tk)
    label.image = img_tk
    label.pack(pady=20)

    # 入力ボックスを作成
    # input_box = tk.Entry(root, width=20)
    input_box = tk.Text(root, height=5, width=40)
    input_box.pack()

    # 送信ボタンを作成
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=10)

    # GUIループを開始
    root.mainloop()

def main():
    def sample():
        return "ok"
    create_gui(sample)

if __name__ == "__main__":
    main()