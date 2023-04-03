from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(int)
    
    for num, genre in enumerate(genres) :
        genres_dict[genre] += plays[num]
    genres_dict = sorted(genres_dict.items(), key=lambda x:x[1], reverse = True)
    
    for genre_dict, _ in genres_dict :
        box = []
        for num in range(len(genres)) :
            if genres[num] == genre_dict :
                box.append((plays[num], num))
                
        box.sort(reverse=True, key = lambda x:(x[0], -x[1]))

        if len(box) == 1 :
            answer.append(box[0][1])
        else :
            answer.append(box[0][1])
            answer.append(box[1][1])
        
    return answer