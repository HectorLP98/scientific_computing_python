def arithmetic_arranger(problems, val=False):
  operand_1=[]
  operand_2=[]
  operator=[]
  result=[]
  second_num=[]
  first_num=[]
  #print(len(problems))
    
    
  if len(problems)>=6:
    return'Error: Too many problems.'
  else:
    for i in range(0,len(problems)):
            
      x=problems[i]
      x_split=x.split()
      first_num.append(x_split[0])
      second_num.append(x_split[2])
      operator.append(x_split[1])
      if len(x_split[0])>4 or len(x_split[2])>4:
        return "Error: Numbers cannot be more than four digits."
      else:
        if operator[i] != '+' and operator[i] != '-':
          return "Error: Operator must be '+' or '-'."
        else:                
          try:
            operand_1.append(int(x_split[0]))
            operand_2.append(int(x_split[2]))
          except:
            return "Error: Numbers must only contain digits."
  #print(f'operand_1 {operand_1}')
  #print(f'operand_2 {operand_2}')
  for i in range(0, len(problems)):
    if operator[i] == '+':
      result_one= operand_1[i]+operand_2[i]
      result.append(result_one)
    elif operator[i] == '-':
      result_one= operand_1[i]-operand_2[i]
      result.append(result_one)
  #print(f'result {result}')

  
  top_row=''
  dashes= ''
  solutions=''
  bottom_row=''
  for i in range(0, len(problems)):
    space_width=max(len(first_num[i]),len(second_num[i]))+2
    top_row+=first_num[i].rjust(space_width)
    dashes+='-'*space_width
    solutions+=str(result[i]).rjust(space_width)
    if i!=len(problems)-1:
      top_row += ' ' * 4
      dashes += ' ' * 4
      solutions += ' ' * 4
       
        
  for i in range(0,len(problems)):
    space_width=max(len(first_num[i]),len(second_num[i]))+1
    bottom_row+=operator[i]
    bottom_row+=second_num[i].rjust(space_width)
    if i!=len(problems)-1:
      bottom_row+=' '* 4
  
    
  if val:
    arranged_problems =top_row+'\n'+bottom_row+'\n'+dashes+'\n'+solutions
    
  else:
    arranged_problems =top_row+'\n'+bottom_row+'\n'+dashes 
  return arranged_problems