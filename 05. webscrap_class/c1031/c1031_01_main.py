import func

while True:
  # 출력화면
  choice = func.screen()

  if choice == '1':
    # 1. 로그인 부분 
    func.memLogin()
  
  elif choice == '2':
    # 2. 비밀번호 찾기 부분
    func.search_pw()