public class Solution {

    public string Encode(IList<string> strs) {
        for(int i = 0; i < strs.Count(); i++)
        {
            strs[i] = $"{strs[i].Length}*{strs[i]}";
        }
        return string.Join("", strs);
    }

   public List<string> Decode(string s) {
    var lst = new List<string>();
    int i = 0;
    while(i < s.Length)
    {
        int delimiterPos = s.IndexOf('*', i);
        int length = int.Parse(s.Substring(i, delimiterPos - i));
        i = delimiterPos + 1; // Move past the '*'
        lst.Add(s.Substring(i, length));
        i += length; // Move past the decoded string
    }
    return lst;
}
}
