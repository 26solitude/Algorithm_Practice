def get_melon_best_album(genre_array, play_array):
    total_play_dict = {}
    total_index_play_dict = {}

    n = len(play_array)

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in total_play_dict:
            total_play_dict[genre] = play
            total_index_play_dict[genre] = [[i, play]]
        else:
            total_play_dict[genre_array[i]] += play_array[i]
            total_index_play_dict[genre].append([i, play])

    sorted_play_dict = dict(sorted(total_play_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_play_dict)

    ans = []
    for genre in sorted_play_dict:
        sorted_index_play_dict = dict(sorted(total_index_play_dict[genre], key=lambda item: item[1], reverse=True))
        count = 0
        for index in sorted_index_play_dict:
            if count > 1:
                break
            ans.append(index)
            count += 1

    return ans


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
      get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
      get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
                           [2000, 500, 600, 150, 800, 2500, 2000]))
