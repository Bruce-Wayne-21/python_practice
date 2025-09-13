using System;

namespace leetcode_practice
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var solution = new Solution();

            try
            {
                // Capture and display the result
                double result = solution.FindMedianSortedArrays(new int[] { 1, 3 }, new int[] { 2 });
                Console.WriteLine($"Median: {result}");
                Console.WriteLine("Hello, World!");

                // Keep console open to see output
                Console.WriteLine("Press any key to exit...");
                Console.ReadKey();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Console.ReadKey();
            }
        }

        public class Solution
        {
            public double FindMedianSortedArrays(int[] nums1, int[] nums2)
            {
                if (nums1.Length > nums2.Length) return FindMedianSortedArrays(nums2, nums1);

                int len1 = nums1.Length, len2 = nums2.Length;
                int imin = 0, imax = len1, halfLen = (len1 + len2 + 1) / 2;

                while (imin <= imax)
                {
                    int i = (imin + imax) / 2;
                    int j = halfLen - i;

                    int maxLeft1 = (i == 0) ? int.MinValue : nums1[i - 1];
                    int minRight1 = (i == len1) ? int.MaxValue : nums1[i];
                    int maxLeft2 = (j == 0) ? int.MinValue : nums2[j - 1];
                    int minRight2 = (j == len2) ? int.MaxValue : nums2[j];

                    if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1)
                    {
                        return (len1 + len2) % 2 == 0
                            ? (Math.Max(maxLeft1, maxLeft2) + Math.Min(minRight1, minRight2)) / 2.0
                            : Math.Max(maxLeft1, maxLeft2);
                    }
                    else if (maxLeft1 > minRight2)
                    {
                        imax = i - 1;
                    }
                    else
                    {
                        imin = i + 1;
                    }
                }

                throw new ArgumentException("Input arrays are not sorted or have invalid lengths.");
            }
        }
    }
}