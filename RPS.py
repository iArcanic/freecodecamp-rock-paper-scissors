import random

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[]):
    # Initialize player state
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize Markov chain and move history if not present
    if 'markov_chain' not in player.__dict__:
        player.markov_chain = {}
        player.history_length = 2  # Adjust length for pattern matching

    # Update Markov chain with the last moves
    if prev_play and len(opponent_history) > player.history_length:
        last_moves = ''.join(opponent_history[-player.history_length:])
        if last_moves not in player.markov_chain:
            player.markov_chain[last_moves] = {'R': 0, 'P': 0, 'S': 0}
        player.markov_chain[last_moves][prev_play] += 1

    # Generate the prediction
    if len(opponent_history) > player.history_length:
        last_moves = ''.join(opponent_history[-player.history_length:])
        move_counts = player.markov_chain.get(last_moves, {'R': 1, 'P': 1, 'S': 1})  # Default to avoid empty dict
        predicted_move = max(move_counts, key=move_counts.get)
    else:
        # Fallback to random choice if not enough history
        predicted_move = random.choice(['R', 'P', 'S'])

    # Counter strategy based on prediction
    move_counter = {'R': 'P', 'P': 'S', 'S': 'R'}
    return move_counter.get(predicted_move, random.choice(['R', 'P', 'S']))
