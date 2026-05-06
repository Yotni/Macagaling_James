import tkinter as tk

def Title_box(parent, text):
    box = tk.Frame(parent, bg="#8A2BE2", padx=30, pady=15)
    box.pack(pady=20)

    tk.Label(
        box,
        text = text,
        font=("Courier", 15, "bold"),
        bg="#8A2BE2",
        fg="white"
    ).pack()

    return box

def Personal_Right_Box_Add_Del(parent):
    right_panel = tk.Frame(parent, bg="#8A2BE2")
    right_panel.place(relx=0.635, rely=0.12, relwidth=0.35, relheight=0.1)

    return right_panel

def Containter_Left_Box_Scroll(parent):
    box = tk.Frame(parent, bg="#8A2BE2")
    box.place(relx=0.02, rely=0.12, relwidth=0.6, relheight=0.87)

    # Title box
    tk.Label(
        box,
        text="Your List of Stories:",
        bg="#8A2BE2",
        fg="white",
        font=("Courier", 14, "bold")
    ).pack(anchor="center", padx=10, pady=10)

    # canva scroll area
    canvas = tk.Canvas(box, bg="#8A2BE2", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True, anchor="n")

    # scrollbar
    scrollbar = tk.Scrollbar(box, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Content box or the inner frame
    list_frame = tk.Frame(canvas, bg="#8A2BE2")

    # Put frame inside canvas
    window_id = canvas.create_window((0, 0), window=list_frame, anchor="nw")

    # Update scroll region properly
    def update_scroll(event=None):
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    list_frame.bind("<Configure>", update_scroll)

    # Make frame match canvas width
    def resize_frame(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", resize_frame)

    return list_frame

def Containter_Center_Box_Scroll(parent):
    box = tk.Frame(parent, bg="#8A2BE2")
    box.place(relx=0.02, rely=0.12, relwidth=0.95, relheight=0.87)

    # Title box
    tk.Label(
        box,
        text="Public Section Stories:",
        bg="#8A2BE2",
        fg="white",
        font=("Courier", 14, "bold")
    ).pack(anchor="center", padx=10, pady=10)

    # canva scroll area
    canvas = tk.Canvas(box, bg="#8A2BE2", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True, anchor="n")

    # scrollbar
    scrollbar = tk.Scrollbar(box, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Content box or the inner frame
    list_frame = tk.Frame(canvas, bg="#8A2BE2")

    # Put frame inside canvas
    window_id = canvas.create_window((0, 0), window=list_frame, anchor="nw")

    # Update scroll region properly
    def update_scroll(event=None):
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    list_frame.bind("<Configure>", update_scroll)

    # Make frame match canvas width
    def resize_frame(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", resize_frame)

    return list_frame


def Intro_box(parent, text, font):
    box = tk.Frame(parent, bg="#8A2BE2", padx=30, pady=20)
    box.pack(anchor= "center", fill="y", pady=30, padx=20, ipadx=20)

    tk.Label(
        box,
        text = text,
        font= font,
        bg="#8A2BE2",
        fg="white"
    ).pack()

    return box