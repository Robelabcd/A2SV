class ListNode:
    def __init__(self, val="", prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.browser.next = ListNode(url, self.browser)
        self.browser = self.browser.next
        

    def back(self, steps: int) -> str:
        while self.browser.prev and steps > 0:
            self.browser = self.browser.prev
            steps -= 1

        return self.browser.val
        

    def forward(self, steps: int) -> str:
        while self.browser.next and steps > 0:
            self.browser = self.browser.next
            steps -= 1

        return self.browser.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)