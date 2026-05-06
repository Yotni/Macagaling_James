# Imports:
import tkinter as tk
from tkinter import ttk
from UI_Components import Intro_box, Title_box, Containter_Left_Box_Scroll,Personal_Right_Box_Add_Del, Containter_Center_Box_Scroll
from Story_adding_UI import Add_Popup_Container, Adding_Story_Box
from Story_Deleting_UI import Del_Popup_Container, deleting_Story_Box
from Story_Sharing_UI import Share_Popup_Container, Share_Story_Box


from Dictionary_of_Stories import Personal_load_data, Public_load_data

# this variable names is jsut for readabiliy for bolding a word:
BOLD_2x = '\033[2m'
BOLD = '\033[1m'
END = '\033[0m'

#Global but remember to also put it inside of a function as it may use the very first memory data or something:

def Sharing():
    pass

def view_Personal_Section(parent, Library):
    Library = Library()
    # clear old UI
    for widget in parent.winfo_children():
        widget.destroy()

    container = tk.Frame(parent, bg="#8A2BE2")
    container.pack(fill="both", expand=True)

    for key, Story in Library.items():
        Titles = Story["Title"]
        Graphic_Novel = Story["Type of MMM"]
        Story_Statuses = Story["Story Status"]
        Genre = Story["Genres"]
        Rev_Rec = Story["Review and recommendation"]

        # Story Box
        story_box = tk.Frame(container, bg="#8A2BE2", highlightbackground="white", highlightthickness=1
        )
        story_box.pack(fill="x", padx=30, pady=5)

        # Title Key
        tk.Label(
            story_box,
            text=f"{key}",
            fg="#ffffff",
            bg="#8A2BE2",
            font=("Courier", 15, "bold"),
            anchor="center"
        ).pack(fill="x", padx=10, pady=5)

        #Line Box for the Info

        def line(label_text, value_text):
            row = tk.Frame(
                story_box,
                bg="#8A2BE2"
            )
            row.pack(fill="x", padx=15, pady=5)

            # Labels box for title, type....
            left = tk.Frame(
                row,
                bg="#B57CFF",
                highlightbackground="white",
                highlightthickness=1
            )
            left.pack(side="left", padx=20)

            tk.Label(
                left,
                text=label_text,
                bg="#B57CFF",
                fg="black",
                width=12,
                anchor="w"
            ).pack(padx=20, pady=10)

            # Right box for the values
            right = tk.Frame(row, bg="#D6B3FF", highlightbackground="white", highlightthickness=1)
            right.pack(side="left", fill="both", expand=True)

            tk.Label(
                right,
                text=value_text,
                bg="#D6B3FF",
                fg="black",
                anchor="center",
                justify="left",
                wraplength=500,
                font=("Arial", 12)
            ).pack(fill="both", padx=8, pady=6)
        
        line("Title", Titles)
        line("Type", Graphic_Novel)
        line("Status", Story_Statuses)
        line("Genres", " | ".join(Genre))
        if isinstance(Rev_Rec, list):
            review_text = "\n\n".join(f"- {r}" for r in Rev_Rec)
        else:
            review_text = str(Rev_Rec)

        line("Review", review_text)

