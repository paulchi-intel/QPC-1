import os
import sys
import subprocess

from q_learning import CQLearning
from simulate_states_actions import CSimulateStatesActions
from modify_reward_table import CModifyRewardTable
from additional_features import CAdditionalFeatures

from constants import (DEF_INPUT, DEF_OUTPUT, DEF_BACKUP, DEF_INPUT_INSTRUCTIONS,
                       DEF_INPUT_PROMPT_SYSTEM, DEF_OUTPUT_NEW_REWARD_TABLE,
                       DEF_OUTPUT_DESIGN_PRINCIPLES, DEF_OUTPUT_Q_TABLE)

class CMain:
    """
    Main class for the Q-Learning Power Control project.
    """

    def __init__(self):
        """
        Constructor: Defines data members and creates input, output, and backup folders if they don't exist.
        """
        print("constructor")

        # Create input, output and backup folders if they don't exist
        for directory in [DEF_INPUT, DEF_OUTPUT, DEF_BACKUP]:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def __del__(self):
        """
        Destructor: Cleans up when the object is destroyed.
        """
        print("destructor")

    def __exit(self):
        """
        Exit: Exits the program.
        """
        print("__exit")
        sys.exit()

    def __invalid(self):
        """
        Invalid: Handles invalid user input.
        """
        print("__invalid")

    def __converge_q_table(self):
        """
        Converge Q-table: Runs the Q-Learning algorithm.
        """
        print("__converge_q_table")
        CQLearning().run()

    def __simulate_states_actions(self):
        """
        Simulate States / Actions: Simulates states and actions.
        """
        print("__simulate_states_actions")
        CSimulateStatesActions().run()

    def __modify_reward_table(self):
        """
        Modify Reward Table: Modifies the reward table.
        """
        print("__modify_reward_table")
        CModifyRewardTable().run()

    def __additional_features(self):
        """
        Additional Features: Runs additional features.
        """
        print("__additional_features")
        CAdditionalFeatures().run()

    def run(self):
        """
        Run: Main loop of the program.
        """
        print("run")

        while True:
            menu = {"1": ("Converge Q-table", self.__converge_q_table),
                    "2": ("Simulate States / Actions", self.__simulate_states_actions),
                    "3": ("Modify Reward Table", self.__modify_reward_table),
                    "4": ("Additional Features", self.__additional_features),
                    "0": ("exit", self.__exit)
                    }

            # Print the menu
            for key in menu.keys():
                print(key + ": " + menu[key][0])

            # Get user input
            ans = input(">>> ")

            # Get the corresponding function pointer based on user input and call it
            menu.get(ans, [None, self.__invalid])[1]()


if __name__ == "__main__":
    os.system("chcp 950")  # Switch to Chinese Mode

    my_main = CMain()
    my_main.run()