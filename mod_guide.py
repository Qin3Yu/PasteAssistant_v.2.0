import tkinter as tk
from tkinter import ttk


guide_text = '''
 软件说明：

     本程序提供一个模拟键盘输入的粘贴方案，用于解决带有
 禁止粘贴检测的网站（如学习通等）的粘贴操作。
     本程序仅供学习和交流使用，禁止实际投入场景使用或用
 于违法用途。最终解释权归 QinT6o 所有。
    

 输入方法：

     1.将文本复制进标签页“粘贴工具”下的文本框中。
     2.在右下角选择中或英文输入模式。
     3.按下快捷键后等待输入完成即可。
     4.在输入过程中，可以按下快捷键强制程序停止运行。
    

 注意事项：

     1.程序不会因为焦点丢失而暂停运行。
     2.输入前请确保输入法处于英文输入状态。
     3.中文模式下，请确保按下 shift 后可以切换中英文。
     4.中文模式输入因输入法差别可能有误，请自行检查。
    
    
     程序还提供简单的文本校对功能，用于比对中文模式下输
 入的内容差别，便于用户做出修改，在标签页“文本校对”下
 将程序输入后的文本粘贴到右侧文本框，点击“比较”，差别
 内容将会特殊显示。
 
 
 
                               -- by GitHub.QinT6o
                            PasteAssistant_v.2.0
'''


def create_guide_tab(notebook):
    guide_frame = ttk.Frame(notebook)
    text_box = tk.Text(guide_frame, wrap='word', height=10, width=50)
    text_box.insert('1.0', guide_text)
    text_box.config(state='disabled')
    text_box.pack(expand=True, fill='both')
    notebook.add(guide_frame, text="使用说明")
    return guide_frame
