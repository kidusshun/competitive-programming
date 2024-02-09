class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pfx = [0]
        n_count = 0
        y_count = customers.count("Y")
        sfx = [y_count]
        for i in range(len(customers)):
            if customers[i] == "N":
                n_count +=1
            pfx.append(n_count)
            if customers[i] =="Y":
                y_count -=1
            sfx.append(y_count)
        max_ = float("inf")
        ind = 0
        for i in range(len(sfx)):
            curr = sfx[i]+pfx[i]
            if curr < max_:
                max_ = curr
                ind = i
        return ind

