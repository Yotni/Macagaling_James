
from Dictionary_of_Stories import Public_save_data, Personal_load_data, Public_load_data

def Is_PLL_Empty(Personal_Library):
    if not Personal_Library:
        return True
    else:
        return False
    

def load_data():
    Personal_Library = Personal_load_data()
    Public_Library = Public_load_data()
    return Personal_Library, Public_Library


def get_story_ID(story_number, Personal_Library):
    Story_ID = (f"Story {story_number}")

    if Story_ID not in Personal_Library:
        return False
    
    else:
        return Story_ID

def find_public_story(Public_Library, Title_of_story):
    Public_Story_exist = None

    for Pub_Story_ID, PStory_Info in Public_Library.items():
        if PStory_Info.get("Title") == Title_of_story:
            Public_Story_exist = Pub_Story_ID
            break

    return Public_Story_exist

def add_new_story(Public_Library, Story_to_Share, New_Rev_Rec):
    count = (len(Public_Library) + 1)
    New_Story_ID = f"Story {count}"

    if not isinstance(Story_to_Share.get("Review and recommendation"), list):
        Story_to_Share["Review and recommendation"] = [New_Rev_Rec]

    Public_Library[New_Story_ID] = Story_to_Share


def update_existing_story(Public_Library, Public_Story_exist, New_Rev_Rec):
    Story_exist_Rec = Public_Library[Public_Story_exist].get("Review and recommendation")

    if Story_exist_Rec is None:
        Story_exist_Rec = []

    if not isinstance(Story_exist_Rec, list):
        Story_exist_Rec = [Story_exist_Rec]

    if New_Rev_Rec:
        Story_exist_Rec.append(New_Rev_Rec)

    Public_Library[Public_Story_exist]["Review and recommendation"] = Story_exist_Rec


def Share_Personal_list(story_number):
    Personal_Library = Personal_load_data()
    Public_Library = Public_load_data()

    if Is_PLL_Empty(Personal_Library):
        return 

    Story_ID = get_story_ID(story_number, Personal_Library)
    if not Story_ID:
        return

    Story_to_Share = Personal_Library[Story_ID]
    Title_of_story = Story_to_Share.get("Title")

    Public_Story_exist = find_public_story(Public_Library, Title_of_story)
    New_Rev_Rec = Story_to_Share.get("Review and recommendation", "")

    if Public_Story_exist is None:
        add_new_story(Public_Library, Story_to_Share, New_Rev_Rec)
    else:
        update_existing_story(Public_Library, Public_Story_exist, New_Rev_Rec)

    Public_save_data(Public_Library)
    

        
