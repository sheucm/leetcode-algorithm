import math
class Solution:
    def insert(self, intervals, newInterval):
        if (len(intervals) == 0):
            return [newInterval]
        elif (len(intervals) == 1):
            sorted = self._sort(intervals[0], newInterval)
            i1 = sorted[0]
            i2 = sorted[1]

            is_overlap = self._is_overlap(i1, i2)
            if (is_overlap):
                return [self._merge(i1, i2)]
            else:
                return [i1, i2]
        else:
            merged, removed_idx_list = self._find(
                intervals,
                newInterval,
                removed_list = [],
                prev_position = None
            )
            final_intervals = []
            for idx, obj in enumerate(intervals):
                if (obj[0] not in removed_idx_list):
                    final_intervals.append(obj)
            return self._join(final_intervals, merged)

    def _join(self, intervals, new_interval):
        if (not intervals or len(intervals) == 0):
            return [new_interval]
        elif (len(intervals) == 1):
            return self._sort(intervals[0], new_interval)
        elif(new_interval[0] > intervals[-1][0]):
            return intervals + [new_interval]
        
        
        left = 0
        right = len(intervals) - 1

        tgt_x = new_interval[0]
        
        behind_idx = 0
        while True:
            if (right - left == 0):
                behind_idx = right
                break
            midd_idx = math.floor((left + right) / 2)
            midd_x = intervals[midd_idx][0]
            if (tgt_x < midd_x):
                right = midd_idx
            elif (tgt_x > midd_x):
                if (left == midd_idx):
                    behind_idx = right
                    break
                left = midd_idx
            
        return_intervals = []
        for idx, obj in enumerate(intervals):
            if (idx == behind_idx):
                return_intervals.append(new_interval)
            return_intervals.append(obj)
        return return_intervals




    # intervals length > 1
    def _find(self, 
        intervals, 
        new_interval, 
        removed_list = [],
        prev_position = None, # left | right | none
        is_prev_overlap = False,
        recursive_level = 0
    ):
        """
        return merged_interval and removed indexs
        """
        
        if not intervals:
            return new_interval, removed_list
        elif len(intervals) == 1:
            i1 = intervals[0]
            i2 = new_interval
            is_overlap = self._is_overlap(i1, i2)
            if (is_overlap):
                merged = self._merge(i1, i2)
                removed_list.append(intervals[0][0])
                return merged, removed_list
            else:
                return new_interval, removed_list


        index_1 = 0
        index_2 = len(intervals) - 1

        middle_i = math.floor((index_1 + index_2) / 2)
        middle_interval = intervals[middle_i]


        left_intervals = []
        right_intervals = []
        left_index_list = []
        right_index_list = []
        for idx, obj in enumerate(intervals):
            if (idx < middle_i):
                left_intervals.append(obj)
                left_index_list.append(idx)
            if (idx > middle_i):
                right_intervals.append(obj)
                right_index_list.append(idx)



        sorted = self._sort(new_interval, middle_interval)
        is_overlap = self._is_overlap(sorted[0], sorted[1])
        if is_overlap:
            
            removed_list.append(middle_interval[0])
            merged = self._merge(sorted[0], sorted[1])
            

            if prev_position == 'left' and is_prev_overlap:
                # merge
                for obj in left_intervals:
                    merged = self._merge(merged, obj)
                for idx in left_index_list:
                    removed_list.append(intervals[idx][0])
                left_intervals = []
            elif prev_position == 'right' and is_prev_overlap:
                # merge
                for obj in right_intervals:
                    merged = self._merge(merged, obj)
                for idx in right_index_list:
                    removed_list.append(intervals[idx][0])
                right_intervals = []

            

            # left
            left_merged, left_removed_list = self._find(
                intervals = left_intervals,
                new_interval = merged,
                removed_list = removed_list,
                prev_position = 'right',
                is_prev_overlap = True,
                recursive_level = recursive_level + 1
            )

            # right
            right_merged, right_removed_list = self._find(
                intervals = right_intervals,
                new_interval = merged,
                removed_list = removed_list,
                prev_position = 'left',
                is_prev_overlap = True,
                recursive_level = recursive_level + 1
            )



            # merged left and right
            final_merged = self._merge(left_merged, right_merged)
            # union removed list
            final_removed_list = self._union_idx(left_removed_list, right_removed_list)
            
            return final_merged, final_removed_list
        else:
            
            # if not overlap
            new_interval_position = ""
            order = self._order(middle_interval, new_interval)
            if (order == 'acs'):
                # can ignore left side intervals, do the right side
                merged, removed_list = self._find(
                    intervals = right_intervals,
                    new_interval = new_interval,
                    removed_list = removed_list,
                    prev_position = 'left',
                    is_prev_overlap = False,
                    recursive_level = recursive_level + 1
                )
                return merged, removed_list
            else:
                # can ignore right side intervals, do the left side
                merged, removed_list = self._find(
                    intervals = left_intervals,
                    new_interval = new_interval,
                    removed_list = removed_list,
                    prev_position = 'right',
                    is_prev_overlap = False,
                    recursive_level = recursive_level + 1
                )
                return merged, removed_list


                
    def _union_idx(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        new_list = list(set1.union(set2))
        return new_list
    
    def _is_overlap(self, interval1, interval2):
        s1 = interval1[0]
        e1 = interval1[1]
        s2 = interval2[0]
        e2 = interval2[1]
        if (
            (s2 >= s1 and s2 <= e1)
            or (s1 >= s2 and s1 <= e2)
        ):
            return True
        return False

    # only used for two overlapping intervals
    def _merge(self, interval1, interval2):
        sorted = self._sort(interval1, interval2)
        i1 = sorted[0]
        i2 = sorted[1]
        if (i1[1] >= i2[1]):
            # i1 totally includes i2
            return i1
        else:
            return [i1[0], i2[1]]


    def _order(self, interval1, interval2):
        if (interval1[0] <= interval2[0]):
            return "acs"
        return "desc"

    def _sort(self, interval1, interval2):
        i1 = interval1 if interval1[0] < interval2[0] else interval2
        i2 = interval2 if i1 == interval1 else interval1
        return [i1, i2]