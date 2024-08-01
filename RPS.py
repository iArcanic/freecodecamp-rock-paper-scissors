# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return "R"
    
    # Count occurrences of each move
    counts = {"R": opponent_history.count("R"), "P": opponent_history.count("P"), "S": opponent_history.count("S")}
    
    # Find the move with the highest count
    most_frequent = max(counts, key=counts.get)
    
    # Play the move that beats the opponent's most frequent move
    if most_frequent == "R":
        return "P"
    elif most_frequent == "P":
        return "S"
    else:
        return "R"
