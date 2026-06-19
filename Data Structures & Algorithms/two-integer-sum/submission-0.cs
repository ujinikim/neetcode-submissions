public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        // for(int i = 0; i < nums.Length - 1; i++)
        // {
        //     for(int j = 1; j < nums.Length; j++)
        //     {
        //         if (nums[i] + nums[j] == target)
        //         {
        //             return new int[] {i, j};
        //         }
        //     }
        // }
        // return null;

        var hash = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++)
        {
            var lookUp = target - nums[i];
            if(!hash.ContainsKey(lookUp))
            {
                hash[nums[i]] = i;
            }
            else
            {
                return new int[]{hash[lookUp], i};
            }
        }
        return null;
    }
}