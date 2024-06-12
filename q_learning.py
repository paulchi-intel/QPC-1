import os
import sys
import numpy as np
from constants import DEF_INPUT, DEF_OUTPUT, DEF_INPUT_REWARD_TABLE, DEF_INPUT_INSTRUCTIONS, DEF_INPUT_PROMPT_SYSTEM, DEF_OUTPUT_NEW_REWARD_TABLE, DEF_OUTPUT_DESIGN_PRINCIPLES, DEF_OUTPUT_Q_TABLE
import matplotlib.pyplot as plt
import csv

class CQLearning:
    """
    Class for Q-Learning algorithm.
    """

    def __init__(self):
        """
        Constructor: Defines data members, generates input and output folder if they don't exist.
        """
        print("constructor")

        # Define States and Actions, states from S1 to S72, actions from A1 to A4
        self.states = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "S14", "S15", "S16",
                  "S17", "S18", "S19", "S20", "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28", "S29", "S30", "S31",
                  "S32", "S33", "S34", "S35", "S36", "S37", "S38", "S39", "S40", "S41", "S42", "S43", "S44", "S45", "S46",
                  "S47", "S48", "S49", "S50", "S51", "S52", "S53", "S54", "S55", "S56", "S57", "S58", "S59", "S60", "S61",
                  "S62", "S63", "S64", "S65", "S66", "S67", "S68", "S69", "S70", "S71", "S72"]
        self.actions = ["A1", "A2", "A3", "A4"]

        # Check if DEF_OUTPUT/DEF_OUTPUT_Q_TABLE exists, if yes, use it to initialize Q-table, if not, initialize Q-table with zeros
        if os.path.exists(DEF_OUTPUT + "/" + DEF_OUTPUT_Q_TABLE):
            with open(DEF_OUTPUT + "/" + DEF_OUTPUT_Q_TABLE, "r") as f:
                reader = csv.reader(f)
                q_table = list(reader)

            # Convert Q-table to numpy array
            self.Q_table = np.array([list(map(float, row[1:])) for row in q_table[1:]])
        else:
            # Initialize Q-table with zeros
            self.Q_table = np.zeros((len(self.states), len(self.actions)))

        # Reward structure, reward_table state from S1 to S72, action from A1 to A4, the value of reward is read from Q-Table.csv at runtime
        self.reward_table = {}

        with open(DEF_INPUT + "/" + DEF_INPUT_REWARD_TABLE, "r") as f:
            # Skip the first line
            next(f)
            for line in f:
                state, _, _, _, _, reward_a1, reward_a2, reward_a3, reward_a4 = line.strip().split(",")
                self.reward_table[(state, self.actions[0])] = float(reward_a1)
                self.reward_table[(state, self.actions[1])] = float(reward_a2)
                self.reward_table[(state, self.actions[2])] = float(reward_a3)
                self.reward_table[(state, self.actions[3])] = float(reward_a4)

        # Parameters of Q-learning
        self.alpha = 0.1  # Learning Rate
        self.gamma = 0.9  # Discount Factor
        self.episodes = 50  # Number of training iterations

    def __del__(self):
        """
        Destructor: Cleans up when the object is destroyed.
        """
        print("destructor")

    def __get_next_state(self, state, action):
        """
        Get Next State: Returns the next state given the current state and action.
        """
        print("get_next_state")
        next_state = np.random.choice(self.states)
        return next_state

    def __plot_q_table(self, str_title):
        """
        Plot Q-table: Plots the Q-table.
        """
        print("plot_q_table")

        plt.clf()

        # Plot a line for each action
        for i, action in enumerate(self.actions):
            plt.plot(self.states, self.Q_table[:, i], label=action)

        # Add legend
        plt.legend(loc='lower right')

        # Add x and y axis labels
        plt.xlabel('States')
        plt.ylabel('Q value')

        xticks = [0, 9, 18, 27, 36, 45, 54, 63, 71]  # Select indices for S1, S37, S72
        xticklabels = [self.states[i] for i in xticks]  # Get corresponding state labels
        plt.xticks(xticks, xticklabels)

        plt.title(str_title)
        plt.grid(True)
        plt.draw()
        plt.pause(0.05)

    def run(self):
        """
        Run: Main loop of the program.
        """
        print("run")

        for episode in range(self.episodes):
            state = np.random.choice(self.states) # randomly select a state to start

            while True:
                # select action
                action_index = np.random.choice(len(self.actions))
                action = self.actions[action_index]

                # do action, get reward and next state
                reward = self.reward_table[(state, action)]
                next_state = self.__get_next_state(state, action)

                # Update Q-value
                state_index = self.states.index(state)
                next_state_index = self.states.index(next_state)
                max_next_Q = np.max(self.Q_table[next_state_index, :])
                self.Q_table[state_index, action_index] = self.Q_table[state_index, action_index] + self.alpha * (
                            reward + self.gamma * max_next_Q - self.Q_table[state_index, action_index])

                # Check if the episode ends
                if state == "S72" and action == "A1":
                    print(f"Episode: {episode + 1}")
                    print(f"State: {state}")
                    print(f"Action: {action}")
                    print(f"Reward: {reward}")
                    print(f"Next State: {next_state}")
                    print("Updated Q-table:")
                    print("State \\ Action\tA1\t\tA2\t\tA3\t\tA4")
                    for i, state in enumerate(self.states):
                        print(f"{state}\t\t\t\t{self.Q_table[i, 0]:.2f}\t{self.Q_table[i, 1]:.2f}\t{self.Q_table[i, 2]:.2f}\t{self.Q_table[i, 3]:.2f}")
                    print("=" * 50)

                    self.__plot_q_table("Episode:" + str(episode+1))
                    break

                state = next_state

        # Print the final Q-table
        print("Final Q-table:")
        print("State \\ Action\tA1\t\tA2\t\tA3\t\tA4")
        for i, state in enumerate(self.states):
            print(f"{state}\t\t\t\t{self.Q_table[i, 0]:.2f}\t{self.Q_table[i, 1]:.2f}\t{self.Q_table[i, 2]:.2f}\t{self.Q_table[i, 3]:.2f}")

        self.__plot_q_table("Final Q-Table")

        # output the Q-table to DEF_OUTPUT\DEF_OUTPUT_Q_TABLE, with 2D output ex: state, A1, A2, A3, A4
        with open(DEF_OUTPUT + "/" + DEF_OUTPUT_Q_TABLE, "w") as f:
            f.write("State,A1,A2,A3,A4\n")
            for i, state in enumerate(self.states):
                f.write(f"{state},{self.Q_table[i, 0]},{self.Q_table[i, 1]},{self.Q_table[i, 2]},{self.Q_table[i, 3]}\n")

if __name__ == "__main__":
    os.system("chcp 950")  # Switch to Chinese Mode

    CQLearning().run()