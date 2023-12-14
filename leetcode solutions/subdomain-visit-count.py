class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdomain = defaultdict(int)
        for domain in cpdomains:
            sub_domain = domain.split(" ")
            count = sub_domain[0]
            address = sub_domain[1].split(".")
            for i in range(len(address)):
                ad = ".".join(address[i:])
                cpdomain[ad]+=int(count)
        ans = []
        for key, val in cpdomain.items():
            ans.append(f"{val} {key}")
        return ans