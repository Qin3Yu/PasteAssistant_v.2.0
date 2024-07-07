import tkinter as tk


def highlight_differences():
    text1_content = text1.get("1.0", tk.END).strip()
    text2_content = text2.get("1.0", tk.END).strip()
    text1.tag_remove("red", "1.0", tk.END)
    text1.tag_remove("blue", "1.0", tk.END)
    text2.tag_remove("red", "1.0", tk.END)
    text2.tag_remove("blue", "1.0", tk.END)
    lines1 = text1_content.splitlines()
    lines2 = text2_content.splitlines()
    max_lines = max(len(lines1), len(lines2))
    while len(lines1) > len(lines2):
        lines2.append("")
    while len(lines2) > len(lines1):
        lines1.append("")
    for i in range(max_lines):
        line1 = lines1[i]
        line2 = lines2[i]
        max_len = max(len(line1), len(line2))
        for j in range(max_len):
            char1 = line1[j] if j < len(line1) else ""
            char2 = line2[j] if j < len(line2) else ""
            start_index = f"{i + 1}.{j}"
            end_index = f"{i + 1}.{j + 1}"
            if char1 != char2:
                if not char1:
                    text2.tag_add("blue", start_index, end_index)
                elif not char2:
                    text1.tag_add("blue", start_index, end_index)
                else:
                    text2.tag_add("red", start_index, end_index)
    text2.tag_config("red", background="#FF8E8E")
    text2.tag_config("blue", background="#8E92FF")


def create_window(notebook):
    global text1, text2
    compare_frame = tk.Frame(notebook)
    notebook.add(compare_frame, text='文本校对')

    compare_frame.grid_rowconfigure(0, weight=1)
    compare_frame.grid_columnconfigure(0, weight=1)
    compare_frame.grid_columnconfigure(1, weight=1)

    text1 = tk.Text(compare_frame, width=50, height=20, wrap=tk.WORD)
    text1.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
    text2 = tk.Text(compare_frame, width=50, height=20, wrap=tk.WORD)
    text2.grid(row=0, column=1, padx=5, pady=5, sticky = (tk.W, tk.E, tk.N, tk.S))

    compare_button = tk.Button(compare_frame, text="比较", command=highlight_differences)
    compare_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Adding scrollbar to text1
    scroll1 = tk.Scrollbar(compare_frame, command=text1.yview)
    scroll1.grid(row=0, column=0, sticky='nse')
    text1.config(yscrollcommand=scroll1.set)

    # Adding scrollbar to text2
    scroll2 = tk.Scrollbar(compare_frame, command=text2.yview)
    scroll2.grid(row=0, column=1, sticky='nse')
    text2.config(yscrollcommand=scroll2.set)


def set_text(input_text):
    text1.delete('1.0', tk.END)
    text1.insert('1.0', input_text)
