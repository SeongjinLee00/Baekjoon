#include <bits/stdc++.h>

using namespace std;

int main()
{
    for(int i=0;i<4;i++)
    {
        int x1,x2,x3,x4,y1,y2,y3,y4;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        scanf("%d%d%d%d",&x3,&y3,&x4,&y4);
        if(x2<x3 || x1>x4 || y1>y4 || y2<y3 || x2==x3 && y3>y2 || y1>y4 || x2==x1 && y3>y2 || y1>y4 || y2==y3 && x3>x2 || x1>x4 || y2==y3 && x3>x2 || x1>x4)
            printf("d\n");
        else if((x2==x3 || x1==x4) && (y1==y4 || y2==y3))
            printf("c\n");
        else if(x2==x3 || x1==x4 || y2==y3 || y1==y4)
            printf("b\n");
        else
            printf("a\n");
    }
    return 0;
}
