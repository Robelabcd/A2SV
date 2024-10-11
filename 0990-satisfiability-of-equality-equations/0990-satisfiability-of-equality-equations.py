class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        class UnionFind:
            def __init__(self):
                self.parent = {}

            def find(self, item):
                if item != self.parent.setdefault(item, item):
                    self.parent[item] = self.find(self.parent[item])
                return self.parent[item]

            def union(self, item1, item2):
                root1 = self.find(item1)
                root2 = self.find(item2)
                if root1 != root2:
                    self.parent[root1] = root2

        uf = UnionFind()
        
        for equation in equations:
            if equation[1:3] == "==":
                uf.union(equation[0], equation[3])
        
        for equation in equations:
            if equation[1:3] == "!=":
                if uf.find(equation[0]) == uf.find(equation[3]):
                    return False
        
        return True
