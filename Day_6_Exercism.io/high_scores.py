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
    scores = [2, 3, 1, 5, 4]
    print("highest score:", highest(scores))
    print("scores", scores)
    print("last_added score:", last_added(scores))
    print("top_3 scores:", top_3(scores))