from Dictionary_of_Stories import Personal_save_data, Personal_load_data

def Title_Story(Personal_Library, Title):
    while True:
        No_input = "1"
        while Title == "":
            return No_input

        Input_Exit = "2"
        while Title.lower() in ((Story["Title"].lower()) for Story in Personal_Library.values()):
            return Input_Exit

        TITLE = Title.upper()
        return TITLE


def Type_Graphic_Novel(Graphic_Novel):
    Graphic_Novels = ["Manwha", "Manhua", "Manga"]

    if Graphic_Novel.lower() in (MMM.lower() for MMM in Graphic_Novels):
        for MMM in Graphic_Novels:
            if Graphic_Novel.lower() == MMM.lower():
                Graphic_Novel = MMM
                return Graphic_Novel
    else:
        return False


def Story_Status(Story_Status):
    Story_Statuses = ["Ongoing", "Completed", "Cancelled", "Hiatus"]

    if Story_Status.lower() in (Status.lower() for Status in Story_Statuses):
        for Stat in Story_Statuses:
            if Story_Status.lower() == Stat.lower():
                Story_Status = Stat
                return Story_Status
    else:
        return False


def Genre_Selection(Genre_Input_List):
    Genres = [
        "Action", "Kingdom Building", "Adventure", "Comedy", "Crime", "Drama", "Fantasy",
        "Gore", "Historical", "Horror", "Isekai", "Mature", "Mecha", "Medical", "Mystery",
        "Romance", "Sci-Fi", "Slice of Life", "Sports", "Superhero", "Thriller",
        "Apocalyptic", "Post-Apocalyptic", "Pre-Apocalyptic", "Cultivation", "Murim",
        "Dungeons", "Martial Arts", "Magic", "Noble", "Rebirth", "Regression", "Reincarnation",
        "Revenge", "Supernatural", "Survival", "Time Travel", "Tower", "Villain"
    ]

    Pick_Genres = []

    for Genre in Genre_Input_List:
        if Genre.upper() == 'X':
            break
        elif Genre.lower() in (Gens.lower() for Gens in Genres):
            if Genre not in Pick_Genres:
                Pick_Genres.append(Genre)
        else:
            pass

    return Pick_Genres


def get_Rec_Rev(Rev_Rec_Input, Change_List):
    def Change_Rec_Rev(Rev_Rec, Change_List):
        for change in Change_List:
            if change.upper() == "Y":
                Rev_Rec = change
        return Rev_Rec

    if Rev_Rec_Input == "":
        return False

    Final_Rev_Rec = Change_Rec_Rev(Rev_Rec_Input, Change_List)

    return Final_Rev_Rec


def Submit_Story(Personal_Library, Story_Info_List, Submit):
    if Submit.upper() == "Y":
        Personal_Library = Personal_load_data()
        count = (len(Personal_Library) + 1)
        key = (f"Story {count}")
        Personal_Library[key] = Story_Info_List
        NewData_PLL = Personal_Library
        Personal_save_data(NewData_PLL)
        return True

    elif Submit.upper() == "N":
        return False

    else:
        return False

def Add_Story(Personal_Library, Title, Graphic_Novel, Status, Genres, Review_Recom, Submit):
    Personal_Library = Personal_load_data()

    Title = Title_Story(Personal_Library, Title)
    if Title == "1":
        return "Please put a Title!"
    if Title == "2":
        return "Title Already Exist!"

    Graphic_Novel = Type_Graphic_Novel(Graphic_Novel)
    if not Graphic_Novel:
        return "Invalid Graphic Novel Type"

    Status = Story_Status(Status)
    if not Status:
        return "Invalid Story Status"

    Genres = Genre_Selection(Genres)

    Review_Recom = get_Rec_Rev(Review_Recom, [])
    if not Review_Recom:
        return "Invalid Review and Recommendation"

    Story_Info_List = {
        "Title": Title,
        "Type of MMM": Graphic_Novel,
        "Story Status": Status,
        "Genres": Genres,
        "Review and recommendation": Review_Recom
    }

    Submit_Story(Personal_Library, Story_Info_List, Submit)