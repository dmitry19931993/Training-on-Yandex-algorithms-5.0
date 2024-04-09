Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном в обе стороны вертикальном столбе, который для удобства можно представить как числовую прямую. Изначально Петя находится в точке 
0
.
Вася кормит Петю ягодами. У него есть 
n
 ягод, каждая в единственном экземпляре. Вася знает, что если утром он даст Пете ягоду с номером 
i
, то поев и набравшись сил, за остаток дня Петя поднимется на 
a
i
 единиц вверх по столбу, но при этом за ночь, потяжелев, съедет на 
b
i
 единиц вниз. Параметры различных ягод могут совпадать.
Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь. Ближайшие 
n
 дней он будет кормить Петю ягодами из своего запаса таким образом, чтобы максимальная высота, на которой побывал Петя за эти 
n
 дней была максимальной. К сожалению, Вася не умеет программировать, поэтому он попросил вас о помощи. Найдите, максимальную высоту, на которой Петя сможет побывать за эти 
n
 дней и в каком порядке Вася должен давать Пете ягоды, чтобы Петя смог её достичь!

Формат ввода
В первой строке входных данных дано число 
n
 (
1
≤
n
≤
5
⋅
1
0
5
) — количество ягод у Васи. В последующих 
n
 строках описываются параметры каждой ягоды. В 
i
+
1
 строке дано два числа 
a
i
 и 
b
i
 (
0
≤
a
i
,
b
i
≤
1
0
9
) — то, насколько поднимется улитка за день после того, как съест 
i
 ягоду и насколько опуститься за ночь.
Формат вывода
В первой строке выходных данных выведите единственное число — максимальную высоту, которую сможет достичь Петя, если Вася будет его кормить оптимальным образом. В следующей строке выведите 
n
 различных целых чисел от 
1
 до 
n
 — порядок, в котором Вася должен кормить Петю (
i
 число в строке соответствует номеру ягоды, которую Вася должен дать Пете в 
i
 день чтобы Петя смог достичь максимальной высоты).