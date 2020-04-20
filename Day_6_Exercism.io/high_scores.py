# Manage a game player's High Score list.
# Your task is to build a high-score component of the classic Frogger game, one of the highest selling 
# and addictive games of all time, and a classic of the arcade era. Your task is to write methods that return the highest
# score from the list, the last added score and the three highest scores.

def highest(scores):
    return max(scores)

def last_added(scores):
    return scores[-1]


def top_3(scores):
    scores.sort(reverse=True)
    return scores[:3]

if __name__ == "__main__":
    # TEST CASES
    # scores = [2, 3, 1, 5, 4]
    # scores = [250, 320, 112, 569, 440]
    scores = [380, 491, 722, 830, 209]

    # Get the highest score within the list of scores:
    print("highest score:", highest(scores)) # Expected score: 830

    # Get the most recently added score in the list of scores:
    print("last_added score:", last_added(scores)) # Expected score: 209

    # get the 3 highest scores within the list of scores:
    print("top_3 scores:", top_3(scores)) # Expected score: 830, 722, 491