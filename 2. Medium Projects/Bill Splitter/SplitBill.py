class SplitBill:
    bill_dictionary = {}
    
    def __init__(self, list_of_friends, bill_amount):
        self.bill_dictionary = self.make_bill_dictionary(list_of_friends, bill_amount)
    

    def make_bill_dictionary(self, list_of_friends, bill_amount):
        dic = {}
        split_bill_amount = round(bill_amount / len(list_of_friends), 2)
        for friend in list_of_friends:
            dic[friend] = split_bill_amount
        return dic

    def update_lucky_friend(self, lucky_friend):
        to_increase = (self.bill_dictionary[lucky_friend]) / (len(self.bill_dictionary) - 1)
        for friend in self.bill_dictionary:
            self.bill_dictionary[friend] += to_increase
        self.bill_dictionary[lucky_friend] = 0
