# def sum_pairs(ints, s):
#     result = [ints[0], ints[1]]
#     for i in range(len(ints)):
#         result = [ints[i]]
#         for j in range(len(ints)):
#             if ints[i] + ints[j] == s and i != j:
#                 result.append(ints[j])
#                 return result
#     if len(result) == 1:
#         return None


def sum_pairs(ints, s):
    mem_log = set()
    for int in ints:
        int2 = s - int
        if int2 in mem_log:
            return [int2, int]
        mem_log.add(int)
        

        

print(sum_pairs([20, -13, 40], -7))
