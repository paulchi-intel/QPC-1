import os
import sys
import subprocess
import shutil
import datetime
import threading
import time
import itertools

from constants import DEF_INPUT, DEF_OUTPUT, DEF_BACKUP, DEF_INPUT_REWARD_TABLE, DEF_INPUT_DEFAULT_REWARD_TABLE, DEF_INPUT_INSTRUCTIONS, DEF_INPUT_PROMPT_SYSTEM, DEF_OUTPUT_NEW_REWARD_TABLE, DEF_OUTPUT_DESIGN_PRINCIPLES, DEF_OUTPUT_Q_TABLE, DEF_PROMPT_SYSTEM, DEF_PROMPT_USER_PREFIX
import openai
from dotenv import load_dotenv

class LoadingAnimation(threading.Thread):
    """
    Class for creating a loading animation while waiting for a response.
    """
    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        """
        Run: Starts the loading animation.
        """
        self.running = True
        for c in itertools.cycle(['.', '..', '...', '....', '.....']):
            if not self.running:
                break
            print(f'\rGenerating Response{c}', end='', flush=True)
            time.sleep(0.2)
        print('\rDone!     ')

    def stop(self):
        """
        Stop: Stops the loading animation.
        """
        self.running = False

class CModifyRewardTable:
    """
    Class for modifying the reward table in the Q-Learning Power Control project.
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

    def __modify_transcript(self, prompt_user):
        """
        Modify Transcript: Modifies the transcript based on the user's prompt.
        """
        print("__modify_transcript")
        load_dotenv()
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        with open(DEF_INPUT + "/" + DEF_INPUT_DEFAULT_REWARD_TABLE, 'r', encoding='utf-8') as file:
            reward_table = file.read()

        with open(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE_PERFORMANCE, 'r', encoding='utf-8') as file:
            reward_table_performance = file.read()

        with open(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE_POWER_SAVING, 'r', encoding='utf-8') as file:
            reward_table_power_saving = file.read()

        with open(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE_BALANCED, 'r', encoding='utf-8') as file:
            reward_table_balanced = file.read()

        prompt_system = DEF_PROMPT_SYSTEM(reward_table, reward_table_performance, reward_table_power_saving, reward_table_balanced)
        prompt_user = DEF_PROMPT_USER_PREFIX(prompt_user)

        animation = LoadingAnimation()
        animation.start()

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": prompt_user}
            ]
        )

        animation.stop()
        animation.join()

        content = response['choices'][0]['message']['content']

        if "[Design Principle]" in content:
            split_content = content.split("[Design Principle]")
            new_reward_table = split_content[0].replace("[Reward Table]", "").strip()
            design_principal = split_content[1].strip()
        else:
            new_reward_table = content.replace("[Reward Table]", "").strip()
            design_principal = "No Design Principal provided."

        with open(DEF_OUTPUT + "/" + DEF_OUTPUT_NEW_REWARD_TABLE, 'w', encoding='utf-8') as file:
            file.write(new_reward_table)

        with open(DEF_OUTPUT + "/" + DEF_OUTPUT_DESIGN_PRINCIPLES, 'w', encoding='utf-8') as file:
            file.write(design_principal)

        shutil.copyfile(DEF_OUTPUT + "/" + DEF_OUTPUT_NEW_REWARD_TABLE, DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE)

    def __high_performance(self):
        """
        High Performance: Modifies the reward table for high performance.
        """
        print("__high_performance")
        user_prompt = "I'm going to play games, keep it in high performance mode at all times unless the battery is really low."
        print("Prompt: " + user_prompt)
        self.__modify_transcript(user_prompt)
        return True

    def __high_power_saving(self):
        """
        High Power Saving: Modifies the reward table for high power saving.
        """
        print("__high_power_saving")
        user_prompt = "I'll be out all day and won't be able to charge my device, keep it in low power mode at all times."
        print("Prompt: " + user_prompt)
        self.__modify_transcript(user_prompt)
        return True

    def __balanced(self):
        """
        Balanced: Modifies the reward table for balanced performance and power saving.
        """
        print("__balanced")
        user_prompt = "Balancing performance and power saving."
        print("Prompt: " + user_prompt)
        self.__modify_transcript(user_prompt)
        return True

    def __zero_fill(self):
        """
        Zero Fill: Fills the reward table with zeros.
        """
        print("__zero_fill")
        user_prompt = "Fill in the reward table with zeros."
        print("Prompt: " + user_prompt)
        self.__modify_transcript(user_prompt)
        return True

    def __custom(self):
        """
        Custom: Modifies the reward table based on user input.
        """
        print("__custom")
        user_prompt = input("Please enter your custom prompt: ")
        print("Prompt: " + user_prompt)
        self.__modify_transcript(user_prompt)
        return True

    def run(self):
        """
        Run: Main loop of the program.
        """
        print("run")

        while True:
            menu = {"1": ("High Performance", self.__high_performance),
                    "2": ("High Power Saving", self.__high_power_saving),
                    "3": ("Balanced", self.__balanced),
                    "4": ("Fill with Zero", self.__zero_fill),
                    "5": ("Custom (User Input)", self.__custom),
                    "0": ("back", self.__back)
                    }

            for key in menu.keys():
                print(key + ": " + menu[key][0])

            ans = input(">>> ")

            if menu.get(ans, [None, self.__invalid])[1]():
                break

if __name__ == "__main__":
    os.system("chcp 950")  # Switch to Chinese Mode
    CModifyRewardTable().run()