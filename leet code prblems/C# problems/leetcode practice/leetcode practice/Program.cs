using System;

namespace leetcode_practice
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //for (int i = 1; i <= 99; i += 2)
            //{
            //    if (i < 99)
            //        Console.Write(i + ", ");
            //    else
            //        Console.Write(i);
            
            var solution = new Solution();
            var result = solution.LengthOfLongestSubstring("abcabcbb");
            Console.WriteLine(result);

            Console.WriteLine(); // For a new line at the end
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        public class Solution
        {
            public int LengthOfLongestSubstring(string s)
            {
                int n = s.Length;
                int maxLen = 0;

                for (int i = 0; i < n; i++)
                {
                    var set = new HashSet<char>();
                    for (int j = i; j < n; j++)
                    {
                        if (set.Contains(s[j]))
                            break;
                        set.Add(s[j]);
                        maxLen = Math.Max(maxLen, j - i + 1);
                    }
                }

                return maxLen;
            }

            private int lenthofSubstr(string ss)
            {
                int length = ss.Length;
                int maxlenght = 0;

                for (int i = 0; i < length; i++)
                {
                    var hashset = new HashSet<char>();
                    for (int j = i; j < length; j++)
                    {
                        if (hashset.Contains(ss[j]))
                            break;
                        hashset.Add(ss[j]);
                        maxlenght = Math.Max(maxlenght, j - i + 1);
                    }


                }

                return maxlenght;
            }
        }
    }
}