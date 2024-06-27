import re
import pyautogui
import jieba
from pypinyin import lazy_pinyin
import tkinter as tk
from tkinter import scrolledtext, font
from pynput import keyboard
import string

class PasteAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("粘贴工具_v.2.0.qin")
        self.custom_font = font.Font(family="等线", size=14)
        self.textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=self.custom_font)
        self.textbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(fill=tk.X, padx=10, pady=5)
        self.display_label = tk.Label(self.top_frame, text="按下 Ctrl+Alt+P 启动粘贴，按下按下 Ctrl+Alt+L 强制停止\n请保证输入法处于英文，且按 shift 可切换中英文", wraplength=800, justify=tk.LEFT, font=self.custom_font)
        self.display_label.pack(side=tk.LEFT)
        self.radio_frame = tk.Frame(self.top_frame)
        self.radio_frame.pack(side=tk.RIGHT)
        self.language_var = tk.StringVar(root)
        self.language_var.set("English")
        self.english_radio = tk.Radiobutton(self.radio_frame, text="英文", variable=self.language_var, value="English", font=self.custom_font)
        self.chinese_radio = tk.Radiobutton(self.radio_frame, text="中文", variable=self.language_var, value="Chinese", font=self.custom_font)
        self.english_radio.grid(row=0, column=0, padx=5, pady=5)
        self.chinese_radio.grid(row=0, column=1, padx=5, pady=5)
        self.listener = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+p': self.queue_display_text,
            '<ctrl>+<alt>+l': self.stop_paste
        })
        self.listener.start()
        self.is_running = False
        self.is_stopping = False
        self.delay_period = 1

    def queue_display_text(self):
        if not self.is_running:
            self.is_running = True
            self.is_stopping = False
            self.root.after(self.delay_period * 1000, self.display_text)

    def display_text(self):
        input_text = self.textbox.get("1.0", tk.END).strip()
        start_paste(input_text, self.language_var.get(), self)
        self.is_running = False

    def stop_paste(self):
        if self.is_running:
            self.is_stopping = True

    def on_closing(self):
        self.listener.stop()
        self.root.destroy()

full_to_half = {'。': '.', '，': ',', '；': ';', '‘': '\'', '’': '\'', '【': '[', '】': ']', '、': '\\'}
down_to_up = {'《': ',', '》': 'right', '？': '/', '：': ';', '“': '\'', '”': '\'', '「': '[', '」': 'right', '、': '|',
              '<': ',', '>': '.', '?': '/', ':': ';', '"': '\'', '{': '[', '}': ']', '\\': '|'}

def start_paste(in_s, mode, app):

    if mode == 'English':

        s = ''
        for c in in_s:
            if c in full_to_half:
                c = full_to_half[c]
            s += c
        words_list = re.split(r'(\s+)', s)
        words = []
        for i in words_list:
            if '\n' not in i:
                words.append(i)
                words.append(' ')
            else:
                line = i.split('\n')
                for l in line:
                    words.append(l)
                    words.append('\n')
            words.pop()
        for word in words:
            if app.is_stopping:
                break
            if word == '\n':
                pyautogui.press('enter')
            elif word == ' ':
                pyautogui.write(' ')
            elif any(char.isupper() for char in word):
                for c in word:
                    if app.is_stopping:
                        break
                    if c in string.ascii_uppercase:
                        pyautogui.keyDown('leftshift')
                        pyautogui.typewrite(c)
                        pyautogui.keyUp('leftshift')
                    else:
                        pyautogui.typewrite(c)
            else:
                pyautogui.write(word)

    elif mode == 'Chinese':

        s = in_s
        put_s = ""
        lis = jieba.lcut(s)
        for i in range(len(lis)):
            new_s = "".join(lazy_pinyin(lis[i]))
            if new_s != lis[i]:
                new_s += "1の"
                put_s += 'の'
            put_s += new_s
        for c in put_s:
            if app.is_stopping:
                break
            if c == '\n':
                pyautogui.press('enter')
            elif c == 'の':
                pyautogui.press('shiftleft')
            elif c in full_to_half:
                pyautogui.press('shiftleft')
                pyautogui.typewrite(full_to_half[c])
                pyautogui.press('shiftleft')
            elif c in down_to_up:
                if c == '》' or c == '」':
                    pyautogui.press(down_to_up[c])
                else:
                    pyautogui.press('shiftleft')
                    pyautogui.hotkey('shiftleft', down_to_up[c])
                    pyautogui.press('shiftleft')
            else:
                pyautogui.write(c)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasteAssistant(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
