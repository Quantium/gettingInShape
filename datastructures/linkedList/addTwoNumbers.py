#!/usr/bin/python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        # Crea un dummy de ListNode
        res =ListNode
        # Establece el current para el loop con el mismo dummy
        ll = res
        # Establece carry a 0, es con lo que vamos a llevar nuestro residuo
        c = 0
        # Mientras que l1 o l2 no sean 'None' o carry no sea 0 ...
        # Mientras existan nodos o no haya ningún residuo por sumar, osease que sea 0
        while l1 or l2 or c:
            # Obtiene el valor de l1 y l2, si no existe lo deja en 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Suma todos los valores
            val = v1 + v2 + c
            # Saca el carry (lo que llevamos) dividiendo sin decimales el valor por si es mayor de 10
            c = val//10
            # Saca el valor ya sin el carry, obteniendo el residuo de la división entre 10 (ej: 14%10=4 y 14//10=1)
            v = val%10
            # Establece el next del índice con el valor obtenido de las suma sin carry
            ll.next = ListNode(v)
	        # Establece el índice al next del anterior
	        # En caso de que sea el primero, no importa, se deshecha
            ll = ll.next
            # Establece l1 y l2 con el siguiente valor de los nodos, si no existe entonces establece None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # A menos que haya un residuo en carry se detendría el loop
        # Devuelve el dummy.next, porque el valor de dummy está vacío y el loop empezó a llenarlo en el next de la primera iteración
        return ll.next

sol = Solution()
res = sol.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))),ListNode(5,ListNode(6,ListNode(4))))
print(res)
