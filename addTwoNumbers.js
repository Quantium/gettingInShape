/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var root = new ListNode()
    var iter = root
    var res = 0
    while(l1 || l2 || res){
      let value1 = l1?l1.val:0
      let value2 = l2?l2.val:0
      let value = value1 + value2 + res
      res = Math.floor(value/10)
      value = Math.floor(value%10)
      
      iter = iter.next = new ListNode(value)
      
      l1 = l1?l1.next:0
      l2 = l2?l2.next:0
    }
    return root.next
  };