import java.util.Scanner;

public class Main {
    static Node[] n;
    static int[] t;
    static int SUM;

    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        int T = cin.nextInt();
        for (int p = 1; p <= T; p++) {
            int tmp = 0;
            int N = cin.nextInt();
            n = new Node[4 * N];
            t = new int[N + 1];
            for (int i = 1; i <= N; i++)
                t[i] = cin.nextInt();
            make(1, N, 0);
            while (true) {
                String str = cin.next();
                if ("End".equals(str))
                    break;
                int i = cin.nextInt();
                int j = cin.nextInt();
                if ("Query".equals(str)) {
                    SUM = 0;
                    if (tmp == 0) {
                        System.out.println("Case " + p + ":");
                        tmp++;
                    }
                    query(i, j, 0);
                    System.out.println(SUM);
                } else if ("Add".equals(str))
                    add(i, j, 0);
                else // Sub
                    sub(i, j, 0);
            }
        }
    }

    static void make(int l, int r, int idx) { // l为左端点，r为右端点，idx为数组下标
        n[idx] = new Node();
        n[idx].l = l;
        n[idx].r = r;
        if (l == r) // 已经是叶节点了
            n[idx].sum = t[l]; // 也可以是t[r]
        else {
            make(l, (l + r) >> 1, (idx << 1) + 1); // 递归构造左子树
            make(((l + r) >> 1) + 1, r, (idx << 1) + 2); // 递归构造右子树
            n[idx].sum = n[(idx << 1) + 1].sum + n[(idx << 1) + 2].sum;
            // 父节点值等于子节点值之和，线段树分成两段
        }
    }

    static void add(int i, int j, int idx) { // 第i个营地增加j个人
        // 从根节点不断往下更改，只要包含点i的线段都增加数量j
        n[idx].sum += j;
        if (n[idx].l == i && n[idx].r == i) // 如果找到i的叶子节点则停止
            return;
        if (i <= ((n[idx].l + n[idx].r) >> 1)) // 如果i在线段左边
            add(i, j, (idx << 1) + 1); // 递归进入左子节点
        else // 如果i在线段右边
            add(i, j, (idx << 1) + 2); // 递归进入右子节点
    }

    static void sub(int i, int j, int idx) { // 第i个营地减少j个人
        // 从根节点不断往下更改，只要包含点i的线段都减少数量j
        n[idx].sum -= j;
        if (n[idx].l == i && n[idx].r == i) // 如果找到i的叶子节点则停止
            return;
        if (i <= ((n[idx].l + n[idx].r) >> 1)) // 如果i在线段左边
            sub(i, j, (idx << 1) + 1); // 递归进入左子节点
        else
            sub(i, j, (idx << 1) + 2); // 递归进入右子节点
    }

    static void query(int l, int r, int idx) { // 初始idx为0，即从根节点开始查找
        if (l <= n[idx].l && r >= n[idx].r)
            SUM += n[idx].sum;
        else {
            int mid = (n[idx].l + n[idx].r) >> 1;
            if (r <= mid) // 要查询的区间在左边
                query(l, r, (idx << 1) + 1);
            else if (l > mid) // 要查询的区间在右边
                query(l, r, (idx << 1) + 2);
            else { // 要查询的区间在中间，分段查询，左右都查
                query(l, r, (idx << 1) + 1);
                query(l, r, (idx << 1) + 2);
            }
        }
    }
}

class Node {
    int l, r, sum;
}