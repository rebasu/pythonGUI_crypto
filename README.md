# pythonGUI_crypto
Python GUI for UncleEngineer group

Process

1. create GUI Set resolution / title
2. Create login form (Username, Password)
3. Create Button in login form
4. Create Label linked to register form (New window)
5. Use template in 2. create register form
6. Create Button in register form that store username and password in 'log.csv' when clicked
7. Read the data in 'log.csv' and compare to input in login form
	7.1 If the input same as any data in 'log.csv' navigate to new frame
	7.2 If not 'Incorrect username or password' will be appeared
8. Use library 'hashlib' encode password that collected in 6. by SHA-256
9. Add Hashing password function in 7.
10. Create Logout Button and link to login form when clicked
11. Create About Me form (Name / Role / Further plans / Address)
12. Show current username in each form (exclude login and register form)
13. Create Account form (Balance / Number of buy-sell)
14. Create table template In Allocation form
15. Create insert initial money button and store in log.csv index 3
16. Create order button and do the internal template
17. Do calculate algorithm check conditions:
	17.1 Amount / Price is positive number
	17.2 FOR BUY ORDER: current money MUST MORE than calculate money
	17.3 FOR SELL ORDER: current amount MUST LESS than given amount
18. Store the BUY / SELL order in 'order{username}.csv'
19. Do the CRUD for table and csv file:
	19.1 C (Create) when do the buy or sell order
	19.2 R (Read) when show the result in the table
	19.3 U (Update) when buy or sell order / click undo button
	19.4 D (Delete) when click undo button / clear order / clear initial
20. Count the amount of each coin and show under the table
21. Show the current money and show in allocation tab and create order tab
22. Create change password feature in account tab
	MEMO: THE NEW PASSWORD CAN BE ANYTHING (IT SHOULD NOT BE SAME AS PREVIOUS)
23. Link the balance (current money) and number of buy-sell (number or orders)
24. Do UX/UI Design.
