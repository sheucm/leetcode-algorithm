class Solution:

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
            
            if source == target:
                return 0
            
            m = {}
            for bus, route in enumerate(routes):
                for stop in route:
                    if not m.get(stop):
                        m[stop] = set()    
                    m[stop].add(bus)
            


            queue = []
            visits = set()
            for bus in m[source]:
                queue += routes[bus]
                visits.add(bus)

            num = 1
            while queue:
                if target in queue:
                    return num

                # Insert next stops into queue
                l = len(queue)
                for i in range(l):
                    stop = queue.pop(0)
                    for bus in m[stop]:
                        if bus in visits:
                            continue
                        visits.add(bus)
                        queue.extend(routes[bus])
                num += 1

            return -1


