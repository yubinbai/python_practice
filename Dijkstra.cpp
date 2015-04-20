/*
 * Problem: USACO Training 3.2.6
 * Author: Guo Jiabao
 * Time: 2009.4.6 10:20
 * State: Solved
 * Memo: Dijkstra + 堆
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#define MAXC 501
#define MAXN 801
#define MAXM 1451*2
#define INF 0x7FFFFFFF
using namespace std;
struct edge
{
    edge *next;
    int t, v;
} ES[MAXM];
struct HeapElement
{
    int key, value;
};
struct MinHeap
{
    HeapElement H[MAXN];
    int size;
    int Position[MAXN];
    void init()
    {
        H[size = 0].value = -INF;
    }
    void ins(int key, int value)
    {
        int i, f;
        HeapElement p = {key, value};
        for (i = ++size; p.value<H[f = i >> 1].value; i = f)
        {
            H[i] = H[f];
            Position[H[i].key] = i;
        }
        H[i] = p;
        Position[H[i].key] = i;
    }
    void decrease(int key, int value)
    {
        int i, f;
        HeapElement p = {key, value};
        for (i = Position[key]; p.value<H[f = i >> 1].value; i = f)
        {
            H[i] = H[f];
            Position[H[i].key] = i;
        }
        H[i] = p;
        Position[H[i].key] = i;
    }
    void delmin()
    {
        int i, c;
        HeapElement p = H[size--];
        for (i = 1; (c = i << 1) <= size; i = c)
        {
            if (c + 1 <= size && H[c + 1].value < H[c].value)
                c++;
            if (H[c].value < p.value)
            {
                H[i] = H[c];
                Position[H[i].key] = i;
            }
            else
                break;
        }
        H[i] = p;
        Position[H[i].key] = i;
    }
} H;
int N, M, C, EC = -1, Ans = INF;
int Cow[MAXC], sp[MAXN];
edge *V[MAXN];
inline void addedge(int a, int b, int c)
{
    ES[++EC].next = V[a];
    ES[EC].t = b; ES[EC].v = c;
    V[a] = &ES[EC];
}
void init()
{
    int i, a, b, c;
    freopen("butter.in", "r", stdin);
    freopen("butter.out", "w", stdout);
    scanf("%d%d%d", &C, &N, &M);
    for (i = 1; i <= C; i++)
        scanf("%d", &Cow[i]);
    for (i = 1; i <= M; i++)
    {
        scanf("%d%d%d", &a, &b, &c);
        addedge(a, b, c);
        addedge(b, a, c);
    }
}
void Dijkstra(int S)
{
    int i, j;
    sp[S] = 0;
    H.decrease(S, 0);
    for (i = S;;)
    {
        H.delmin();
        for (edge *k = V[i]; k; k = k->next)
        {
            if (sp[i] + k->v < sp[j = k->t])
            {
                sp[j] = sp[i] + k->v;
                H.decrease(j, sp[j]);
            }
        }
        if (H.size)
            i = H.H[1].key;
        else
            break;
    }
}
void solve()
{
    int i, j, Total;
    for (i = 1; i <= N; i++)
    {
        H.init();
        for (j = 1; j <= N; j++)
        {
            H.ins(j, INF);
            sp[j] = INF;
        }
        Total = 0;
        Dijkstra(i);
        for (j = 1; j <= C; j++)
            Total += sp[Cow[j]];
        if (Total < Ans)
            Ans = Total;
    }
}
int main()
{
    init();
    solve();
    printf("%d\n", Ans);
    return 0;
}