price = 40
message = input()

print(f'{len(message) * price // 100} р. {len(message) * price % 100}коп.')
