class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        length = len(profits)

        projects = sorted([(capital[i], profits[i]) for i in range(length)], key = lambda x: x[0])
        available_projects = sorted([project[1] for project in projects if project[0] <= w])
        del projects[:len(available_projects)]

        for _ in range(k):
            if not available_projects:
                break
            w += available_projects.pop()[1]

            newly_available_projects = [project[1] for project in projects if project[0] <= w]

            if newly_available_projects:
                available_projects.extend(newly_available_projects)
                available_projects = sorted(available_projects)
                del projects[:len(newly_available_projects)]

        return w
        