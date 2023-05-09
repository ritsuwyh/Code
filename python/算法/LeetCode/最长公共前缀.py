
#! 思路1 遇事不决先排序!!!!!!!!!!!!!! 由于已经是按字典序了 而且短的一定在前面 只需要比较头元素和尾元素即可
# class Solution {
# public:
#     string longestCommonPrefix(vector<string>& strs) {
#         if(strs.empty()) return string();
#         sort(strs.begin(), strs.end());
#         string st = strs.front(), en = strs.back();
#         int i, num = min(st.size(), en.size());
#         for(i = 0; i < num && st[i] == en[i]; i ++);
#         return string(st, 0, i);
#     }
# };
#! 思路2 想不到别的好方法 想暴力模拟的时候想想二分查找   二分查找前缀可能的长度
        
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            #! 掌握这种all+列表生成式的写法
            return all(strs[i][:length] == str0 for i in range(1, count))
#! all 函数的用法！！！！！！ 判断是否全为真  掌握！！！！
        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength #! 即使最长的话 也就是字符串里面最短的那个
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]
