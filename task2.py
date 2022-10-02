def warn_the_sheep(queue):
    q = queue[::-1]
    w = "wolf"
    if w == q[0]:
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {q.index(w)}! You are about to be eaten by a wolf!"
