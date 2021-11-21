def main():
   print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])
   s='ias alab'
   print(s[::-1])

if __name__== "__main__":
  main()
