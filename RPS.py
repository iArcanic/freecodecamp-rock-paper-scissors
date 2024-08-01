# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    # Initialize the opponent's history if it's the first game
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize Markov chain dictionary and counters for adaptive strategy
    if 'markov_chain' not in player.__dict__:
        player.markov_chain = {}
        player.last_moves = ""
        player.strategy = "markov"
        player.markov_wins = 0
        player.freq_wins = 0
    
    # Update Markov chain with previous moves
    if len(player.last_moves) >= 5:
        if player.last_moves not in player.markov_chain:
            player.markov_chain[player.last_moves] = {'R': 0, 'P': 0, 'S': 0}
        if prev_play:
            player.markov_chain[player.last_moves][prev_play] += 1
    
    # Update the last_moves sequence
    player.last_moves = (player.last_moves + prev_play)[-5:] if prev_play else player.last_moves

    # Frequency analysis
    move_count = {'R': opponent_history.count('R'), 'P': opponent_history.count('P'), 'S': opponent_history.count('S')}
    most_frequent_move = max(move_count, key=move_count.get)
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    freq_move = counter_moves[most_frequent_move]

    # Markov chain prediction
    if len(opponent_history) < 5:
        return "R"
    
    possible_moves = player.markov_chain.get(player.last_moves, {'R': 0, 'P': 0, 'S': 0})
    predicted_move = max(possible_moves, key=possible_moves.get)
    markov_move = counter_moves[predicted_move]
    
    # Switch strategy based on performance
    if player.strategy == "markov":
        if prev_play == counter_moves[markov_move]:
            player.markov_wins += 1
        else:
            player.markov_wins = max(player.markov_wins - 1, 0)
        
        if player.markov_wins < player.freq_wins:
            player.strategy = "frequency"
            player.markov_wins = 0
    
    if player.strategy == "frequency":
        if prev_play == counter_moves[freq_move]:
            player.freq_wins += 1
        else:
            player.freq_wins = max(player.freq_wins - 1, 0)
        
        if player.freq_wins < player.markov_wins:
            player.strategy = "markov"
            player.freq_wins = 0
    
    return markov_move if player.strategy == "markov" else freq_move
