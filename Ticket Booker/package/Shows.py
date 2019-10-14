class theaterMovies:
  def movies():
    show1 = 1
    show2 = 2
    show3 = 3
    show4 = 4
    print(' ')
    print('Nite Striker is 1, Day Breaker is 2, Lethal Dragon is 3 and Man Cave is 4')
    print(' ')
    customer = int(input('please enter your movie of choice: '))
    while(True):
      if(customer == show1 or customer == show2):
        print(' ')
        print('thank you your show is in theatre 1 and 2 please pick your seats')
        break
      elif(customer == show3 or customer == show4):
        print(' ')
        print('thank you your show is in theatre 3 and 4 please pick your seats')
        break 
      else:
        print(' ')
        print('error')
        print(' ')
        customer = int(input('please enter your movie of choice: '))
  movies()