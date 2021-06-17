class CourseSchedule:

    def __init__(self, num_courses, prerequisites):
        self.num_courses = num_courses
        self.prerequisites = prerequisites
        self.graph = self.create_graph()

    def create_graph(self):
        graph = {}
        for course in range(self.num_courses):
            graph[course] = []
        for prerequisite, dependent in self.prerequisites:
            graph[prerequisite].append(dependent)
        return graph

    def can_finish(self):
        seen = set()
        stack = []

        for course in self.graph:
            if course not in seen:
                if self.has_cycle(course, stack, seen): return False

        return True

    def has_cycle(self, course, stack, seen):
        seen.add(course)
        stack.append(course)

        for dependent in self.graph[course]:
            if dependent not in seen:
                if self.has_cycle(dependent, stack, seen):
                    return True
            elif dependent in stack:
                return True

        stack.pop()

        return False