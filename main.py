import tkinter as tk
import mod_textCompar
import mod_guide
from mod_pasteTool import PasteAssistant


def main():

    root = tk.Tk()
    root.title("粘贴工具_v.2.0.qin")
    root.wm_minsize(400, 500)
    root.geometry("400x500")
    app = PasteAssistant(root)
    mod_textCompar.create_window(app.notebook)
    mod_guide.create_guide_tab(app.notebook)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
