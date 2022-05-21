# Breadth-First-Search-BFS-Algorithm

#include <iostream>
#include <map>
#include <queue>
#include <list>
 
using namespace std;
 
template <typename T>
class example
{
    map<T, list <pair <T, int>>> l; // adjacency list
public:
    void add_edge(T node, T neighbour, int distance = 1, bool is_directed = false)
    {
        l[node].push_back(make_pair(neighbour, distance));
 
        if(!is_directed)
            l[neighbour].push_back(make_pair(node, distance));
    }
 
    void print_example()
    {
      for(auto p : l)
        { 
            T node = p.first;
            list <pair <T, int>> neighbour = p.second;
 
            cout << "Neighbours of: " << node << " are:\n";
 
            for(auto nbr : neighbour)
            {
                T dest = nbr.first;
                int distance = nbr.second;
 
                cout << "Neighbour: " << dest << " " << " Distance: "<< distance << endl;
            }
            cout << endl;
        }
    }
 
    void bfs(T src)
    {
        map <T, bool> visited;
 
        queue <T> q;
        q.push(src);
        visited[src] = true;
 
        while(!q.empty())
        {
            T node = q.front();
            q.pop();
            cout << node << endl;
 
            for(pair <T, int> nbr : l[node])
            {
               
                if(!visited[nbr.first])
                {
                    q.push(nbr.first);
                    visited[nbr.first] = true;
                }
            }
        }
 
        return;
    }
};
 
 
 
int main()
{
    Graph <string> g;
     
    g.add_edge("Delhi", "shimla");
    g.add_edge("Delhi", "rishikesh");
    g.add_edge("Delhi", "lucknow");
    g.add_edge("Shamli", "pithoragarh");
    g.add_edge("Shamli", "ranikhet");
    g.add_edge("Jaipur", "Bikaner");
    g.add_edge("Udaipur", "Jaipur");
    g.add_edge("Uttarlai", "Jaipur");
    g.add_edge("Jaipur", "Jodhpur");
    g.add_edge("Mumbai", "Jaipur");
 
    g.bfs("Delhi");
 
    return 0;
}
