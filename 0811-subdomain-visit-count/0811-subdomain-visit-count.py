class Solution(object):
    def subdomainVisits(self, cpdomains):
        count = collections.Counter()
        for cpdomain in cpdomains:
            n, domain = cpdomain.split()
            count[domain] += int(n)
            for i in range(len(domain)):
                if domain[i] == ".":
                    count[domain[i + 1:]] += int(n)
        return ["%d %s" % (count[s], s) for s in count]
        