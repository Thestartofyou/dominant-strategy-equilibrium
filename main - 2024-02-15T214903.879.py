def find_dominant_strategy(matrix):
    """
    Find dominant strategy for a player in a given payoff matrix.

    Parameters:
    matrix (list of lists): Payoff matrix representing the game.

    Returns:
    int or None: Index of the dominant strategy for the player, or None if no dominant strategy exists.
    """
    num_strategies = len(matrix)
    for i in range(num_strategies):
        is_dominant = True
        for j in range(num_strategies):
            if matrix[i] < matrix[j]:
                is_dominant = False
                break
        if is_dominant:
            return i
    return None

# Example usage
player1_payoffs = [ [3, 1], [2, 0] ]  # Payoff matrix for Player 1
player2_payoffs = [ [2, 3], [1, 0] ]  # Payoff matrix for Player 2

# Find dominant strategies for both players
dominant_strategy_player1 = find_dominant_strategy(player1_payoffs)
dominant_strategy_player2 = find_dominant_strategy(player2_payoffs)

# Print the results
if dominant_strategy_player1 is not None:
    print("Player 1's dominant strategy is:", dominant_strategy_player1)
else:
    print("Player 1 has no dominant strategy.")

if dominant_strategy_player2 is not None:
    print("Player 2's dominant strategy is:", dominant_strategy_player2)
else:
    print("Player 2 has no dominant strategy.")
