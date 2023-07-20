def reverse_words(sentence):
   sentence = ' '.join(sentence.split())
   s_list = list(sentence)
   s_list.reverse()

   left, right = 0, 0
   for i, curr_ch in enumerate(s_list):
      if curr_ch.isspace() or i == len(s_list) - 1:
            if curr_ch.isspace():
               right = i - 1
            else:
               right = i
            while left < right:
               s_list[left], s_list[right] = s_list[right], s_list[left]
               left += 1
               right -= 1
            left, right = i + 1, i + 1

   return ''.join(s_list)