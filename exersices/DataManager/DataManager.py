import os
import pandas as pd
MAIN_PATH = r"C:\Users\{}\AppData\Roaming\exercise_app".format(os.getlogin())

if not os.path.exists(MAIN_PATH) :
    os.mkdir(MAIN_PATH)

class SaveData:
    def __init__(self , exercise_name:str):
        global data
        self.exersice_path_file = MAIN_PATH+ f"\{exercise_name}" + ".csv" 


        if not os.path.exists(self.exersice_path_file):
            data = pd.DataFrame([[0 , 0]] , columns=["LastRep" , "MaxRep"])            
            data.to_csv(self.exersice_path_file , index=False)

        data = pd.read_csv(self.exersice_path_file)

        self.lastrep = data.iloc[0 , 0]
        self.maxrep = data.iloc[0 , 1]

    def update_csv(self , nowrep) :
        if nowrep > self.maxrep :
            self.lastrep , self.maxrep = nowrep , nowrep

            data.iloc[0 , :] = self.lastrep , self.maxrep
            data.to_csv(self.exersice_path_file ,index=False)


        elif nowrep < self.maxrep :
            self.lastrep , self.maxrep = nowrep , self.maxrep

            data.iloc[0 , :] = self.lastrep , self.maxrep
            data.to_csv(self.exersice_path_file ,index=False)

        
