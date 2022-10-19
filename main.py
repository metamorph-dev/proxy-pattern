from bank_account.bank_account import BankAccount
from bank_account.bank_account_protocol import BankAccountProtocol
from bank_account.proxy_signal import ProxySignal


def cash_out(bank_account: BankAccountProtocol) -> None:
    bank_account.sub(bank_account.amount)


def main() -> None:
    account1 = BankAccount('Tom')
    account2 = ProxySignal(
        bank_account=BankAccount('Alex'),
        post_add=(lambda account, value: print(f'Added {value} to {account.username} amount')),
        pre_sub=(lambda account, value: print(f'Preparing for subtract {value} from {account.username} amount...')),
        post_sub=(lambda account, value: print(f'Subtracted {value} from {account.username} amount')),
    )

    account1.add(400)

    account2.add(100)
    account2.add(100)
    account2.add(100)

    cash_out(account1)
    cash_out(account2)


if __name__ == '__main__':
    main()
