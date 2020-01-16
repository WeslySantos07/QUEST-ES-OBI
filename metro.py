#include <bits/stdc++.h>
#define pb push_back
using namespace std;
int n,m;

vector<int> G[100100][2];
int dist[100100][2];
pair<int,int> dfs(int u,int p,int k){
	int v = u;
	pair<int,int> sz = {1,u};
	for(int &w : G[u][k]){
		if(w==p){
			continue;
		}
		pair<int,int> next = dfs(w,u,k);
		if(sz.first < next.first + 1){
			sz = next;
			sz.first ++;
		}
	}
	return sz;
}
pair<int,int> find_diameter(int graph){
	int w = dfs(1,0,graph).second;
	int ch1 = w, ch2 = dfs(w,0,graph).second;
	return {ch1,ch2};
}
int get_dist(int u,int k,int graph){
	for(int &v : G[u][graph]){
		if(dist[v][k] == -1){
			dist[v][k] = dist[u][k] + 1;
			get_dist(v,k,graph);
		}
	}
}
int get_vertex(int graph){
	pair<int,int> diameter = find_diameter(graph);
	//cout << graph << " : " << diameter.first << " " << diameter.second << endl;
	memset(dist,-1,sizeof dist);
	dist[diameter.first][0] = 0;
	dist[diameter.second][1] = 0;
	get_dist(diameter.first,0,graph);
	get_dist(diameter.second,1,graph);
	int w = 1;
	for(int i=2;i<=(graph==1 ? m : n);i++){
		int x = max(dist[i][0],dist[i][1]);
		int y = max(dist[w][0],dist[w][1]);
		//cout << i << " " << w << " "  << x << " " << y << endl;
		if(x < y){
			w = i;
		}
	}
	return w;
}
int main() {
    cin >> n >> m;
	for(int i=1;i<n;i++){
		int a,b;
		cin >> a >> b;
		G[a][0].pb(b);
		G[b][0].pb(a);	
	}
	for(int i=1;i<m;i++){
		int a,b;
		cin >> a >> b;
		G[a][1].pb(b);
		G[b][1].pb(a);	
	}
	int x = get_vertex(0);
	int y = get_vertex(1);
	cout << x << " " << y << endl;
}
