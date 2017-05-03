text_format = "{:^10}" * 5
test_format = "{:^10}/"
hero_names = ['Stefan', 'Made', 'This', 'Game']
hero_hp = ['100', '50', '5000', '20']
hero_maxmp = ['1000', '500', '9000', '200']
print text_format


print text_format.format("", *hero_names)
print text_format.format("", *hero_hp)

practice_text = '{}'
print practice_text.format(hero_names)
