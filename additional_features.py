import os
import sys
import subprocess
import shutil
import datetime

from constants import DEF_INPUT, DEF_OUTPUT, DEF_BACKUP, DEF_INPUT_REWARD_TABLE, DEF_INPUT_DEFAULT_REWARD_TABLE, DEF_INPUT_INSTRUCTIONS, DEF_INPUT_PROMPT_SYSTEM, DEF_OUTPUT_NEW_REWARD_TABLE, DEF_OUTPUT_DESIGN_PRINCIPLES, DEF_OUTPUT_Q_TABLE

class CAdditionalFeatures:
    """
    Class for additional features in the Q-Learning Power Control project.
    """

    def __init__(self):
        """
        Constructor: Defines data members, generates input and output folder if they don't exist.
        """
        print("constructor")

    def __del__(self):
        """
        Destructor: Cleans up when the object is destroyed.
        """
        print("destructor")

    def __back(self):
        """
        Back: Returns to the previous menu.
        """
        print("__back")
        return True

    def __invalid(self):
        """
        Invalid: Handles invalid user input.
        """
        print("__invalid")

    def __show_reward_table(self):
        """
        Show Reward Table: Opens the reward table CSV file.
        """
        print("__show_reward_table")
        os.system("start " + os.path.abspath(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE))
        return True

    def __show_q_table(self):
        """
        Show Q-table: Opens the Q-table CSV file.
        """
        print("__show_q_table")
        os.system("start " + os.path.abspath(DEF_OUTPUT + "/" + DEF_OUTPUT_Q_TABLE))
        return True

    def __restore_default_reward_table(self):
        """
        Restore Default Reward Table: Restores the default reward table.
        """
        print("__restore_default_reward_table")
        shutil.copyfile(DEF_INPUT + "/" + DEF_INPUT_DEFAULT_REWARD_TABLE, DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE)
        print("Restore completed")
        os.system("start " + os.path.abspath(DEF_INPUT))
        return True

    def __backup_reward_table(self):
        """
        Backup Reward Table: Backs up the current reward table.
        """
        print("__backup_reward_table")
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
        shutil.copyfile(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE, DEF_BACKUP + "/" + DEF_INPUT_REWARD_TABLE + "_" + timestamp + ".csv")
        shutil.copyfile(DEF_OUTPUT + "/" + DEF_OUTPUT_DESIGN_PRINCIPLES, DEF_BACKUP + "/" + DEF_OUTPUT_DESIGN_PRINCIPLES + "_" + timestamp + ".txt")
        print("Backup completed")
        os.system("start " + os.path.abspath(DEF_BACKUP))
        shutil.copyfile(DEF_OUTPUT + "/" + DEF_OUTPUT_NEW_REWARD_TABLE, DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE)
        return True

    def run(self):
        """
        Run: Main loop of the program.
        """
        print("run")

        while True:
            menu = {"1": ("Show Reward Table", self.__show_reward_table),
                    "2": ("Show Q-table", self.__show_q_table),
                    "3": ("Restore Default Reward Table", self.__restore_default_reward_table),
                    "4": ("Backup Reward Table", self.__backup_reward_table),
                    "0": ("back", self.__back)
                    }

            for key in menu.keys():
                print(key + ": " + menu[key][0])

            ans = input(">>> ")

            if menu.get(ans, [None, self.__invalid])[1]():
                break

if __name__ == "__main__":
    os.system("chcp 950")  # Switch to Chinese Mode
    CAdditionalFeatures().run()