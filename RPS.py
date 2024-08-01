# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # Initialize the opponent's history if it's the first game
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize Markov chain dictionary
    if 'markov_chain' not in player.__dict__:
        player.markov_chain = {}
        player.last_moves = ""
    
    # Update Markov chain with previous moves
    if len(player.last_moves) >= 5:
        if player.last_moves not in player.markov_chain:
            player.markov_chain[player.last_moves] = {'R': 0, 'P': 0, 'S': 0}
        if prev_play:
            player.markov_chain[player.last_moves][prev_play] += 1
    
    # Set the last moves
    player.last_moves = (player.last_moves + prev_play)[-5:] if prev_play else player.last_moves
    
    # Default first move
    if len(opponent_history) < 5:
        return "R"
    
    # Predict the opponent's next move based on the most frequent subsequent move
    possible_moves = player.markov_chain.get(player.last_moves, {'R': 0, 'P': 0, 'S': 0})
    predicted_move = max(possible_moves, key=possible_moves.get)
    
    # Counter the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
