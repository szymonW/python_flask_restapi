def create_games(names):
    temp_names = names.copy()
    temp_games = {}
    games = {}
    iter_games = 1
    for i in names:
        temp_names.pop(0)
        for j in temp_names:
            temp_games[iter_games] = {"p1": i, "p2": j, "winner": ""}
            iter_games += 1

    iter_games = 1
    pro_iter_games = 1
    rev_iter_games = 0
    for mix_games in range(len(temp_games.keys())):
        if (mix_games+1) % 2:
            games[mix_games+1] = temp_games[pro_iter_games]
            pro_iter_games += 1
        else:
            games[mix_games+1] = temp_games[len(temp_games.keys())-rev_iter_games]
            rev_iter_games += 1
        iter_games += 1

    return games


if __name__ == "__main__":
    x = create_games(["player_1", "player_2", "player_3", "player_4", "player_5"])
    for i in x:
        print(f"{i}: {x[i]}")
