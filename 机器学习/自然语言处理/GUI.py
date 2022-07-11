import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog

# 显示界面
root = tk.Tk()
# root.geometry("800x600+283+82")
root.title("文本分析系统")
width, height = 800, 800
widths_max, height_max = root.maxsize()
s_center = "%dx%d+%d+%d" % (width, height, (widths_max - width) / 2, (height_max - height) / 2)  # 居中
root.geometry(s_center)
# root.resizable(width=True,height=False) #拉伸
# root.mainloop()
