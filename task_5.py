class TestCase:
    def __init__(self, steps={}, result=None):
        steps = {'Шаги': {},
                 'Ожидаемый результат': {}}  # create dict
        self.steps = steps
        self.result = result

    def set_step(self, num, step):
        self.steps['Шаги'][num] = step  # add step in dict

    def delete_step(self, num):
        self.steps['Шаги'].pop(num)  # del step in dict

    def set_result(self, result):
        self.steps['Ожидаемый результат'] = result  # add result in dict

    def get_test_case(self):
        print(self.steps)  # print dict


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()
