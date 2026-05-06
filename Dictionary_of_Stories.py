import json

File_Path_Personal = "Permanent_PLL.json"

def Personal_save_data(NewData_PLL):
    Data = NewData_PLL
    try:
        with open(File_Path_Personal, 'w') as File:
            json.dump(Data, File, indent = 1)
    except:
        return {}
def Personal_load_data():
    try:
        with open(File_Path_Personal, "r") as file:
            return json.load(file)
    except:
        return {}
    
File_Path_Public= "Permanent_Public_List.json"

def Public_save_data(NewData_Public):
    Data = NewData_Public
    try:
        with open(File_Path_Public, 'w') as File:
            json.dump(Data, File, indent = 1)
    except:
        return {}
def Public_load_data():
    try:
        with open(File_Path_Public, "r") as file:
            return json.load(file)
    except:
        return {}
    

