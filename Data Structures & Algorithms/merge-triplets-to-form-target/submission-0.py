class Solution:
    def mergeTriplets(
        self,
        triplets: List[List[int]],
        target: List[int]
    ) -> bool:

        found_first = False
        found_second = False
        found_third = False

        for triplet in triplets:
            first = triplet[0]
            second = triplet[1]
            third = triplet[2]

            # Skip this triplet if it would make
            # any position exceed the target.
            if first > target[0]:
                continue

            if second > target[1]:
                continue

            if third > target[2]:
                continue

            # This triplet is safe to use.
            # Check which target positions it can contribute.
            if first == target[0]:
                found_first = True

            if second == target[1]:
                found_second = True

            if third == target[2]:
                found_third = True

        return found_first and found_second and found_third