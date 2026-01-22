from collections import defaultdict


def groupAnagrams(strs):
        mp = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            mp[key].append(word)
        for key,values in mp.items():
              print(key,values)
        print(mp)      
        return list(mp.values())
        
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))    