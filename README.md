# letcode
these are some examples.


- 201 注意奇偶相与一定为偶数，如果为连续的数字，则奇数可不用考虑
- 49 此题比较简单，主要是需要掌握字符串排序，并且字典的key值可以为元组
- 56 双向实现，从正反两方面都可以考虑
- 459 代码很简单（最简单的方法是通过枚举来实现），但是自己没想到，要想知道是否有子串，可选择将两个s连在一起，移除第一个和最后一个字符，如果还能找到s，则证明其一定包含子串
- 491 递归和动态规划是我的一难点，看了别人的代码感觉会，自己写又弄不出来。在递归和动态规划一定要注意重复的问题
- 17 此题不是很难，其应属于回溯算法中较简单的一类，需提前定义数字含有的字母，且在遍历时，应该在迭代处进行字符串增加
- 332 看题解时，发现一个欧拉回路的问题（简单说一下就是从一个点出发会形成一个回路），此处可通过压栈出栈的方法来达到简单求解
- 657 这道题很简单，只需要想清楚正负相互抵消的原则
- 557 这道题很简单，理解清楚python内核函数就很容易了
- 166 这道题很绕，首先要判断乘除法相同为正，相异为负，其次就是需要记住开始循环的位置
- 841 两种方法，一种是使用dfs深度优先遍历实现，另一种方法是使用排除法进行遍历实现的，若进入过该房间，就将其设置为True，如果全都为True，则证明都进入过
- 1455 需要比对搜索字符是否为前缀
- 725 对链表的操作不是很熟悉，同时，在分割链表的时候，需要对后面的范围进行遍历
- 486 感觉这道题就是一个动态规划，找最大的组合，每个玩家都贪心选择最大的值，从这道题看出动态规划问题，自己真的还是写不来代码
- 51 之前很久没做题了，其就是被这道题打击到了，想法是对的，但是就是不知道为啥写不对，感觉很难受呀
- 637 今天做了这棵树，足以看出自己的基础多么的薄弱，明明很简单的问题，想了很久也没有答案
- 79 这道深度优先是自己没有遇到过的题目，其主要有两个经典之处，第一个是通过visited来判断是否访问，第二个是一个回退机制，如果当前值不可行可回退到最初状态
- 94 首先中序遍历是本科就已经写过的，有些忘了怎么弄的，但是回顾了一下思想左中右还是能回忆起来，刷完这道题去看了一下别人的题解，直接递归那个函数，哎哟，真是觉得变态啊，什么都能想
- 37 这道题很难，如果不看解析，我可能都不知道怎么下手，他通过记录的方式保存了当前行列块存在的数字，在我们进行遍历是要保证数字不应等于当前数字
- 226 这道题很简单，就有一个递归翻转的思想就能很轻松的做出来
- 572 刚开始想简单方法去了，后来回头想用same_tree的方法就被局限了，此题最大的难点就是python在return时是返回最内层然后迭代嵌套返回的
- 47 就是将其所有可能都列出来，然后去除重复。
- 78 这道题其实和全排列类似，都是将所有可能列出来，其思想也很简单，子集一般都是2^n，可以通过此来验证
- 538 确实没把这道题看的很懂，但根据多次测试和看了一下攻略，其指出是反转的左中右结构
- 404 这道题把我搞的很难受呀，自己想出来怎么做，但是因为有一点想差了，在判断时应该用and而不是or
- 968 这道题很难，做的时候也是顺着别人的思路去理，下来又看了很久
- 617 太菜啦，这没想到，但是长见识啦
- 501 今天来了一个超级简单的题，很美滋滋，昨天晚上又被685打击到啦，自己想了一个办法怎么都不达标，原因是关于图的题，自己完全没有考虑出度和入度之间的关系，今天晚上再想想
- 106 大概知道需要分解，但是没有想到用递归分解，确实有点憨，算法思想还不根深蒂固啊
- 113 这道题主要是要掌握tree与stack的结合使用，在遍历后选择出入栈
- 235 二叉搜索树的性质是解题的关键部分，同时要了解若该值一大一小，当前节点肯定为其根节点
- 117 思路还是比较简单，就是递归层次，然后将同一层的数据连接起来
- 145 二叉树的后序遍历比较简单，今天很轻松
- 701 难度还是不大，还是老规矩，要了解二叉搜索树是什么，然后我觉得我的方法有点笨，应该直接将其分支赋值就行了，就如我注解所示
- lcp19 这道题难得很大，需要考虑的东西很多，昨天为了保持连刷，没有考虑的很清楚
- 771 这道题python配合counter函数就非常简单了，完全没有难度
- 868 思路简单，当时做题以为有简便方法就一直在那里想，结果最后还是按照最开始的思路来实施的
- 1 二刷这道题，首先确保只有两个数，所以需要考虑的因素就很少了
- 2 同样的二刷，然后看了下之前的解题思路做上的，感觉老了呀，知道意思，但总想着简单的方法来实现，最后去看题解那里，都说这几天的题是梦开始的地方，哈哈