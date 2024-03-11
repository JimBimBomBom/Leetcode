class Solution {
public:
    string customSortString(string order, string s) {
        int insert_index = 0;

        printf("s: %s\n", s.c_str());

        for (int i = 0; i < order.size(); i += 1) {
            for (int j = insert_index; j < s.size(); j += 1) {
                if (s[j] == order[i]) {
                    swap(s[insert_index], s[j]);
                    insert_index += 1;
                }
            }
        }

        printf("s: %s\n", s.c_str());
        
        return s;
    }
};
