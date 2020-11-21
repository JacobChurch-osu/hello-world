def mean(lyst):
    if not lyst:
        return 0
    total = 0
    for num in lyst:
        total += num
    return total / len(lyst)
def median(lyst):
    if not lyst:
        return 0
    samples = sorted(lyst.copy())
    if len(samples) % 2 == 1:
        return samples[int(len(samples) / 2)]
    else:
        return (samples[int(len(samples) / 2)] + samples[int(len(samples) / 2) - 1]) / 2
def mode(lyst):
    if not lyst:
        return 0
    result = lyst[0]
    count = 0
    for num in lyst:
        if lyst.count(num) >= count:
            count = lyst.count(num)
            result = num
    return result
def main():
   userList = [8, 9, 9, 2, 6, 14, 1, 3, 6, 9]
   print('List:', userList)
   print('Mode:', mode(userList))
   print('Median:', median(userList))
   print('Mean:', mean(userList))
main()
