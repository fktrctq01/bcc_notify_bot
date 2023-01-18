class EmailDto:

    def __init__(self):
        self._id = None
        self._email_time = None
        self._trn_time = None
        self._trn_amount = None
        self._trn_currency = None
        self._balance = None
        self._balance_currency = None
        self._merchant = None

    @property
    def id(self):
        return self._id

    def with_id(self, id: int):
        self._id = id
        return self

    @property
    def email_time(self):
        return self._email_time

    def with_email_time(self, time: str):
        self._email_time = time
        return self

    @property
    def trn_time(self):
        return self._trn_time

    def with_trn_time(self, time: str):
        self._trn_time = time
        return self

    @property
    def trn_amount(self):
        return self._trn_amount

    def with_trn_amount(self, trn_amount: str):
        self._trn_amount = trn_amount
        return self

    @property
    def trn_currency(self):
        return self._trn_currency

    def with_trn_currency(self, trn_currency: str):
        self._trn_currency = trn_currency
        return self

    @property
    def balance(self):
        return self._balance

    def with_balance(self, balance: str):
        self._balance = balance
        return self

    @property
    def balance_currency(self):
        return self._balance_currency

    def with_balance_currency(self, balance_currency: str):
        self._balance_currency = balance_currency
        return self

    @property
    def merchant(self):
        return self._merchant

    def with_merchant(self, merchant: str):
        self._merchant = merchant
        return self

    def __repr__(self) -> str:
        return f"id={self._id}, email_time={self._email_time}, " \
               f"trn_time={self._trn_time} trn_amount={self._trn_amount} trn_currency={self._trn_currency} " \
               f"balance={self._balance} balance_currency={self._balance_currency} " \
               f"merchant={self._merchant}"

    def __str__(self) -> str:
        return f"{self._trn_time.strftime('%d.%m %H:%M')} покупка на сумму {self._trn_amount} {self._trn_currency} {self._merchant}" \
               f"\nБаланс {self._balance} {self._balance_currency}" \
               f"\nУведомление получено {self._email_time.strftime('%d.%m %H:%M')}"
