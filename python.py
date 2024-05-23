from queue import Queue


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, c):
        # дуга: [конечная вершина, поток, пропусканя способность, индекс обратной дуги]
        forward_edge = list([v, 0, c, len(self.adj[v])])
        backward_edge = list([u, 0, 0, len(self.adj[u])])

        self.adj[u].append(forward_edge)
        self.adj[v].append(backward_edge)


class Dinic:
    def __init__(self, graph):
        self.graph = graph
        self.levels = [0 for _ in range(graph.num_vertices)]

    def BFS_levels(self, s, t):
        for i in range(self.graph.num_vertices):
            self.levels[i] = -1
        self.levels[s] = 0

        queue = Queue()
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            # Смотрим все достижимые из u вершины
            for v, flow, c, _ in self.graph.adj[u]:
                # Если v еще не пройдена и ребро не насыщеное
                if self.levels[v] < 0 and flow < c:
                    self.levels[v] = self.levels[u] + 1
                    queue.put(v)

        return self.levels[t] >= 0

    def DFS_flow(self, u, flow, t, visited):
        if u == t:
            return flow

        # пока есть непройденные дуги исходящие из u
        while visited[u] < len(self.graph.adj[u]):
            v, e_flow, c, rev = self.graph.adj[u][visited[u]]
            if self.levels[v] == self.levels[u] + 1 and e_flow < c:
                # c_f = c - e_flow
                curr_flow = min(flow, c - e_flow)
                decent_flow = self.DFS_flow(v, curr_flow, t, visited)

                if decent_flow > 0:
                    # по прямой дуги добавляем поток
                    self.graph.adj[u][visited[u]][1] += decent_flow
                    # по обратной вычитаем
                    self.graph.adj[v][rev][1] -= decent_flow

                    return decent_flow

            visited[u] += 1

        return 0

    def max_flow(self, s, t):
        if s == t:
            raise ValueError()

        total = 0
        while self.BFS_levels(s, t):
            visited = [0 for _ in range(self.graph.num_vertices)]
            while True:
                flow = self.DFS_flow(s, float('inf'), t, visited)
                if flow == 0:
                    break
                total += flow

        return total


def main():
    num_teams = int(input())
    scores = list([int(i) for i in input().split()])
    num_games = int(num_teams * (num_teams - 1) / 2)  # what if float
    num_vertices = 1 + num_games + num_teams + 1
    graph = Graph(num_vertices)
    for v in range(1, num_games + 1):
        graph.add_edge(0, v, 3)
    game_v = 1
    for team1_v in range((num_games + 1), (num_games + 1) + num_teams - 1):
        for team2_v in range(team1_v + 1, (num_games + 1) + num_teams):
            graph.add_edge(game_v, team1_v, 3)
            graph.add_edge(game_v, team2_v, 3)
            game_v += 1
    for v_team in range(num_teams):
        graph.add_edge((num_vertices - 1) - num_teams + v_team, (num_vertices - 1), scores[v_team])
    total_score = 3 * num_teams * (num_teams - 1) / 2
    dinic = Dinic(graph)
    max_flow = dinic.max_flow(0, (num_vertices - 1))

    if max_flow != total_score:
        print('INCORRECT')
        return

    print('CORRECT')
    for v in range(1, num_games + 1):
        edge1 = graph.adj[v][1]
        edge2 = graph.adj[v][2]
        team1 = edge1[0] - num_games
        team2 = edge2[0] - num_games
        score1 = edge1[1]
        score2 = edge2[1]
        if score1 > score2:
            if score2 == 1:
                match_result = '>='
            else:
                match_result = '>'
        else:
            if score1 == 1:
                match_result = '<='
            else:
                match_result = '<'
        print(team1, match_result, team2)


if __name__ == '__main__':
    main()