def view_Public_Section(parent, Library):
    Library = Library()
    # clear old UI
    for widget in parent.winfo_children():
        widget.destroy()

    container = tk.Frame(parent, bg="#8A2BE2")
    container.pack(fill="both", expand=True)

    for key, Story in Library.items():
        Titles = Story["Title"]
        Graphic_Novel = Story["Type of MMM"]
        Story_Statuses = Story["Story Status"]
        Genre = Story["Genres"]
        Rev_Rec = Story["Review and recommendation"]

        # Story Box
        story_box = tk.Frame(container, bg="#8A2BE2", highlightbackground="white", highlightthickness=1
        )
        story_box.pack(fill="x", padx=30, pady=5)

        # Title Key
        tk.Label(
            story_box,
            text=f"{key}",
            fg="#ffffff",
            bg="#8A2BE2",
            font=("Courier", 15, "bold"),
            anchor="center"
        ).pack(fill="x", padx=10, pady=5)

        #Line Box for the Info

        def line(label_text, value_text):
            row = tk.Frame(
                story_box,
                bg="#8A2BE2"
            )
            row.pack(fill="x", padx=15, pady=5)

            # Labels box for title, type....
            left = tk.Frame(
                row,
                bg="#B57CFF",
                highlightbackground="white",
                highlightthickness=1
            )
            left.pack(side="left", padx=20)

            tk.Label(
                left,
                text=label_text,
                bg="#B57CFF",
                fg="black",
                width=12,
                anchor="w"
            ).pack(padx=20, pady=10)

            # Right box for the values
            right = tk.Frame(row, bg="#D6B3FF", highlightbackground="white", highlightthickness=1)
            right.pack(side="left", fill="both", expand=True)

            tk.Label(
                right,
                text=value_text,
                bg="#D6B3FF",
                fg="black",
                anchor="w",
                justify="left",
                wraplength=500,
                font=("Arial", 12)
            ).pack(fill="both", padx=8, pady=6)
        
        line("Title", Titles)
        line("Type", Graphic_Novel)
        line("Status", Story_Statuses)
        line("Genres", " | ".join(Genre))
        if isinstance(Rev_Rec, list):
            review_text = "\n\n".join(f"- {r}" for r in Rev_Rec)
        else:
            review_text = str(Rev_Rec)

        line("Review", review_text)

# Personal Section
def Personal_Libray_List(Personal_tab):
    Title_box(Personal_tab, text="Welcome to your Personal Library List")

    list_frame = Containter_Left_Box_Scroll(Personal_tab)
    Personal_Library = Personal_load_data
    view_Personal_Section(list_frame, Personal_Library)

    right_panel = Personal_Right_Box_Add_Del(Personal_tab)

    Add_Content_Frame = Add_Popup_Container(right_panel, Personal_tab)
    Adding_Story_Box(Add_Content_Frame)

    Del_Content_Frame = Del_Popup_Container(right_panel, Personal_tab)
    deleting_Story_Box(Del_Content_Frame)

    Share_Content_Frame = Share_Popup_Container(right_panel, Personal_tab)
    Share_Story_Box(Share_Content_Frame)

# Public Section
def Public_List(Public_tab):
    Title_box(Public_tab, text="Welcome to the Public List")

    list_frame = Containter_Center_Box_Scroll(Public_tab)
    Public_Library = Public_load_data
    view_Public_Section(list_frame, Public_Library)



# Public menu
def main_menu(home):
    Title_box(home, text="MMM Library")
    Intro_box(home, text="Welcome to your Manga, Manhwa and Manhua Library", font=("Courier", 30, "bold"),)
    Intro_box(home, text="Share the stories you love and discover new favorites", font=("Courier", 25,),)
# for displaying 3 section   
def display_menu(root):
    style = ttk.Style()
    style.theme_use("default")

    style.configure("TNotebook", background="#E6D6FF", borderwidth=0)

    style.configure("TNotebook.Tab", background="#D6B3FF", foreground="white", padding=[25, 10])

    style.map("TNotebook.Tab", background=[("selected", "#B57CFF")])

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # TAB 1 (Home)
    home = tk.Frame(notebook, bg="#3E3E3E")
    notebook.add(home, text="Home")

    # TAB 2 (Personal)
    personal_tab = tk.Frame(notebook, bg="#3E3E3E")
    notebook.add(personal_tab, text="Personal Library")

    # TAB 3 (Public)
    public_tab = tk.Frame(notebook, bg="#3E3E3E")
    notebook.add(public_tab, text="Public Library")

    # Tab Switching
    def on_tab_change(event):
        selected = notebook.index(notebook.select())
        #Just for clearing 
        for frame in [home, personal_tab, public_tab]:
            for widget in frame.winfo_children():
                widget.destroy()

        if selected == 0:
            main_menu(home)
        elif selected == 1:
            Personal_Libray_List(personal_tab)

        elif selected == 2:
            Public_List(public_tab)

    notebook.bind("<<NotebookTabChanged>>", on_tab_change)

def main():
    root = tk.Tk()
    root.title("MMM Library")
    root.state("zoomed")
    display_menu(root)

    print("-----Programmed ended-----")

    root.mainloop()
if __name__ == "__main__":
    main()

      