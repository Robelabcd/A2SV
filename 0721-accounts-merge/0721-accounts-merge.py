class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)

        email_to_name = dict()

        for account in accounts:
            name = account[0]
            emails = account[1:]

            prev = None
            for email in emails:
                email_to_name[email] = name
                if email in graph:
                    if prev is None:
                        prev = email
                    else:
                        graph[prev].append(email)
                        graph[email].append(prev)
                else:
                    graph[email] = []
                    if prev:
                        graph[prev].append(email)
                        graph[email].append(prev)
                    prev = email
        visited = set()
        res = []
        for account in accounts:
            emails = account[1:]
            for email in emails:
                if email in visited:
                    continue

                stack = [email]
                identity = email_to_name[email]
                visited.add(email)
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            stack.append(nei)
                            visited.add(nei)

                component.sort()
                res.append([identity] + component)
        return res
