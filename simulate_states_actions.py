import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import csv

from constants import DEF_INPUT, DEF_OUTPUT, DEF_INPUT_REWARD_TABLE, DEF_INPUT_INSTRUCTIONS, DEF_INPUT_PROMPT_SYSTEM, DEF_OUTPUT_NEW_REWARD_TABLE, DEF_OUTPUT_DESIGN_PRINCIPLES, DEF_OUTPUT_Q_TABLE

class CSimulateStatesActions:

    def __draw_gui(self):
        """
        Draw GUI: Creates a graphical user interface for the simulation.
        """
        print("draw_gui")

        # Read CSV file from DEF_INPUT/DEF_INPUT_REWARD_TABLE and convert it to a list
        with open(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)

        # Create a Tk window
        root = tk.Tk()
        root.attributes("-fullscreen", True)
        # Set the title of the window
        root.title("QPC (Q-Learning Power Control)")

        # Add a title above the Listbox
        title = tk.Label(root, text="State (Power Source,Remaining Power,Drain Rate,Application)",
                         font=("Helvetica", 14))
        title.grid(row=0, column=0, sticky='w')

        # Create a Listbox to display all states, and set its width to 50, font size to 14 and height to 30
        listbox = tk.Listbox(root, font=("Helvetica", 14))
        listbox.grid(row=1, column=0, sticky='nsew')

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Add all states to the Listbox
        for row in data[1:]:  # Skip the header row
            state_info = f"{row[0]} ({row[1]}, {row[2]}, {row[3]}, {row[4]})"
            listbox.insert(tk.END, state_info)

        # Add a Text widget on the right to display state history
        history_title = tk.Label(root, text="State History", font=("Helvetica", 14))
        history_title.grid(row=0, column=1, sticky='ew')

        history_text = tk.Text(root, font=("Helvetica", 14), padx=0, pady=0)
        history_text.grid(row=1, column=1, sticky='nsew')

        root.grid_columnconfigure(1, weight=1)

        # Create a function to handle user selection
        def on_select(event):
            # Get the currently selected state
            index = listbox.curselection()[0]
            state = listbox.get(index)

            # Read the DEF_OUTPUT_Q_TABLE file under DEF_OUTPUT
            # Find the corresponding Action(A1, A2, A3, A4, select the one with the highest Reward) based on States
            with open(DEF_OUTPUT + "/" + DEF_OUTPUT_Q_TABLE, "r") as f:
                reader = csv.reader(f)
                q_table = list(reader)  # Read the Q-table
                states = q_table[0][1:]  # Skip the header column
                actions = q_table[1:]  # Skip the header row
                state_name = state.split(' ')[0]  # Get the state name
                # Find state_name from state, then find the corresponding Action(A1, A2, A3, A4), select the one with the highest Reward
                for row in actions:
                    if row[0] == state_name:
                        max_value = max(float(i) for i in row[1:])
                        action_index = row.index(str(max_value))
                        action = f"A{action_index}"
                        print(f"Best action for state {state_name}: {action}")
                        break

            # Add the selected state and corresponding Action to the "State History" Text widget
            # Add explanation after action (ex: A1: Performance; A2: Efficiency; A3: Balanced; A4: Power Saving)
            action_explain = {'A1': 'Performance', 'A2': 'Efficiency', 'A3': 'Balanced', 'A4': 'Power Saving'}
            history_text.insert('1.0', state + ' ' + action + ' (' + action_explain[action] + ')' + '\n')

        # Call the on_select function when the user selects a state
        listbox.bind('<<ListboxSelect>>', on_select)

        # Add a Button widget below the "State History" Text widget
        clear_button = tk.Button(root, text="Clear", command=lambda: history_text.delete(1.0, tk.END),
                                 font=("Helvetica", 14), padx=10, pady=10)
        clear_button.grid(row=2, column=1, sticky='ew')
        # "Exit" button
        exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 14), padx=10, pady=10)
        exit_button.grid(row=2, column=0, sticky='w')
        # Run the Tk window
        root.mainloop()

    def __init__(self):
        """
        Constructor: Defines data members, generates input and output folder if they don't exist.
        """
        print("constructor")

        self.__draw_gui()

    def __del__(self):
        """
        Destructor: Cleans up when the object is destroyed.
        """
        print("destructor")

    def run(self):
        """
        Run: Main loop of the program.
        """
        print("run")

if __name__ == "__main__":
    os.system("chcp 950")  # Switch to Chinese Mode

    CSimulateStatesActions().run()