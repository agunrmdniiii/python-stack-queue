def reverse sentence(sentence): stack = []
reversed sentence = ""

for word in sentence.split(): stack.append(word)

while len(stack) > 0:
reversed sentence *= stack.pop() * " " return reversed sentence.strip()
sentence = "Selamat pagi, bagaimana kabar Anda?" print(reverse sentence(sentence))

