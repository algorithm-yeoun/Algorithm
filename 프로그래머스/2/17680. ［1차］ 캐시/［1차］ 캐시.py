def solution(cacheSize, cities):
    answer = 0
    cache_list=[]
    
    if not cacheSize:
        return len(cities)*5
    else:
        for city in cities:
            if len(cache_list) <= cacheSize:
                if city.lower() in cache_list:
                    cache_list.remove(city.lower())
                    answer+=1
                else:
                    if len(cache_list) == cacheSize:
                        cache_list.pop(0)
                    answer+=5
            cache_list.append(city.lower())

        return answer