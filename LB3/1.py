import numpy as np


def load_electricity_data():
    generation_years = np.genfromtxt(
        'global-electricity-generation.csv',
        delimiter=',',
        skip_header=1,
        usecols=range(1, 31),
        missing_values='--',
        filling_values=np.nan
    )
    
    consumption_years = np.genfromtxt(
        'global-electricity-consumption.csv',
        delimiter=',',
        skip_header=1,
        usecols=range(1, 31),
        missing_values='--',
        filling_values=np.nan
    )
    
    countries = np.genfromtxt(
        'global-electricity-generation.csv',
        delimiter=',',
        skip_header=1,
        usecols=0, 
        dtype='U50',
        encoding='utf-8'
    )
    
    return countries, generation_years, consumption_years


countries, generation, consumption = load_electricity_data()

print(f"Данные загружены")


# ВТОРАЯ ЧАСТЬ ЗАДАНИЯ
last_5_years_indices = range(25, 30)

avg_generation_last_5 = np.nanmean(generation[:, last_5_years_indices], axis=1)
avg_consumption_last_5 = np.nanmean(consumption[:, last_5_years_indices], axis=1)

print("\nСреднее производство за 5 лет::")
for i in range(len(avg_generation_last_5)):
    print(f"{countries[i]}: {avg_generation_last_5[i]:.2f}")

print("\nСреднее потребление за 5 лет::")
for i in range(len(avg_consumption_last_5)):
    print(f"{countries[i]}: {avg_consumption_last_5[i]:.2f}")


# ТРЕТЬЯ ЧАСТЬ ЗАДАНИЯ
# 3.1. Суммарное потребление по всем странам за каждый год
total_consumption_per_year = np.nansum(consumption, axis=0)

# 3.2. Максимальное количество электроэнергии, произведенное одной страной за один год
max_production_single = np.nanmax(generation)

# 3.3. Страны, производящие более 500 млрд кВт*ч в среднем за последние 5 лет
high_production_countries = countries[avg_generation_last_5 > 500]

# 3.4. 10% стран с наибольшим потреблением в среднем за последние 5 лет
threshold_90_percent = np.nanquantile(avg_consumption_last_5, 0.9)
top_10_consumption = countries[avg_consumption_last_5 >= threshold_90_percent]

# 3.5. Страны, увеличившие производство в 2021 vs 1992 более чем в 10 раз
production_1992 = generation[:, 0]
production_2021 = generation[:, -1]
increase_10_times = countries[(production_2021 / production_1992) > 10]

# 3.6. Страны с суммарным потреблением >100 млрд кВт*ч и дефицитом производства
total_consumption_all_years = np.nansum(consumption, axis=1)
total_generation_all_years = np.nansum(generation, axis=1)
deficit_countries = countries[(total_consumption_all_years > 100) & 
                             (total_generation_all_years < total_consumption_all_years)]

# 3.7. Страна с наибольшим потреблением в 2020 году
consumption_2020 = consumption[:, -2]
max_consumption_2020_idx = np.nanargmax(consumption_2020)
country_max_consumption_2020 = countries[max_consumption_2020_idx]

print("3.1. Суммарное потребление по годам:")
for i in range(len(total_consumption_per_year)):
    print(f"{1992+i}: {total_consumption_per_year[i]}")
print("3.2. Максимальное производство одной страной за год:", max_production_single)
print("3.3. Страны с производством >500 млрд кВт*ч: " + ', '.join(high_production_countries))
print("3.4. 10% стран с наибольшим потреблением: " + ', '.join(top_10_consumption))
print("3.5. Страны с ростом производства >10 раз: " + ', '.join(increase_10_times))
print("3.6. Страны с дефицитом и потреблением >100 млрд: " + ', '.join(deficit_countries))
print("3.7. Страна с наибольшим потреблением в 2020:", country_max_consumption_2020)
