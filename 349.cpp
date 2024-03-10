// void swap(int& a, int& b) {
//     int temp = a;
//     a = b;
//     b = temp;
// }

// void sort(vector<int>& v) {
//     for (int i = 0; i < v.size(); i += 1) {
//         for (int j = i + 1; j < v.size(); j += 1) {
//             if (v[i] > v[j]) {
//                 swap(v[i], v[j]);
//             }
//         }
//     }
// }

void unique(vector<int>& v) {
    // sort(v);
    v.sort(v.begin(), v.end());
    int unique_insert_index = 1;
    int search_index = 1;
    while (search_index < v.size()) {
        if (v[unique_insert_index - 1] != v[search_index]) {
            v[unique_insert_index] = v[search_index];
            unique_insert_index += 1;
        }
        search_index += 1;
    }

    v.resize(unique_insert_index);
}

vector<int> intersect(vector<int>& v1, vector<int>& v2) {
    // unique(v1);
    // unique(v2);
    v1.unique();
    v2.unique();
    vector<int> result;
    int i = 0;
    int j = 0;
    while (i < v1.size() && j < v2.size()) {
        if (v1[i] == v2[j]) {
            result.push_back(v1[i]);
            i += 1;
            j += 1;
        } else if (v1[i] < v2[j]) {
            i += 1;
        } else {
            j += 1;
        }
    }
    return result;
}

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        return intersect(nums1, nums2);
    }
};
