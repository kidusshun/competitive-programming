class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            files = path.split()
            directory = files[0]
            for f in files[1:]:
                words = f.split("(")
                d[words[1][:-1]].append(f"{files[0]}/{words[0]}")

        return [val for val in d.values() if len(val)>1]
            