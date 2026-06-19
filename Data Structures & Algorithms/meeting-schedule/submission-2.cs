/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    public bool CanAttendMeetings(List<Interval> intervals) {
        intervals.Sort((i1, i2) => i1.Start.CompareTo(i2.Start));

        for (int i = 1; i < intervals.Count; i++) {
            Interval i1 = intervals[i - 1];
            Interval i2 = intervals[i];

            if (i1.End > i2.Start) {
                return false;
            }
        }

        return true;
    }
}
