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
            var result2 = solution.RomanToInt("MCMXCIV");
            Program.Solution.oddnumber();

            Console.WriteLine(result2);
            Console.WriteLine(); // For a new line at the end
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        public class Solution
        {
            private char nextChar;

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

            private static int CalcScale(char nextChar, char higher, char mid)
            {
                return (nextChar == higher || nextChar == mid) ? -1 : 1;
            }

            public int RomanToInt(string s)
            {
                try
                {
                    int result = 0;

                    for (int n = 0; n < s.Length; n++)
                    {
                       char nextChar = (n + 1 < s.Length) ? s[n + 1] : '\0';

                        switch (s[n])
                        {
                            case 'M':
                                result += 1000;
                                break;
                            case 'D':
                                result += 500;
                                break;
                            case 'C':
                                result += 100 * CalcScale(nextChar, 'M', 'D');
                                break;
                            case 'L':
                                result += 50;
                                break;
                            case 'X':
                                result += 10 * CalcScale(nextChar, 'C', 'L');
                                break;
                            case 'V':
                                result += 5;
                                break;
                            case 'I':
                                result += 1 * CalcScale(nextChar, 'X', 'V');
                                break;
                        }
                    }

                    return result;
                }
                catch (Exception ex)
                {
                    throw new Exception("An error occurred while converting Roman numeral to an integer.", ex);
                }
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

           public string  longcommanPrefix(string[] strs)
           {
                string prefix = strs[0];
                for (int i = 1; i < strs.Length; i++)
                {

                }
                return prefix;
           }

            public static void oddnumber()
            {
                int n = 99; 
                for (int i=0; i<n; i++)
                {
                    if(i % 2 != 0)
                    {
                         if (i < 99)
                            Console.Write("Odd number"+  i + ", ");
                        else
                            Console.Write(i);
                    }
                    else if( i % 2 == 0)
                    {
                        Console.WriteLine("Even number" + i);
                    }
                }
            }


        }
    }
}