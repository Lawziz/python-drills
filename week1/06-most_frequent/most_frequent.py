
def most_frequent(items):
    if len(items) == 0:
        return None

    frequence = {}
    highest_count = 0
    most_freq_num = None

    for number in items:
        if number in frequence:
            frequence[number] += 1
        else:
            frequence[number] = 1

        if frequence[number] >= highest_count:
            highest_count = frequence[number]           
            most_freq_num = number

    return most_freq_num

print(most_frequent([3, 4, 4, 3, 5]))

