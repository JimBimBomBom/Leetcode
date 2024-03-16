/**
 * Definition for singly-linked list->
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct Pointer
{
    int index;
    int value;
};

class Solution
{
public:
    ListNode *removeZeroSumSublists(ListNode *head)
    {
        // Only keep nodes with non zero values
        ListNode *probe = head;
        while (probe && probe->next)
        {
            if (probe->next->val == 0)
            {
                ListNode *curr_node = probe->next;
                while (curr_node->next)
                {
                    if (curr_node->val != 0)
                    {
                        probe->next = curr_node;
                        break;
                    }
                    curr_node = curr_node->next;
                }

                if (probe->next->val == 0)
                    probe->next = nullptr;
            }

            probe = probe->next;
        }
        if (head->val == 0)
            head = head->next;
        if (head == nullptr)
            return head;

        ListNode *nodes[1000] = {};

        printf("head: %d\n", head->val);
        ListNode *curr_node = head;
        int index = 0;
        while (curr_node != nullptr)
        {
            nodes[index] = curr_node;
            curr_node = curr_node->next;
            index += 1;
        }

        int size = index;
        printf("size: %d\n", size);



        
        while (true)
        {
            bool change_occured = false;
            for (int i = 1; i < size; i += 1)
            {
                printf("i: %d\n", i);
                if (nodes[i - 1]->val < 0 && nodes[i]->val >= 0)
                {
                    Pointer left = {i - 1, nodes[i - 1]->val};
                    Pointer right = {i, nodes[i]->val};
                    printf("left;RIGHT\n");
                    while (true)
                    {
                        printf("Index: left: %d, right: %d\n", left.index, right.index);
                        printf("Value: left: %d, right: %d\n", left.value, right.value);
                        if (left.value + right.value == 0)
                        {
                            change_occured = true;
                            if (left.index == 0)
                            {
                                head = nodes[right.index]->next;
                            }
                            else if (right.index == size)
                            {
                                nodes[left.index - 1]->next = nullptr;
                            }
                            else
                            {
                                nodes[left.index - 1]->next = nodes[right.index]->next;
                            }

                            for (int j = left.index; j <= right.index; j += 1)
                            {
                                nodes[j]->val = 0;
                            }
                            break;
                        }
                        else if (left.value * -1 < right.value)
                        {
                            if (nodes[left.index]->val < 0)
                            {
                                if (left.index == 0)
                                    break;
                                left.index -= 1;
                                left.value += nodes[left.index]->val;
                            }
                            else
                                break;
                        }
                        else
                        {
                            if (nodes[right.index]->val >= 0)
                            {
                                if (right.index == size - 1)
                                    break;
                                right.index += 1;
                                right.value += nodes[right.index]->val;
                            }
                            else
                                break;
                        }
                    }
                }
                else if (nodes[i - 1]->val >= 0 && nodes[i]->val < 0)
                {
                    Pointer left = {i - 1, nodes[i - 1]->val};
                    Pointer right = {i, nodes[i]->val};
                    printf("LEFT;right\n");
                    while (true)
                    {
                        printf("Index: left: %d, right: %d\n", left.index, right.index);
                        printf("Value: left: %d, right: %d\n", left.value, right.value);
                        if (left.index < 0 || right.index > size - 1)
                            break;
                        if (left.value + right.value == 0)
                        {
                            change_occured = true;
                            if (left.index == 0)
                            {
                                head = nodes[right.index]->next;
                            }
                            else if (right.index == size)
                            {
                                nodes[left.index - 1]->next = nullptr;
                            }
                            else
                            {
                                nodes[left.index - 1]->next = nodes[right.index]->next;
                            }

                            for (int j = left.index; j <= right.index; j += 1)
                            {
                                nodes[j]->val = 0;
                            }
                            break;
                        }
                        else if (left.value < right.value * -1)
                        {
                            if (nodes[left.index]->val >= 0)
                            {
                                if (left.index == 0)
                                    break;
                                left.index -= 1;
                                left.value += nodes[left.index]->val;
                            }
                            else
                                break;
                        }
                        else
                        {
                            if (nodes[right.index]->val < 0)
                            {
                                if (right.index == size - 1)
                                    break;
                                right.index += 1;
                                right.value += nodes[right.index]->val;
                            }
                            else
                                break;
                        }
                    }
                }
            }

            if (!change_occured)
            {
                break;
            }
        }

        return head;
    }
};
