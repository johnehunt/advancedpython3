import fintech.accounts as accounts
import pymysql

def write_account_transaction_to_db(filename, account):
    print('Starting write of DB example')

    # Open database connection
    connection = pymysql.connect('localhost', 'user', 'password', 'accounts')

    # prepare a cursor object using cursor() method
    cursor = connection.cursor()

    try:
        # Execute INSERT command
        account_number = account.account_number
        name = account.account_holder
        cursor.execute(
            "INSERT INTO acc_info (idacc_info, name) " +
            "VALUES (" + account_number + ", '" + name + "')")
        # Commit the changes to the database

        # Write out the transactions
        for transaction in account.history:
            id = transaction.id
            action = transaction.action
            amount = transaction.amount
            statement = "INSERT into transactions (idtransactions, type, amount, account) VALUES (" + str(id) + ", '" + action + "', " + str(amount) + ", " + str(account_number) + ")"
            print(statement)
            cursor.execute(statement)
        connection.commit()
    except Exception as exp:
        # Something went wrong
        # rollback the changes
        print(exp)
        connection.rollback()

    # Close the database connection
    connection.close()

    print('Done Write DB Example')



print('Starting')
acc = accounts.CurrentAccount('123', 'John', 10.05, 100.0)
acc.deposit(23.45)
acc.withdraw(12.33)

print('Writing Account Transactions')
write_account_transaction_to_db('accounts.xlsx', acc)

print('Done')


