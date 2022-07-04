def arithmetic_arranger(problems, results = False):
  # check if there are more than 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    top = ""
    middle = ""
    line = ""
    bottom = ""
    spacing = "    "
  
  # split problems and define variables
  for (x, p) in enumerate(problems):
    s = p.split()
    a = s[0]
    b = s[2]
    c = s[1]
    
    # convert string into integer
    try:
      aa = int(a)
      bb = int(b)
    except:
      return "Error: Numbers must only contain digits."
    
    # break if wrong operator or else add or subract integers
    if c == "*" or c == "/":
      return "Error: Operator must be '+' or '-'."
    else:
        if c == "+":
          m = aa + bb
          m = str(m)
        else:
          m = aa - bb
          m = str(m)

    # break if chars are greater than 4 or else format the arithmetic problems
    if len(a) > 4 or len(b) > 4:
      return "Error: Numbers cannot be more than four digits."
    else:
      length = max(len(a), len(b)) + 2
      if x < len(problems) - 1:
        top = top + a.rjust(length) + spacing
        middle = middle + c.ljust(0) + b.rjust(length-1) + spacing
        line = line + (length * "-") + spacing
        bottom = bottom + m.rjust(length) + spacing
      else:
        top = top + a.rjust(length)
        middle = middle + c + b.rjust(length - 1)
        line = line + (length * "-")
        bottom = bottom + m.rjust(length)

      # if second parameter is True, print out the result
      if results == True:
        arranged_problems = (top + "\n" + middle + "\n" + line + "\n" + bottom)
      else:
        arranged_problems = (top + "\n" + middle + "\n" + line)
  return arranged_problems