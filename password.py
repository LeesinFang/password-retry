#密碼重設程式
password = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼: ') #訂正
	if pwd == password:
		print('登入成功!')
		break 	
	else:
		i = i-1
		print('密碼錯誤! 還有' , i, '次機會') #切三段 中間放整數
		if i == 0:
			break