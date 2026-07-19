class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start_x, start_y = 0, 0
        cells_visited = set()
        for move in path:
            cells_visited.add((start_x, start_y))
            match move:
                case "N":
                    start_y += 1
                case "S":
                    start_y -= 1
                case "E":
                    start_x += 1
                case _:
                    start_x -= 1

            if (start_x, start_y) in cells_visited:
                return True
            else:
                pass

        return False            
        