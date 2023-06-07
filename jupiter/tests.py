# from datetime import datetime


# class Saving:
#     def __init__(self, created_at: datetime):
#         self._created_at = created_at
#         self._amount = 0

#     def _only_positive(self, number):
#         if number > 0:
#             self._amount = number
#         else:
#             self._amount = 0

#     @property
#     def created_at(self):
#         return self._created_at

#     @property
#     def amount(self):
#         return self._amount

#     @amount.setter
#     def amount(self, amount):
#         if amount > 0:
#             self._amount = amount

#     def __repr__(self) -> str:
#         return f'{self._created_at.strftime("%d-%m-%Y")} - {self._amount}'


# class Savings:

#     def __init__(self):
#         self.savings = []

#     def add_saving(self, saving: Saving):
#         self.savings.append(saving)

#     @property
#     def total(self):
#         return sum([saving.amount for saving in self.savings])


# s1 = Saving(datetime(2020, 2, 14), 100)
# s2 = Saving(datetime(2020, 2, 15), 200)

# s3 = Saving(datetime(2020, 9, 9), -20)
# s1.amount = -23

# print("saving:", s1.amount)
# # savings = Savings()

# # savings.add_saving(s1)
# # savings.add_saving(s2)
# # savings.add_saving(s3)


# # for sav in savings.savings:
# #     print(sav)

# # print(savings.total)


to_sort = [
    {'name': 'Homer', 'age': 39},
    {'name': 'Bart', 'age': 10},
    {'name': 'Miso', 'age': 101},
]
new_list = sorted(to_sort, key=lambda x: x['name'])

print(to_sort)
print(new_list)
