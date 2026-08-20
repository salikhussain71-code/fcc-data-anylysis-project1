def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    
    # First move - start with Rock
    if prev_play == "":
        return "R"
    
    # Strategy 1: Beat what opponent played last time
    # R beats S, S beats P, P beats R
    last_play = opponent_history[-2] if len(opponent_history) > 1 else "R"
    
    if last_play == "R":
        return "P"
    if last_play == "P":
        return "S"
    if last_play == "S":
        return "R"
    
    return "R"

# This is for testing - FCC will handle the bots
if __name__ == "__main__":
    print("RPS player ready")