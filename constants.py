# Description: Constants used in the project

# Directories for input, output, and backup files
DEF_INPUT = "Input"
DEF_OUTPUT = "Output"
DEF_BACKUP = "Backup"

# File names for different versions of the reward table
DEF_INPUT_REWARD_TABLE = 'reward_table.csv'
DEF_INPUT_DEFAULT_REWARD_TABLE = 'reward_table_default.csv'
DEF_INPUT_REWARD_TABLE_PERFORMANCE = 'reward_table_performance.csv'
DEF_INPUT_REWARD_TABLE_POWER_SAVING = 'reward_table_power_saving.csv'
DEF_INPUT_REWARD_TABLE_BALANCED = 'reward_table_balanced.csv'

# File names for instructions and prompt system
DEF_INPUT_INSTRUCTIONS = 'instructions.txt'
DEF_INPUT_PROMPT_SYSTEM = 'prompt_system.txt'

# File names for output files
DEF_OUTPUT_NEW_REWARD_TABLE = 'new_reward_table.csv'
DEF_OUTPUT_DESIGN_PRINCIPLES = 'design_principles.txt'
DEF_OUTPUT_Q_TABLE = 'q_table.csv'

# Function to generate prompt for system
def DEF_PROMPT_SYSTEM(reward_table, reward_table_performance, reward_table_power_saving, reward_table_balanced):
    """
    Generates a prompt for the system to create a new reward table based on user requirements.
    """
    return f"Please generate a new reward table based on the user's requirements and explain its design. The original reward table is as follows:\n\n{reward_table}\n\nPlease output using the following format to separate the reward table and design explanation:\n\n[Reward Table]\n[Design Principle]\n\nReference examples:\nPerformance: {reward_table_performance}\nPower Saving: {reward_table_power_saving}\nBalanced: {reward_table_balanced}\n\nPlease note:\n1. The Reward Table section must retain the original {DEF_INPUT_DEFAULT_REWARD_TABLE} format without any extra text.\n2. This section will be saved separately as a {DEF_OUTPUT_NEW_REWARD_TABLE} file.\n\nThis is very important, so please follow these instructions carefully."

# Function to generate prompt for user
def DEF_PROMPT_USER_PREFIX(prompt_user):
    """
    Generates a prompt for the user to provide a new reward table.
    """
    return f'Please provide a new reward table. {prompt_user}'