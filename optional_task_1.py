types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def del_duplicate(tickets):
    list_tickets = []
    unique_tickets = {}
    for key, value in tickets.items():
        unique_task = []
        for task in value:
            if task not in list_tickets:
                list_tickets.append(task)
                unique_task.append(task)
        unique_tickets[key] = unique_task
    return unique_tickets


def link_priority(types, tickets):
    tickets = del_duplicate(tickets)
    tickets_by_type = {}
    for key, value in types.items():
        if tickets.get(key):
            tickets_by_type[value] = tickets[key]

    return tickets_by_type


print(link_priority(types, tickets))
