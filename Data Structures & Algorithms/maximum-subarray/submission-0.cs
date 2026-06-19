public class Solution {
    public int MaxSubArray(int[] nums) {
      var output = int.MinValue;
      var sum = 0;
      for(int i = 0; i < nums.Length; i++)
      {
        sum += nums[i];
        if(sum > output)
        {
            output = sum;
        }

        if (sum < 0)
        {
            sum = 0;
        }        
      }
      return output;
    }
}
