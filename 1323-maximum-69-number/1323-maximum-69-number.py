class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert number to a list of characters (digits)
        num_list = list(str(num))
        
        # Find the first '6' and change it to '9'
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break  # only one change allowed
        
        # Convert back to integer and return
        return int("".join(num_list))
