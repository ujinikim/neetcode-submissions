public class Solution {
    public List<List<int>> CombinationSum2(int[] candidates, int target) {
        var res = new List<List<int>>(); 
        var set = new HashSet<string>();
        Array.Sort(candidates);
        RecursiveSum(0, candidates, target, res, new List<int>(), set);
        return res;
    }

    public void RecursiveSum(int start, int[] cand, int target, List<List<int>> result, List<int> curComb, HashSet<string> set)
    {
        if(target < 0)
        {
            return;
        }
        else if(target == 0)
        {
            if(set.Add(string.Join("", curComb)))
            {
                result.Add(new List<int>(curComb));
            }
            return;
        }
        else
        {
            for(int i = start; i < cand.Length; i++)
            {
                var curCombNew = new List<int>(curComb);
                curCombNew.Add(cand[i]);
                RecursiveSum(i + 1, cand, target - cand[i], result, curCombNew, set);
                curCombNew.RemoveAt(curCombNew.Count - 1);
            }
        }
    }
}
