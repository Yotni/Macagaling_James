import tkinter as tk
from tkinter import messagebox
from Dictionary_of_Stories import Personal_load_data
from Story_Adding_Pure_Def import Add_Story

def Add_Popup_Container(right_panel, parent_tab):
    # Add Button
    Add_button = tk.Button(
        right_panel,
        text="Add",
        bg="#8A2BE2",
        fg="white",
        activebackground="#D6B3FF",
        activeforeground="white",
        relief="groove",
        font=("Courier", 18, "bold")
    )
    Add_button.pack(side="left", expand=True, fill="x", padx=10)

    # parent frame for both scrolbar, then content_frame
    add_box = tk.Frame(parent_tab, bg="#8A2BE2")

    # canvas for the scrollbar
    canvas = tk.Canvas(add_box, bg="#8A2BE2", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    # scrollbar
    scrollbar = tk.Scrollbar(add_box, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # content frame
    content_frame = tk.Frame(canvas, bg="#8A2BE2")

    window_id = canvas.create_window((0, 0), window=content_frame, anchor="nw")

    #  scroll region update
    def update_scroll(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", update_scroll)

    # width matched
    def resize_frame(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", resize_frame)

    # popup toggle
    box_visible = False

    def toggle_popup():
        nonlocal box_visible

        if box_visible:
            add_box.place_forget()
            Add_button.config(bg="#8A2BE2")
            box_visible = False
        else:
            add_box.place(relx=0.635, rely=0.23, relwidth=0.35, relheight=0.76)
            Add_button.config(bg="#D6B3FF")
            box_visible = True

    Add_button.config(command=toggle_popup)

    # return ONLY list_frame so you can add items easily
    return content_frame

def Adding_Story_Box(content_frame):
    inner_box_line = tk.Frame(
        content_frame,
        bg="#8A2BE2",
        highlightbackground="white",
        highlightthickness=1
    )
    inner_box_line.pack(anchor="center", padx=20, pady=20, fill="x")

    StoryBox(inner_box_line)
    return inner_box_line

class StoryBox:
    def __init__(self, parent):
        self.parent = parent

        self.personal_library = Personal_load_data()

        self.selected_type = None
        self.selected_status = None

        self.Story_adding()

    def Story_adding(self):
        self.Add_container = tk.Frame(self.parent, bg="#8A2BE2")
        self.Add_container.pack(padx=20, pady=20, fill="both")

        # just for reusable container
        def Infos_Containers():
            Infos_Container = tk.Frame(self.Add_container, bg="#8A2BE2", 
                                       highlightthickness=1, highlightcolor="white", padx=5, pady=5)
            Infos_Container.pack(fill="both", pady=5)
            return Infos_Container
    
        # Title Box:
        Title_Con = Infos_Containers()
        Title = tk.Label(Title_Con, text="Title: ",font=("Courier", 15, "bold"), bg="#8A2BE2", fg="white")
        Title.pack(anchor="w")
        self.title_entry = tk.Entry(Title_Con,font=('Courier', 15), bg="#D6B3FF")
        self.title_entry.pack(anchor="w", fill="both", )

        #Type of Graphic Novel Box:
        Type_GN = Infos_Containers()
        Graphic_Novel = tk.Label(Type_GN, text="Graphic Novel Type: ",font=("Courier", 15, "bold"),
                                bg="#8A2BE2", fg="white")
        Graphic_Novel.pack(anchor="w")

        type_frame = tk.Frame(Type_GN, bg="#8A2BE2",)
        type_frame.pack()

        self.type_buttons = {}
        for type in ["Manwha", "Manhua", "Manga"]:
            btn = tk.Button(type_frame, text=type, bg="#D6B3FF", fg="Black", 
                            font=("Courier", 10, "bold"), width=10, 
                            command=lambda x=type: self.select_type_MMM(x)
                            )
            btn.pack(side="left", padx=20,)
            self.type_buttons[type] = btn
        

        # Type of Story Status:
        Status_Con = Infos_Containers()
        Status = tk.Label(Status_Con, text="Status: ",font=("Courier", 15, "bold"), bg="#8A2BE2", fg="white")
        Status.pack(anchor="w")

        status_frame = tk.Frame(Status_Con, bg="#8A2BE2")
        status_frame.pack()

        self.status_buttons = {}
        for status in ["Ongoing", "Completed", "Cancelled", "Hiatus"]:
            btn = tk.Button(status_frame, text=status, bg="#D6B3FF", fg="black",
                            font=("Courier", 10, "bold"), width=10,
                            command=lambda x=status: self.select_status(x)
                            )
            btn.pack(side="left", padx=10,)
            self.status_buttons[status] = btn

        # Genres:    
        Genres_Con = Infos_Containers()
        Genres_Design = tk.Label(Genres_Con, text="Genres: ",font=("Courier", 13, "bold"), bg="#8A2BE2", fg="#FFFFFF")
        Genres_Design.pack(anchor="w")

        self.genre_listbox = tk.Listbox(Genres_Con, selectmode="multiple", font=("Courier", 18, "bold"),fg="#FFFFFF", height=20, background="#D6B3FF", 
                                        selectbackground="#8A2BE2", selectforeground="white")
                                    
        self.genre_listbox.pack()

        genres = [
            "Action", "Kingdom Building", "Adventure", "Comedy", "Crime", "Drama", "Fantasy",
            "Gore", "Historical", "Horror", "Isekai", "Mature", "Mecha", "Medical", "Mystery",
            "Romance", "Sci-Fi", "Slice of Life", "Sports", "Superhero", "Thriller",
            "Apocalyptic", "Post-Apocalyptic", "Pre-Apocalyptic", "Cultivation", "Murim",
            "Dungeons", "Martial Arts", "Magic", "Noble", "Rebirth", "Regression", "Reincarnation",
            "Revenge", "Supernatural", "Survival", "Time Travel", "Tower", "Villain"
        ]

        for g in genres:
            
            self.genre_listbox.insert(tk.END, g,)
            self.genre_listbox.pack(fill="x")

        # Review and recommendation
        Rev_rec_Con = Infos_Containers()
        Rev_rec_design = tk.Label(Rev_rec_Con, text="Review and Recommendation", font=("Courier", 13, "bold"), bg="#8A2BE2", fg="white")
        Rev_rec_design.pack(anchor="w")

        self.review_text = tk.Text(Rev_rec_Con, height=6, width=40)
        self.review_text.pack(fill="x")

        Add_but = Infos_Containers
        ADD_STORY = tk.Button(self.Add_container, text="ADD STORY",relief="groove", command=self.submit_story, bg="#D6B3FF", fg="White",)
        ADD_STORY.pack(pady=10)

    # for buttons when click
    def select_type_MMM(self, value):
        self.selected_type = value

        for k, btn in self.type_buttons.items():
            btn.config(bg="#D6B3FF")

        self.type_buttons[value].config(bg="white")

    def select_status(self, value):
        self.selected_status = value

        for k, btn in self.status_buttons.items():
            btn.config(bg="#D6B3FF")

        self.status_buttons[value].config(bg="white")

    def clear_form(self):
        self.title_entry.delete(0, tk.END)
        self.review_text.delete("1.0", tk.END)
        self.genre_listbox.selection_clear(0, tk.END)

        self.selected_type = None
        self.selected_status = None

        for btn in self.type_buttons.values():
            btn.config(bg="#D6B3FF")

        for btn in self.status_buttons.values():
            btn.config(bg="#D6B3FF")

    def submit_story(self):
        title = self.title_entry.get()
        graphic_novel = self.selected_type
        status = self.selected_status

        selected_indices = self.genre_listbox.curselection()
        genres = [self.genre_listbox.get(i) for i in selected_indices]

        review = self.review_text.get("1.0", tk.END).strip()

        result = Add_Story(
            self.personal_library,
            title,
            graphic_novel,
            status,
            genres,
            review,
            Submit="Y"
        )

        if isinstance(result, str):
            messagebox.showerror("Error", result)
            return

        Done = messagebox.showinfo("Success", "Story added")
        if Done:
            self.clear_form()


