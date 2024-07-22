from bank_accounts import * # * menas import all

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(3000, "Sara")

Sara.deposit(300)

Dave.withdraw(1200)

Dave.transfer(200, Sara)

jim = NewBank( 20000, "Jim")
jim.transfer(100000, Dave)