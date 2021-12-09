from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    list_of_bad_words = ['suka', 'blyat', 'debil', 'blya']
    for bad_word in list_of_bad_words:
        while True:
            if bad_word in value:
                value = value.replace(bad_word, '*' * len(bad_word))
            else:
                break
    return value
