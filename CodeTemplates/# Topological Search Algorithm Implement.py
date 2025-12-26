# Topological Search Algorithm Implementation
# This script implements a topological search algorithm to find a path in a directed acyclic graph


from collections import defaultdict, deque

"""
Find valid course order (topological sort) given prerequisites.

Think: Keep taking courses with no prerequisites, remove them, repeat.


"""


def findOrder(numCourses, prerequisites):
    # Step 1: Count prerequisites for each course (In degree)
    in_degree = [0] * numCourses

    # Step 2: build Graph
    graph = defaultdict(list)

    for course, prereq in prerequisites:
        graph[prereq].append(course) # prereq unlocks course
        in_degree[course] += 1 # Course needs one more prereq


    #Step 3: Find starting courses (no prereqs)
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    # step 4 process courses one by one 
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1 # one less prereq 

            if in_degree[next_course] == 0:
                queue.append(next_course)

    if(len(result) == numCourses):
        return result
    else:
        return []
    
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # Possible outputs: [0,1,2,3] or [0,2,1,3]
print(findOrder(2, [[1,0],[0,1]]))  # Output: [] (cycle detected)