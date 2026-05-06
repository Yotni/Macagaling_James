from Dictionary_of_Stories import Personal_save_data, Personal_load_data


def Story_Existence(Personal_Library, Story_Number):
    key = f"Story {Story_Number}"
    Input_Invalid = "1"
    
    if key not in Personal_Library:
        return Input_Invalid

    return key


def Confirm_Delete_Action(key, Personal_Library, Confirm):
    if Confirm.upper() == "Y":
        return True
    elif Confirm.upper() == "N":
        return False
    else:
        return "INVALID"


def Delete_and_Reindex(Personal_Library, key):
    del Personal_Library[key]

    new_data = {}
    for i, (k, v) in enumerate(Personal_Library.items(), start=1):
        new_data[f"Story {i}"] = v

    Personal_save_data(new_data)
    return new_data


def Ask_Delete_More(Delete_Another):
    if Delete_Another.upper() in ["Y", "N"]:
        return Delete_Another.upper()
    return False


def Story_Deleting(Personal_Library, Story_Number, Confirm, Delete_Another):
    Personal_Library = Personal_load_data()

    key = Story_Existence(Personal_Library, Story_Number)

    if key == "1":
        return "Invalid Story ID Input!"

    confirm_result = Confirm_Delete_Action(key, Personal_Library, Confirm)

    if confirm_result == "INVALID":
        return "Invalid confirmation input"

    if confirm_result:
        Personal_Library = Delete_and_Reindex(Personal_Library, key)

        return {
            "result": "Story Deleted Successfully",
            "library": Personal_Library
        }

    return "Deletion Cancelled"
