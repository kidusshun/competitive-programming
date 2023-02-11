def totalFruit(fruits):
    max1=0
    max2=0
    for ind in range(len(fruits)):
        if fruits.count(fruits[ind]) >=max1 and fruits[ind] not in fruits[:ind]:
            max2=max1
            max1=fruits.count(fruits[ind])
        elif fruits.count(fruits[ind])>max2 and fruits[ind] not in fruits[:ind]:
            max2=fruits.count(fruits[ind])
    return max1 + max2
totalFruit([3,3,3,1,2,1,1,2,3,3,4])