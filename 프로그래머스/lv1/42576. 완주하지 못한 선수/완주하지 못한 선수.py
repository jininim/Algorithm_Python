import collections

def solution(participant, completion):
    participant_count = collections.Counter(participant)
    completion_count = collections.Counter(completion)

    
    for name, count in participant_count.items():
        if count != completion_count[name]:
            return name