"""
    Yandex Contest
    Summer Internship 2021
    A. Andrew and Acid
"""


def logic():
    number = int(input())
    while 1 <= number <= 100000:
        volume = list(map(int, input().split()))

        for i in volume:
            while 1 <= i <= 1000000000:

                count = 0
                if volume == sorted(volume):
                    if len(volume) == number:
                        unique_volume = sorted(list(set(volume)))
                        unique_volume.pop()
                        for n in unique_volume:
                            count += volume[-1] - n
                        return count

                    elif len(volume) != number:
                        return -1

                else:
                    return -1
            break
        break


print(logic())
