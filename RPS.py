# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # Initialize the opponent's history if it's the first game
    if prev_play:
        opponent_history.append(prev_play)
    
    # Initialize Markov chain dictionary
    if 'markov_chain' not in player.__dict__:
        player.markov_chain = {key: 0 for key in ["RR", "RP", "RS", "PR", "PP", "PS", "SR", "SP", "SS"]}
        player.last_move = None
    
    # Update Markov chain with the previous move if both are valid
    if player.last_move is not None and prev_play:
        player.markov_chain[player.last_move + prev_play] += 1
    
    # Set the last move to the current prev_play for the next round
    player.last_move = prev_play if prev_play else player.last_move
    
    # Default first moves
    if len(opponent_history) < 2:
        return "R"
    
    # Predict next move based on Markov chain
    last_two = "".join(opponent_history[-2:])
    possible_moves = [last_two + "R", last_two + "P", last_two + "S"]
    
    # Filter out invalid keys
    possible_moves = [move for move in possible_moves if move in player.markov_chain]
    
    # In case all possible moves are invalid, default to 'R'
    if not possible_moves:
        return "R"
    
    predictions = {move: player.markov_chain[move] for move in possible_moves}
    predicted_move = max(predictions, key=predictions.get)[-1]
    
    # Counter the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
