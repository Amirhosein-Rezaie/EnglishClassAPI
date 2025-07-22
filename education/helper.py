from education.models import Terms


def return_value_cell_term_excel(col, queryset: Terms, row):
    value = row - 1
    term = queryset
    if col == 1:
        value = str(term.title)
    elif col == 2:
        value = str(term.work_book)
    elif col == 3:
        value = str(term.story_book)
    elif col == 4:
        value = str(term.student_book)
    elif col == 5:
        value = str(term.teacher)
    elif col == 6:
        value = int(term.tution)
    elif col == 7:
        value = str(term.start_date)
    elif col == 8:
        value = str(term.end_date)
    elif col == 9:
        value = str(term.start_time)
    elif col == 10:
        value = str(term.end_time)
    elif col == 11:
        value = str(term.type)
    elif col == 12:
        value = str(term.level)
    return value
