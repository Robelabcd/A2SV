class Solution(object):
    def countStudents(self, students, sandwiches):
        
        zeros = students.count(0)
        ones = len(students) - zeros
        for sandwich in sandwiches:
            if sandwich == 0:
                if zeros > 0:
                    zeros -= 1
                else:
                    break
            elif sandwich == 1:
                if ones > 0:
                    ones -= 1
                else:
                    break
        return zeros + ones   