def ballni_ol(matn):
   try:
      return int(matn)
   except ValueError:
      return("Ball son bo'lishi kerak")
text=input()
print(ballni_ol(text))