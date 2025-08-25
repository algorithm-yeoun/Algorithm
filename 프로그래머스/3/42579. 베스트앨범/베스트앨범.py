def solution(genres, plays):
    answer = []
    genres_dict={}
    
    for i in range(len(genres)):
        genres_dict.setdefault(genres[i], []).append((plays[i], i))

    total_plays = {genre: sum(play for play, _ in play_list)
                   for genre, play_list in genres_dict.items()}

    sorted_genres = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        sorted_list = sorted(genres_dict[genre], key=lambda x: (-x[0], x[1]))
        answer.extend(idx for _, idx in sorted_list[:2])

    return answer

# description
    # 1. 장르별로 (재생 수, 인덱스) 쌍 저장
    # 2. 장르별 총 재생수 계산
    # 3. 장르: 총 재생수 내림차순 정렬
    # 4. 장르 내 재생수 내림차순, 재생수 같으면 인덱스 오름차순로 인덱스만 결과리스트에 저장