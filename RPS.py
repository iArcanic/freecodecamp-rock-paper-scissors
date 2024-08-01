# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # Initialize history tracking
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize player state
    if 'markov_chain' not in player.__dict__:
        player.markov_chain = {}
        player.last_moves = ""
        player.pattern_length = 3
        player.strategy = "markov"
        player.markov_wins = 0
        player.freq_wins = 0

    # Update the Markov chain with the last move
    if len(player.last_moves) >= player.pattern_length:
        if player.last_moves not in player.markov_chain:
            player.markov_chain[player.last_moves] = {'R': 0, 'P': 0, 'S': 0}
        if prev_play:
            player.markov_chain[player.last_moves][prev_play] += 1

    # Update the last_moves sequence
    player.last_moves = (player.last_moves + prev_play)[-player.pattern_length:] if prev_play else player.last_moves

    # Frequency analysis
    move_count = {'R': opponent_history.count('R'), 'P': opponent_history.count('P'), 'S': opponent_history.count('S')}
    most_frequent_move = max(move_count, key=move_count.get)
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    freq_move = counter_moves[most_frequent_move]

    # Markov chain prediction
    if len(opponent_history) < player.pattern_length:
        return "R"
    
    possible_moves = player.markov_chain.get(player.last_moves, {'R': 0, 'P': 0, 'S': 0})
    predicted_move = max(possible_moves, key=possible_moves.get)
    markov_move = counter_moves[predicted_move]

    # Adaptive switching based on strategy performance
    total_games = len(opponent_history)
    markov_performance = player.markov_wins / total_games if total_games > 0 else 0
    freq_performance = player.freq_wins / total_games if total_games > 0 else 0
    
    # Update strategy based on performance
    if markov_performance < 0.55 and freq_performance > 0.55:
        player.strategy = "frequency"
    elif freq_performance < 0.55 and markov_performance > 0.55:
        player.strategy = "markov"

    # Return the move based on the selected strategy
    return markov_move if player.strategy == "markov" else freq_move
